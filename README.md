# jhl-wallet 

Command line wallet for Jericoin and ERC20 tokens.
## Environment
-- Ubuntu 18.04
-- Python 3.6.9
-- GCC 8.4.0
## Installation
1. Clone this repository<br>
2. Navigate to the project's root dir<br>
2. Set virtual environment<br>
	$ python3 -m venv venv<br>
	$ source venv/bin/activate<br>
	$ (venv) pip install --upgrade pip setuptools<br>
	$ (venv) pip install .<br>
4. Run `jhl-wallet --help` <br>
 
## Usage

```
jhl-wallet --help
Usage: jhl-wallet [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  add-token         Add new ERC20 contract.
  get-balance       Get address balance.
  get-wallet        Get wallet account from encrypted keystore.
  list-tokens       List all added tokens.
  network           Get connected network (Mainnet, Ropsten) defined in...
  new-wallet        Creates new wallet and store encrypted keystore file.
  restore-wallet    Creates new wallet and store encrypted keystore file.
  reveal-seed       Reveals private key from encrypted keystore.
  send-transaction  Sends transaction.
```

### Create wallet
Create new wallet:
```
$ jhl-wallet new-wallet   
  Passphrase from keystore: 

Account address: 0xB1f761734F00d1D368Ce6f82F755bBb3005538EB
Account pub key: 0xf94e03524a1bd803ee583a1f0de7eb1eb67a90d6802eeac22b90cfdd7ff491039441472e8db543467c0450d1b7c31b5e8f81616b99226775770f9dd531afd31a
Keystore path: /Users/Joe/.jhl-wallet/keystore
Remember these words to restore jhl-wallet: omit speak giant bright enable increase tube worth object timber bleak bullet
```
Show wallet:
```
$ jhl-wallet get-wallet   
Account address: 0xB1f761734F00d1D368Ce6f82F755bBb3005538EB
Account pub key: 0xf94e03524a1bd803ee583a1f0de7eb1eb67a90d6802eeac22b90cfdd7ff491039441472e8db543467c0450d1b7c31b5e8f81616b99226775770f9dd531afd31a
```

### Balances
Get JHL wallet balance:
```
$ jhl-wallet get-balance
Balance on address 0xB1f761734F00d1D368Ce6f82F755bBb3005538EB is: 1.234JHL
```
Add new ERC20 contract:
```
$ jhl-wallet add-token
  Contract address []: 0xa84a9dCd6CA401Ba5D56276790231550f76b828f
  Token symbol []: WJHL
  
New coin was added! WJHL 0xa84a9dCd6CA401Ba5D56276790231550f76b828f
```
Get balance of ERC20 token:
```
$ jhl-wallet get-balance --token WJHL
Balance on address 0xB1f761734F00d1D368Ce6f82F755bBb3005538EB is: 0.0WJHL
```

### Transactions
Send jhl to another wallet
```
$ jhl-wallet send-transaction 
  To address: []: 0xAAD533eb7Fe7F2657960AC7703F87E10c73ae73b
  Value to send: []: 0.01
  Password from keystore: 

transaction: {'to': '0xAAD533eb7Fe7F2657960AC7703F87E10c73ae73b', 'value': 10000000000000000, 'gas': 21000, 'gasPrice': 20000000000, 'nonce': 0, 'chainId': 707007}
Pending.................
Transaction validated!
Hash of the transaction: 0x193919d1ad2dc024349ccc035a15a697987bd33e1ff04e33f878e6f89f2ebbdf
Transaction cost was: 0.00042JHL
```

Send ERC20 contract tokens to another wallet
```
$ jhl-wallet send-transaction --token WJHL
  To address: []: 0xAAD533eb7Fe7F2657960AC7703F87E10c73ae73b
  Value to send: []: 0.9
  Password from keystore:
 
transaction: {'to': '0x19896cB57Bc5B4cb92dbC7D389DBa6290AF505Ce', 'value': 0, 'gas': 36536, 'gasPrice': 20000000000, 'nonce': 2, 'chainId': 707007, 'data': '0xa9059cbb000000000000000000000000a84a9dCd6CA401Ba5D56276790231550f76b828f0000000000000000000000000000000000000000000000000c7d713b49da0000'}

Transaction validated!
Hash of the transaction: 0x118556d192c2efb13ade6ccc2f18a631e14256972af9f7ec8a67067aaafc978c
Transaction cost was: 0.00073072JHL
```

### Wallet utils
Show connected network:
```
$ jhl-wallet network                
You are connected to the JSC mainnet network!
```
List all added tokens:
```
$ jhl-wallet list-tokens
JHL
WJHL
```
Restore wallet:
```
$ jhl-wallet restore-wallet
  Mnemonic sentence []: omit speak giant bright enable increase tube worth object timber bleak bullet
  Passphrase:
   
Account address: 0xB1f761734F00d1D368Ce6f82F755bBb3005538EB
Account pub key: 0xf94e03524a1bd803ee583a1f0de7eb1eb67a90d6802eeac22b90cfdd7ff491039441472e8db543467c0450d1b7c31b5e8f81616b99226775770f9dd531afd31a
Keystore path: /Users/user/.jhl-wallet/keystore
Remember these words to restore jhl-wallet: omit speak giant bright enable increase tube worth object timber bleak bullet
```
> Mnemonic sentence isn't fully compatible with BIP32 and BIP39 wallets. Therefore, only this implementation can reproduce mnemonic sentence and recreate seed!

Reveal wallet master private key:
```
$ jhl-wallet reveal-seed   
  Password from keystore: 
  
Account prv key: 0x843844a23e3ae7b6a695a346c981484b554ff1718299b0b42df3045
```
