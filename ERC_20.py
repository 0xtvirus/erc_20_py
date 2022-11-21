from web3 import Web3
import json
from dotenv import load_dotenv
import os
from web3.middleware import geth_poa_middleware

## Connect Avalanche Network C-chain RPC ####
url = 'https://api.avax.network/ext/bc/C/rpc'

### Check Connection ####
w3 = Web3(Web3.HTTPProvider(url))
if w3.isConnected():
    print("it is connected to avalanche network")

#### Essential for Avalanche
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
w3.clientVersion

with open('ERC_20_TOKEN.json') as fh:
    token_abi = json.load(fh)

class ERC_20_functions(object):
    def __init__(self, token_address, abi=token_abi):
        self.address = Web3.toChecksumAddress(token_address)
        self.abi = token_abi
        self.token = {}
        self.contract = w3.eth.contract(address=self.address, abi=abi)
        self.token['contract'] = self.address
        self.token['Name'] = self.contract.functions.name().call()
        self.token['Symbol'] = self.contract.functions.symbol().call()
        self.token['dec'] = self.contract.functions.decimals().call()


    def get_balance(self, account_address):
        self.account = Web3.toChecksumAddress(account_address)
        self.balance = self.contract.functions.balanceOf(self.account).call()/10**self.token['dec']
        return self.balance
    
    def get_allowance(self, owner, spender):
        owner = Web3.toChecksumAddress(owner)
        spender = Web3.toChecksumAddress(spender)
        allowance = self.contract.functions.allowance(owner, spender).call()/10**self.token['dec']
        return allowance



if __name__ == '__main__':
    USDT = '0xc7198437980c041c805A1EDcbA50c1Ce5db95118'
    usdt_token = ERC_20_functions(USDT)
    holder = '0x806f153c5bffedadd812a96162ecccd66866c8ce' # 14,933.881087 USDT.e

    print(usdt_token.token)
    print(usdt_token.get_balance(holder))