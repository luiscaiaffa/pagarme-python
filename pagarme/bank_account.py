# coding=utf-8
from action import Action
from exception import RequiredParameters


class BankAccount(Action):

	def create(self, data):
		if not data.get('bank_code', None):
			raise RequiredParameters('Bank Account create bank_code not informed')
		elif not data.get('agencia', None) :
			raise RequiredParameters('Bank Account create agencia not informed')
		elif not data.get('conta', None) :
			raise RequiredParameters('Bank Account create conta not informed')
		elif not data.get('conta_dv', None) :
			raise RequiredParameters('Bank Account create conta_dv not informed')
		elif not data.get('document_number', None) :
			raise RequiredParameters('Bank Account create document_number not informed')
		elif not data.get('legal_name', None) :
			raise RequiredParameters('Bank Account create legal_name not informed')
		url = self.api.get_url(['bank_accounts'])
		return super(BankAccount, self).create(url, data)

	def find(self, id):
		url = self.api.get_url(['bank_accounts', id])
		return super(BankAccount, self).search(url)

	def list(self, data={}):
		url = self.api.get_url(['bank_accounts'])
		return super(BankAccount, self).list(url, data)