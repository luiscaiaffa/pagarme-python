# coding=utf-8
from action import Action
from exception import RequiredParameters


class Recipient(Action):

	def create(self, data):
		if not data.get('transfer_interval', None):
			raise RequiredParameters('Recipient create transfer_interval not informed')
		elif not data.get('transfer_day', None):
			raise RequiredParameters('Recipient create transfer_day not informed')
		elif not data.get('transfer_enabled', None):
			raise RequiredParameters('Recipient create transfer_enabled not informed')
		elif not data.get('bank_account_id', None):
			raise RequiredParameters('Recipient create bank_account_id not informed')
		url = self.api.get_url(['recipients'])
		return super(Recipient, self).create(url, data)

	def find(self, id):
		url = self.api.get_url(['recipients', id])
		return super(Recipient, self).search(url)

	def list(self, data={}):
		url = self.api.get_url(['recipients'])
		return super(Recipient, self).list(url, data)

	def change(self, id, data={}):
		if not data.get('transfer_interval', None):
			raise RequiredParameters('Recipient create transfer_interval not informed')
		elif not data.get('transfer_day', None):
			raise RequiredParameters('Recipient create transfer_day not informed')
		elif not data.get('transfer_enabled', None):
			raise RequiredParameters('Recipient create transfer_enabled not informed')
		elif not data.get('bank_account_id', None):
			raise RequiredParameters('Recipient create bank_account_id not informed')
		url = self.api.get_url(['recipients', id])
		return super(Recipient, self).change(url, data)

	def balance_find(self, recipient_id, id):
		url = self.api.get_url(['recipients', recipient_id, 'balance', 'operations', id])
		return super(Recipient, self).search(url)
	
	def balance_list(self, recipient_id, data={}):
		url = self.api.get_url(['recipients', recipient_id, 'balance', 'operations'])
		return super(Recipient, self).list(url, data)
