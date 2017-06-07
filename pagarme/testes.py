from transaction import Transaction
from plan import Plan
from card import Card
from bank_account import BankAccount
from customer import Customer
from subscription import  Subscription
from recipient import Recipient
import pprint




########################################################
## CRIANDO UM CARTÃO
########################################################
##>CREATE
#data={'card_hash':'593942_VYXelvjvfU9e9/KyxYS6xBTGuFk1eApkoRcQLPpbRR3kBC6eY2AKoTNsUKmfVU12JDpHze/JqrNSd5uOO/fGt0KeeCRKYGj5VVZUH3rQfBP8uNUJD33ndW2wJwDZpbhoH3s4MELF5NXEutpugL3Fdz0gEVlRV78Iya8ktaR2ykQgcKP4BOMPM4v5hQP0U5wEtzF5a55yJyalmtiVQuBqFK2qT43TAG1G6c5nAZN55dZiXj4GRRy/LYQnqNPDd+p7ERXDxd6griF6Op5dQ8oFmNGEcJ5fL1crk+TyohbSUiIm7ETkOxg/XUBuRg/YcvTnGAc7CdPfKgzCLnnXI/Hejw=='}
#pprint.pprint (Card().create(data))
# card id card_cj2zaz3jj00x5d76e5i95ujrk
##>FIND
#pprint.pprint (Card().find('card_cj2zaz3jj00x5d76e5i95ujrk'))
########################################################
## FIM CRIANDO UM CARTÃO
########################################################

########################################################
## CRIANDO UMA TRANSAÇÃO
########################################################
##>CREATE
#address = {'street':'Rua teste','street_number': '101','neighborhood': 'teste','zipcode':'25845000',}
#phone = {'ddd':'24','number':'999887766'}
#customer = {'document_number':'18152564000105','name':'cliente teste','email':'teste@teste.com','address':address,'phone':phone,}
#data={'card_id':'card_cj2zaz3jj00x5d76e5i95ujrk', 'amount':500, 'customer':customer}
#pprint.pprint (Transaction().create(data))
# card id card_cj2zaz3jj00x5d76e5i95ujrk
##>FIND
#pprint.pprint (Transaction().find('card_cj2zaz3jj00x5d76e5i95ujrk'))
##>LIST
#pprint.pprint (Transaction().list())
##>CREATE KEY
#pprint.pprint (Transaction().create_key(data={'encryption_key':'ek_test_4RgXvsOVpEbwO6B8DY2vR7BJQysDqd'})) 
##>SPLIT RULES
#pprint.pprint (Transaction().split_rule(1551548)) 
##> SPLIT RULES FIND
#pprint.pprint (Transaction().find_split_rule(1551548, 123123))
##>PAYABLE 
#pprint.pprint (Transaction().payable(1579819))
##>FIND PAYABLE 
#pprint.pprint (Transaction().find_payable(1579819, 1585357)) 
########################################################
## FIM CRIANDO UMA TRANSAÇÃO
########################################################

########################################################
## CRIANDO UM PLANO
########################################################
##>CREATE
#data={'amount':'450','days':'30','name':'Plano 1'}
#pprint.pprint (Plan().create(data))
##>FIND
#pprint.pprint (Plan().find('162681'))
##>LIST
##pprint.pprint (Plan().list())
##>CHANGE
#pprint.pprint (Plan().change('162681', data={'name':'plano teste 1'}))
########################################################
## FIM CRIANDO UM PLANO
########################################################


########################################################
## CRIANDO UMA ASSINATURA
########################################################
##>CREATE
#address = {'street':'Rua teste','street_number': '101','neighborhood': 'teste','zipcode':'25845000',}
#phone = {'ddd':'24','number':'999887766'}
#customer = {'document_number':'18152564000105','name':'cliente teste','email':'teste@teste.com','address':address,'phone':phone,}
#data={'plan_id':'162681','card_id':'card_cj2zaz3jj00x5d76e5i95ujrk','name':'Plano 1','customer':customer}
#pprint.pprint (Subscription().create(data))
##>FIND
#pprint.pprint (Plan().find('162681'))
##>LIST
##pprint.pprint (Plan().list())
##>CHANGE
#pprint.pprint (Plan().change('162681', data={'name':'plano teste 1'}))
########################################################
## FIM CRIANDO UMA ASSINATURA
########################################################


###
# Transaction 1551520,
###
#pprint.pprint (Transaction().split_rule(1551520))

###
# Card
###
# create pprint.pprint (Card().create(data={'card_hash':'580404_I1BCMNhpekqfLbsbjQSSviDNYexbKPgp9S6Dc+/jL32jsrilaxJJ8GA8hvaRpAgkgaB8ogM6llxQktNRxwVwcJPxS7vZQJbKNoByOMvUe9he2HUmWdIid2vrMP3Hr1ap+xFTEvdetKLlC/6+dnlCZrha7Fodo6WrwH98A5s0ahOPfUslRZkUprGwwdTvSmVXOl642jVnhvNsYrsuEphuERo4Ut1ZSz86md/O8xCSlEcNyo8Wg7JVzo/A0cniR3RMUA9ggZ3NDkJz8psOytlWjsSr1PFY7tf2ijnSldN0CxMJMcvL5zeretwqO+rUWCN1tW+ZKnnxYrZ1qH2/L9maUg=='}))
# find pprint.pprint (Card().find('card_cj2zaz3jj00x5d76e5i95ujrk'))

###
# Plan
###
# create pprint.pprint(Plan().create(data={'amount':'500','days':'30','name':'Plano Teste'}))
# find pprint.pprint (Plan().find('160811'))
# list pprint.pprint (Plan().list())
# change pprint.pprint (Plan().change(160811, data={'name':'plano felipe'}))
# 162669
###
# Bank_account
###
# create
'''
data = {
	'bank_code':'341',
	'agencia':'0932',
	'conta':'58054',
	'conta_dv':'1',
	'document_number':'35146484252',
	'legal_name':'Luis',
}
pprint.pprint(BankAccount().create(data))
'''
# find pprint.pprint (BankAccount().find('17482546'))
# list pprint.pprint (BankAccount().list())
'''
###
# Customer
###

address = {
	'street':'Rua teste',
	'street_number': '101',
	'neighborhood': 'teste',
	'zipcode':'25845000',
}

phone = {
	'ddd':'24',
	'number':'999887766',
}

data = {
	'document_number':'18152564000105',
	'name':'cliente teste',
	'email':'teste@teste.com',
	'address':address,
	'phone':phone,
}
pprint.pprint(Customer().create(data))
'''
# find pprint.pprint (Customer().find('191762'))
# list pprint.pprint (Customer().list())

###
# Subscription
###
'''
customer = {
	'email':'lfa.luisfelipe@gmail.com',
}

data = {
	'plan_id':'162669',
	'customer':customer,
}
pprint.pprint(Subscription().create_ticket(data))
'''