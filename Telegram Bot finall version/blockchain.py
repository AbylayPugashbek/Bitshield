from eth_account import Account
from web3 import Web3
from web3.middleware import geth_poa_middleware
from web3.exceptions import ContractLogicError

web3 = Web3(Web3.HTTPProvider('https://data-seed-prebsc-1-s1.bnbchain.org:8545'))

# Добавляем middleware для работы с PoA блокчейнами
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Устанавливаем аккаунт по умолчанию
account = web3.eth.account.from_key('0c9e1bdaabad36a10179227ff8845bdd242fc65f0a73e6f89d684e4854a67bfe')
web3.eth.defaultAccount = account.address
# Проверка подключения
assert web3.is_connected(), "Failed to connect to the blockchain network"

# Компилированные ABI и bytecode смарт-контракта
contract_abi = [
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_company",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_platform",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_login",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_password",
				"type": "string"
			}
		],
		"name": "addAccountData",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_company",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_platform",
				"type": "string"
			}
		],
		"name": "deactivateAccount",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_company",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_platform",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_newLogin",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_newPassword",
				"type": "string"
			}
		],
		"name": "updateAccountData",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "accounts",
		"outputs": [
			{
				"internalType": "string",
				"name": "company",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "platform",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "login",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "password",
				"type": "string"
			},
			{
				"internalType": "bool",
				"name": "isActive",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "index",
				"type": "uint256"
			}
		],
		"name": "getAccountData",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_company",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_platform",
				"type": "string"
			}
		],
		"name": "getLoginAndPassword",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getTotalAccounts",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
	
