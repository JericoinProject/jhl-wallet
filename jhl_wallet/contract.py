import time
from jhl_wallet.jsc import (
    Jsc,
)
from jhl_wallet.utils import (
    get_abi_json,
)


class Contract:
    """Abstraction over ERC20 tokens"""

    def __init__(self, configuration, address):
        """
        Constructor
        :param address: contract address or ESN name
        :type address: string
        """
        self.conf = configuration
        self.address = address

        self.w3 = Jsc().get_web3()
        self.contract = self.w3.eth.contract(address=address, abi=get_abi_json())
        self.contract_decimals = self.contract.functions.decimals().call()

    def add_new_contract(self, contract_symbol, contract_address):
        """
        Add ERC20 token to the wallet
        :param contract_symbol: token symbol
        :param contract_address: contract address
        :return:
        """
        self.conf.add_contract_token(contract_symbol, contract_address)

    def get_balance(self, wallet_address):
        """
        Get wallet's ballance of self.contract
        :param wallet_address: this wallet address
        :type wallet_address: string
        :return: balance as decimal number
        """
        return self.contract.functions.balanceOf(wallet_address).call() / (10 ** self.contract_decimals)

    def get_decimals(self):
        """
        Returns the number of decimals
        :return: integer
        """
        return self.contract_decimals

    def get_erc20_contract(self):
        """
        Returns w3.eth.contract instance
        :return:
        """
        return self.contract


# w3 = jsc().get_web3()
#
# contract = w3.eth.contract(address=fictioncoin_address, abi=get_abi_json())
# # contract = w3.eth.contract(address=binancecoin_address, abi=get_abi_json())
# print(contract.functions.balanceOf(my_address).call() / 10**18)
# print(contract.functions.decimals().call())

#
# nonce = w3.eth.getTransactionCount(my_address)
# txn_dict = contract.functions.transfer(metamask_address, 2 * (10**18)).buildTransaction({
#     'chainId': 707007,
#     'gas': 140000,
#     'gasPrice': w3.toWei('40', 'gwei'),
#     # 'gasPrice': w3.eth.gasPrice * 10 * 2,
#     'nonce': nonce,
# })
#
# signed_txn = w3.eth.account.signTransaction(txn_dict, private_key=priv_key)
# tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
#
# print('Pending', end='', flush=True)
# while True:
#     tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
#     if tx_receipt is None:
#         print('.', end='', flush=True)
#         time.sleep(1)
#     else:
#         print('\nTransaction validated!')
#         break
# print(tx_hash.hex())

