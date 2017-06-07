# coding=utf-8
from action import Action
from exception import RequiredParameters


class Transfer(Action):

	def create(self, data):
		if not data.get('amount', None):
			raise RequiredParameters('Transfer create amount not informed')
		elif not data.get('bank_account_id', None) and not data.get('recipient_id', None):
			raise RequiredParameters('Transfer create bank_account_id or recipient_id not informed')
		url = self.api.get_url(['transfers'])
		return super(Transfer, self).create(url, data)

	def find(self, id):
		url = self.api.get_url(['transfers', id])
		return super(Transfer, self).search(url)

	def list(self, data={}):
		url = self.api.get_url(['transfers'])
		return super(Transfer, self).list(url, data)

	def cancel(self, id, data={}):
		url = self.api.get_url(['transfers', id, 'cancel'])
		return super(Transfer, self).refund_post(url, data)