contract_bytecode = "6080604052348015600e575f80fd5b506116938061001c5f395ff3fe608060405234801561000f575f80fd5b506004361061007b575f3560e01c8063da6841aa11610059578063da6841aa146100ea578063de3f599f14610108578063e97a450614610139578063f2a40db8146101555761007b565b806333a09a331461007f57806387d0356a1461009b5780639247ff59146100b7575b5f80fd5b61009960048036038101906100949190610dbc565b610189565b005b6100b560048036038101906100b09190610dbc565b61028e565b005b6100d160048036038101906100cc9190610ec3565b6103d0565b6040516100e19493929190610f4e565b60405180910390f35b6100f26106f3565b6040516100ff9190610fbc565b60405180910390f35b610122600480360381019061011d9190610fd5565b6106fe565b60405161013092919061104b565b60405180910390f35b610153600480360381019061014e9190610fd5565b610903565b005b61016f600480360381019061016a9190610ec3565b6109df565b60405161018095949392919061109a565b60405180910390f35b5f6101948585610c43565b90505f6001826040516101a79190611141565b90815260200160405180910390205490505f81815481106101cb576101ca611157565b5b905f5260205f2090600502016004015f9054906101000a900460ff16610226576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161021d906111ce565b60405180910390fd5b835f828154811061023a57610239611157565b5b905f5260205f209060050201600201908161025591906113e6565b50825f828154811061026a57610269611157565b5b905f5260205f209060050201600301908161028591906113e6565b50505050505050565b5f6040518060a0016040528086815260200185815260200184815260200183815260200160011515815250908060018154018082558091505060019003905f5260205f2090600502015f909190919091505f820151815f0190816102f291906113e6565b50602082015181600101908161030891906113e6565b50604082015181600201908161031e91906113e6565b50606082015181600301908161033491906113e6565b506080820151816004015f6101000a81548160ff02191690831515021790555050505f6103618585610c43565b905060015f8054905061037491906114e2565b6001826040516103849190611141565b90815260200160405180910390208190555060015f805490506103a791906114e2565b6002866040516103b79190611141565b9081526020016040518091039020819055505050505050565b6060806060805f80549050851061041c576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016104139061155f565b60405180910390fd5b5f858154811061042f5761042e611157565b5b905f5260205f2090600502016004015f9054906101000a900460ff1661048a576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610481906111ce565b60405180910390fd5b5f80868154811061049e5761049d611157565b5b905f5260205f2090600502019050805f018160010182600201836003018380546104c790611219565b80601f01602080910402602001604051908101604052809291908181526020018280546104f390611219565b801561053e5780601f106105155761010080835404028352916020019161053e565b820191905f5260205f20905b81548152906001019060200180831161052157829003601f168201915b5050505050935082805461055190611219565b80601f016020809104026020016040519081016040528092919081815260200182805461057d90611219565b80156105c85780601f1061059f576101008083540402835291602001916105c8565b820191905f5260205f20905b8154815290600101906020018083116105ab57829003601f168201915b505050505092508180546105db90611219565b80601f016020809104026020016040519081016040528092919081815260200182805461060790611219565b80156106525780601f1061062957610100808354040283529160200191610652565b820191905f5260205f20905b81548152906001019060200180831161063557829003601f168201915b5050505050915080805461066590611219565b80601f016020809104026020016040519081016040528092919081815260200182805461069190611219565b80156106dc5780601f106106b3576101008083540402835291602001916106dc565b820191905f5260205f20905b8154815290600101906020018083116106bf57829003601f168201915b505050505090509450945094509450509193509193565b5f8080549050905090565b6060805f61070c8585610c43565b90505f60018260405161071f9190611141565b90815260200160405180910390205490505f818154811061074357610742611157565b5b905f5260205f2090600502016004015f9054906101000a900460ff1661079e576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610795906111ce565b60405180910390fd5b5f81815481106107b1576107b0611157565b5b905f5260205f2090600502016002015f82815481106107d3576107d2611157565b5b905f5260205f2090600502016003018180546107ee90611219565b80601f016020809104026020016040519081016040528092919081815260200182805461081a90611219565b80156108655780601f1061083c57610100808354040283529160200191610865565b820191905f5260205f20905b81548152906001019060200180831161084857829003601f168201915b5050505050915080805461087890611219565b80601f01602080910402602001604051908101604052809291908181526020018280546108a490611219565b80156108ef5780601f106108c6576101008083540402835291602001916108ef565b820191905f5260205f20905b8154815290600101906020018083116108d257829003601f168201915b505050505090509350935050509250929050565b5f61090e8383610c43565b90505f6001826040516109219190611141565b90815260200160405180910390205490505f818154811061094557610944611157565b5b905f5260205f2090600502016004015f9054906101000a900460ff166109a0576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610997906115c7565b60405180910390fd5b5f8082815481106109b4576109b3611157565b5b905f5260205f2090600502016004015f6101000a81548160ff02191690831515021790555050505050565b5f81815481106109ed575f80fd5b905f5260205f2090600502015f91509050805f018054610a0c90611219565b80601f0160208091040260200160405190810160405280929190818152602001828054610a3890611219565b8015610a835780601f10610a5a57610100808354040283529160200191610a83565b820191905f5260205f20905b815481529060010190602001808311610a6657829003601f168201915b505050505090806001018054610a9890611219565b80601f0160208091040260200160405190810160405280929190818152602001828054610ac490611219565b8015610b0f5780601f10610ae657610100808354040283529160200191610b0f565b820191905f5260205f20905b815481529060010190602001808311610af257829003601f168201915b505050505090806002018054610b2490611219565b80601f0160208091040260200160405190810160405280929190818152602001828054610b5090611219565b8015610b9b5780601f10610b7257610100808354040283529160200191610b9b565b820191905f5260205f20905b815481529060010190602001808311610b7e57829003601f168201915b505050505090806003018054610bb090611219565b80601f0160208091040260200160405190810160405280929190818152602001828054610bdc90611219565b8015610c275780601f10610bfe57610100808354040283529160200191610c27565b820191905f5260205f20905b815481529060010190602001808311610c0a57829003601f168201915b505050505090806004015f9054906101000a900460ff16905085565b60608282604051602001610c5892919061162f565b604051602081830303815290604052905092915050565b5f604051905090565b5f80fd5b5f80fd5b5f80fd5b5f80fd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b610cce82610c88565b810181811067ffffffffffffffff82111715610ced57610cec610c98565b5b80604052505050565b5f610cff610c6f565b9050610d0b8282610cc5565b919050565b5f67ffffffffffffffff821115610d2a57610d29610c98565b5b610d3382610c88565b9050602081019050919050565b828183375f83830152505050565b5f610d60610d5b84610d10565b610cf6565b905082815260208101848484011115610d7c57610d7b610c84565b5b610d87848285610d40565b509392505050565b5f82601f830112610da357610da2610c80565b5b8135610db3848260208601610d4e565b91505092915050565b5f805f8060808587031215610dd457610dd3610c78565b5b5f85013567ffffffffffffffff811115610df157610df0610c7c565b5b610dfd87828801610d8f565b945050602085013567ffffffffffffffff811115610e1e57610e1d610c7c565b5b610e2a87828801610d8f565b935050604085013567ffffffffffffffff811115610e4b57610e4a610c7c565b5b610e5787828801610d8f565b925050606085013567ffffffffffffffff811115610e7857610e77610c7c565b5b610e8487828801610d8f565b91505092959194509250565b5f819050919050565b610ea281610e90565b8114610eac575f80fd5b50565b5f81359050610ebd81610e99565b92915050565b5f60208284031215610ed857610ed7610c78565b5b5f610ee584828501610eaf565b91505092915050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f610f2082610eee565b610f2a8185610ef8565b9350610f3a818560208601610f08565b610f4381610c88565b840191505092915050565b5f6080820190508181035f830152610f668187610f16565b90508181036020830152610f7a8186610f16565b90508181036040830152610f8e8185610f16565b90508181036060830152610fa28184610f16565b905095945050505050565b610fb681610e90565b82525050565b5f602082019050610fcf5f830184610fad565b92915050565b5f8060408385031215610feb57610fea610c78565b5b5f83013567ffffffffffffffff81111561100857611007610c7c565b5b61101485828601610d8f565b925050602083013567ffffffffffffffff81111561103557611034610c7c565b5b61104185828601610d8f565b9150509250929050565b5f6040820190508181035f8301526110638185610f16565b905081810360208301526110778184610f16565b90509392505050565b5f8115159050919050565b61109481611080565b82525050565b5f60a0820190508181035f8301526110b28188610f16565b905081810360208301526110c68187610f16565b905081810360408301526110da8186610f16565b905081810360608301526110ee8185610f16565b90506110fd608083018461108b565b9695505050505050565b5f81905092915050565b5f61111b82610eee565b6111258185611107565b9350611135818560208601610f08565b80840191505092915050565b5f61114c8284611111565b915081905092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52603260045260245ffd5b7f4163636f756e74206973206e6f74206163746976652e000000000000000000005f82015250565b5f6111b8601683610ef8565b91506111c382611184565b602082019050919050565b5f6020820190508181035f8301526111e5816111ac565b9050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061123057607f821691505b602082108103611243576112426111ec565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f600883026112a57fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8261126a565b6112af868361126a565b95508019841693508086168417925050509392505050565b5f819050919050565b5f6112ea6112e56112e084610e90565b6112c7565b610e90565b9050919050565b5f819050919050565b611303836112d0565b61131761130f826112f1565b848454611276565b825550505050565b5f90565b61132b61131f565b6113368184846112fa565b505050565b5b818110156113595761134e5f82611323565b60018101905061133c565b5050565b601f82111561139e5761136f81611249565b6113788461125b565b81016020851015611387578190505b61139b6113938561125b565b83018261133b565b50505b505050565b5f82821c905092915050565b5f6113be5f19846008026113a3565b1980831691505092915050565b5f6113d683836113af565b9150826002028217905092915050565b6113ef82610eee565b67ffffffffffffffff81111561140857611407610c98565b5b6114128254611219565b61141d82828561135d565b5f60209050601f83116001811461144e575f841561143c578287015190505b61144685826113cb565b8655506114ad565b601f19841661145c86611249565b5f5b828110156114835784890151825560018201915060208501945060208101905061145e565b868310156114a0578489015161149c601f8916826113af565b8355505b6001600288020188555050505b505050505050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f6114ec82610e90565b91506114f783610e90565b925082820390508181111561150f5761150e6114b5565b5b92915050565b7f496e646578206f7574206f6620626f756e6473000000000000000000000000005f82015250565b5f611549601383610ef8565b915061155482611515565b602082019050919050565b5f6020820190508181035f8301526115768161153d565b9050919050565b7f4163636f756e7420616c72656164792064656163746976617465642e000000005f82015250565b5f6115b1601c83610ef8565b91506115bc8261157d565b602082019050919050565b5f6020820190508181035f8301526115de816115a5565b9050919050565b7f2d000000000000000000000000000000000000000000000000000000000000005f82015250565b5f611619600183611107565b9150611624826115e5565b600182019050919050565b5f61163a8285611111565b91506116458261160d565b91506116518284611111565b9150819050939250505056fea2646970667358221220885c645e2ae6a8774456239f1d9fca7ce14454dfdd551ea1341ff7c2cee6101864736f6c63430008190033"


        
contract_address = "0xEb915059eD14B2f191906E764bd48F694370dbd2"
contract = web3.eth.contract(address=contract_address, abi=contract_abi)


