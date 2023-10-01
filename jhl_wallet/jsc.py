from web3 import (
    Web3,
    HTTPProvider,
)

from web3.middleware import geth_poa_middleware
from jhl_wallet.exceptions import (
    JscErrorException
)


class Jsc:
    """Abstraction over Jericoin node connection."""

    def __init__(self):
        self.w3 = Web3(HTTPProvider("https://rpc.jsc.jericoin.com"))
        self.w3.middleware_onion.inject(geth_poa_middleware,layer=0)
        pass

    def get_web3(self):
        if not self.w3.isConnected():
            raise JscErrorException()

        return self.w3
