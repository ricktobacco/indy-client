import json
from _sha256 import sha256

from plenum.common.eventually import eventually
from plenum.common.port_dispenser import genHa
from plenum.common.signer_simple import SimpleSigner
from plenum.common.txn import TARGET_NYM, ROLE
from plenum.test.cli.helper import TestCliCore, assertAllNodesCreated, \
    checkAllNodesStarted
from plenum.test.testable import Spyable
from sovrin_client.cli.cli import SovrinCli
from sovrin_client.client.wallet.link import Link


@Spyable(methods=[SovrinCli.print, SovrinCli.printTokens])
class TestCLI(SovrinCli, TestCliCore):
    pass


def sendNym(cli, nym, role):
    cli.enterCmd("send NYM {}={} "
                 "{}={}".format(TARGET_NYM, nym,
                                ROLE, role))


def checkGetNym(cli, nym):
    printeds = ["Getting nym {}".format(nym), "Transaction id for NYM {} is "
        .format(nym)]
    checks = [x in cli.lastCmdOutput for x in printeds]
    assert all(checks)
    # TODO: These give NameError, don't know why
    # assert all([x in cli.lastCmdOutput for x in printeds])
    # assert all(x in cli.lastCmdOutput for x in printeds)


def checkAddAttr(cli):
    assert "Adding attributes" in cli.lastCmdOutput


def chkNymAddedOutput(cli, nym):
    checks = [x['msg'] == "Nym {} added".format(nym) for x in cli.printeds]
    assert any(checks)


def checkConnectedToEnv(cli):
    # TODO: Improve this
    assert "now connected to" in cli.lastCmdOutput


def ensureConnectedToTestEnv(cli):
    if not cli.activeEnv:
        cli.enterCmd("connect test")
        cli.looper.run(
            eventually(checkConnectedToEnv, cli, retryWait=1, timeout=10))


def ensureNymAdded(cli, nym, role=None):
    ensureConnectedToTestEnv(cli)
    cmd = "send NYM {dest}={nym}".format(dest=TARGET_NYM, nym=nym)
    if role:
        cmd += " {ROLE}={role}".format(ROLE=ROLE, role=role)
    cli.enterCmd(cmd)
    cli.looper.run(
        eventually(chkNymAddedOutput, cli, nym, retryWait=1, timeout=10))

    cli.enterCmd("send GET_NYM {dest}={nym}".format(dest=TARGET_NYM, nym=nym))
    cli.looper.run(eventually(checkGetNym, cli, nym, retryWait=1, timeout=10))

    cli.enterCmd('send ATTRIB {dest}={nym} raw={raw}'.
                 format(dest=TARGET_NYM, nym=nym,
                        # raw='{\"attrName\":\"attrValue\"}'))
                        raw=json.dumps({"attrName": "attrValue"})))
    cli.looper.run(eventually(checkAddAttr, cli, retryWait=1, timeout=10))


def ensureNodesCreated(cli, nodeNames):
    cli.enterCmd("new node all")
    # TODO: Why 2 different interfaces one with list and one with varags
    assertAllNodesCreated(cli, nodeNames)
    checkAllNodesStarted(cli, *nodeNames)


def getFileLines(path):
    filePath = SovrinCli._getFilePath(path)
    with open(filePath, 'r') as fin:
        lines = fin.readlines()
    alteredLines = []
    for line in lines:
        alteredLines.append(line.replace('{', '{{').replace('}', '}}'))
    return alteredLines


def getLinkInvitation(name, wallet) -> Link:
    existingLinkInvites = wallet.getMatchingLinks(name)
    li = existingLinkInvites[0]
    return li


def getPoolTxnData(nodeAndClientInfoFilePath, poolId, newPoolTxnNodeNames):
    data={}
    data["seeds"]={}
    data["txns"]=[]
    for index, n in enumerate(newPoolTxnNodeNames, start=1):
        newStewardAlias = poolId + "Steward" + str(index)
        stewardSeed = (newStewardAlias + "0" * (32 - len(newStewardAlias))).encode()
        data["seeds"][newStewardAlias] = stewardSeed
        stewardSigner = SimpleSigner(seed=stewardSeed)
        data["txns"].append({
                "dest": stewardSigner.verkey,
                "role": "STEWARD", "type": "NYM",
                "alias": poolId + "Steward" + str(index),
                "txnId": sha256("{}".format(stewardSigner.verkey).encode()).hexdigest()
        })

        newNodeAlias = n
        nodeSeed = (newNodeAlias + "0" * (32 - len(newNodeAlias))).encode()
        data["seeds"][newNodeAlias] = nodeSeed
        nodeSigner = SimpleSigner(seed=nodeSeed)
        data["txns"].append({
                "dest": nodeSigner.verkey,
                "type": "NEW_NODE",
                "identifier": stewardSigner.verkey,
                "data": {
                    "client_ip": "127.0.0.1",
                    "alias": newNodeAlias,
                    "node_ip": "127.0.0.1",
                    "node_port": genHa()[1],
                    "client_port": genHa()[1]
                },
                "txnId": sha256("{}".format(nodeSigner.verkey).encode()).hexdigest()
        })
    return data


def prompt_is(prompt):
    def x(cli):
        assert cli.currPromptText == prompt
    return x