account = web3.eth.account._parsePrivateKey('Put here close private key of your wallet addres') 
def add_data(company,platform,login,password):
	transaction = contract.functions.addAccountData(company,platform,login,password).build_transaction({
    	'nonce': web3.eth.get_transaction_count("0xe8a252041232A746551e057d9F57DA0De78acD29"),
   	 	'from': "0xe8a252041232A746551e057d9F57DA0De78acD29",
   	 	'gas': 2000000,
   	    'gasPrice': web3.to_wei('50', 'gwei')
		})

	signed_txn = web3.eth.account.sign_transaction(transaction, account)
	web3.eth.send_raw_transaction(signed_txn.rawTransaction)

# add_data('aaa','12345','dsadas','dsads')


# result = contract.functions.getAccountData(2).call()
# print(result)


   
def get_all_platforms(company):
    total_accounts = contract.functions.getTotalAccounts().call()
    
    platforms = []
    for i in range(total_accounts):
        try:
            account_data = contract.functions.getAccountData(i).call()
            if account_data[0] == company:  # Фильтрация по названию компании
                platforms.append(account_data[1])  # Сохраняем название платформы
        except ContractLogicError as e:
            if "Account is not active" in str(e):
                pass  # Пропускаем неактивные аккаунты
            else:
                raise e  # Переподнимаем другие ошибки

    return platforms


