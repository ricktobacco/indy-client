from sovrin_client.cli.constants import \
    CLIENT_GRAMS_CLIENT_WITH_IDENTIFIER_FORMATTED_REG_EX, \
    CLIENT_GRAMS_CLIENT_ADD_FORMATTED_REG_EX, SEND_NYM_FORMATTED_REG_EX, \
    GET_NYM_FORMATTED_REG_EX, \
    ADD_ATTRIB_FORMATTED_REG_EX, SEND_CLAIM_DEF_FORMATTED_REG_EX, \
    REQ_CRED_FORMATTED_REG_EX, LIST_CREDS_FORMATTED_REG_EX, \
    GEN_CRED_FORMATTED_REG_EX, ADD_GENESIS_FORMATTED_REG_EX, \
    INIT_ATTR_REPO_FORMATTED_REG_EX, ADD_ATTRS_FORMATTED_REG_EX, \
    STORE_CRED_FORMATTED_REG_EX, \
    GEN_VERIF_NONCE_FORMATTED_REG_EX, PREP_PROOF_FORMATTED_REG_EX, \
    VERIFY_PROOF_FORMATTED_REG_EX, \
    ADD_ATTRS_PROVER_FORMATTED_REG_EX, CONNECT_FORMATTED_REG_EX, \
    SHOW_FILE_FORMATTED_REG_EX, LOAD_FILE_FORMATTED_REG_EX, \
    SHOW_LINK_FORMATTED_REG_EX, SYNC_LINK_FORMATTED_REG_EX, \
    ACCEPT_LINK_FORMATTED_REG_EX, SHOW_CLAIM_FORMATTED_REG_EX, \
    REQUEST_CLAIM_FORMATTED_REG_EX, SHOW_CLAIM_REQ_FORMATTED_REG_EX, \
    SET_ATTRIBUTE_FORMATTED_REG_EX, \
    SEND_ISSUER_KEY_FORMATTED_REG_EX, SEND_CLAIM_FORMATTED_REG_EX, \
    PING_TARGET_FORMATTED_REG_EX


def getNewClientGrams():
    # TODO: Why do we have to manually pipe each regex except the last
    # one? Fix this
    return [
        ADD_GENESIS_FORMATTED_REG_EX,
        # Regex for `new client steward with identifier <nym>`
        CLIENT_GRAMS_CLIENT_WITH_IDENTIFIER_FORMATTED_REG_EX,
        # Regex for `client steward add sponsor bob` or `client steward
        # add user bob`
        CLIENT_GRAMS_CLIENT_ADD_FORMATTED_REG_EX,
        SEND_NYM_FORMATTED_REG_EX,
        GET_NYM_FORMATTED_REG_EX,
        ADD_ATTRIB_FORMATTED_REG_EX,
        SEND_CLAIM_DEF_FORMATTED_REG_EX,
        SEND_ISSUER_KEY_FORMATTED_REG_EX,
        REQ_CRED_FORMATTED_REG_EX,
        LIST_CREDS_FORMATTED_REG_EX,
        GEN_CRED_FORMATTED_REG_EX,
        STORE_CRED_FORMATTED_REG_EX,
        GEN_VERIF_NONCE_FORMATTED_REG_EX,
        PREP_PROOF_FORMATTED_REG_EX,
        VERIFY_PROOF_FORMATTED_REG_EX,
        INIT_ATTR_REPO_FORMATTED_REG_EX,
        ADD_ATTRS_FORMATTED_REG_EX,
        SHOW_LINK_FORMATTED_REG_EX,
        SHOW_FILE_FORMATTED_REG_EX,
        LOAD_FILE_FORMATTED_REG_EX,
        ADD_ATTRS_PROVER_FORMATTED_REG_EX,
        CONNECT_FORMATTED_REG_EX,
        SYNC_LINK_FORMATTED_REG_EX,
        ACCEPT_LINK_FORMATTED_REG_EX,
        SHOW_CLAIM_REQ_FORMATTED_REG_EX,
        SHOW_CLAIM_FORMATTED_REG_EX,
        REQUEST_CLAIM_FORMATTED_REG_EX,
        SET_ATTRIBUTE_FORMATTED_REG_EX,
        PING_TARGET_FORMATTED_REG_EX,
        SEND_CLAIM_FORMATTED_REG_EX
    ]


NEXT_COMMANDS_TO_TRY_TEXT = "Try Next:"
USAGE_TEXT = "Usage:"

