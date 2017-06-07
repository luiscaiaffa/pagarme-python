# coding=utf-8
from action import Action
from exception import RequiredParameters


class Card(Action):

	def create(self, data):
		if not data.get('card_hash', None):
			if not data.get('card_number', None):
				raise RequiredParameters('Card create card_number not informed')
			elif not data.get('holder_name', None):
				raise RequiredParameters('Card create holder_name not informed')
			elif not data.get('card_expiration_date', None):
				raise RequiredParameters('Card create card_expiration_date not informed')
		url = self.api.get_url(['cards'])
		return super(Card, self).create(url, data)

	def find(self, id):
		url = self.api.get_url(['cards', id])
		return super(Card, self).search(url)