# platforms = get_all_platforms('aaa')
# print(platforms)

def get_login_and_password(company, platform_name):
    login, password = contract.functions.getLoginAndPassword(company, platform_name).call()
    return login, password

# login, password = get_login_and_password('aaa','1234')
# print("Login:", login)
# print("Password:", password)

def update_account_data(company, platform, login, password):
    transaction = contract.functions.updateAccountData(company, platform, login, password).build_transaction({
        'nonce': web3.eth.get_transaction_count(web3.eth.defaultAccount),
        'from': web3.eth.defaultAccount,
        'gas': 2000000,
        'gasPrice': web3.to_wei('100', 'gwei')
    })
    
    signed_txn = web3.eth.account.sign_transaction(transaction, account)
    web3.eth.send_raw_transaction(signed_txn.rawTransaction)

# update_account_data('aaa','1234','rus','gay')


def deactivate_account(company, platform):
    transaction = contract.functions.deactivateAccount(company, platform).build_transaction({
        'nonce': web3.eth.get_transaction_count(web3.eth.defaultAccount),
        'from': web3.eth.defaultAccount,
        'gas': 200000,
        'gasPrice': web3.to_wei('100', 'gwei')
    })

    signed_txn = web3.eth.account.sign_transaction(transaction, account)
    web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    
# deactivate_account('aaa','1234')
    
