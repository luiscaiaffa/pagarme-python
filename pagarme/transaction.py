# coding=utf-8
from action import Action
from exception import RequiredParameters


class Transaction(Action):

	def create(self, data):
		if not data.get('amount', None):
			raise RequiredParameters('Transaction create amount not informed')
		
		if data.get('card_id', None):
			if not data.get('customer', None):
				raise RequiredParameters('Transaction create customer not informed')
			elif not data['customer'].get('document_number', None):
				raise RequiredParameters('Transaction create document_number not informed')
			elif not data['customer'].get('name', None):
				raise RequiredParameters('Transaction create name not informed')
			elif not data['customer'].get('email', None):
				raise RequiredParameters('Transaction create email not informed')
			elif not data['customer'].get('address', None):
				raise RequiredParameters('Transaction create address not informed')
			elif not data['customer']['address'].get('zipcode', None):
				raise RequiredParameters('Transaction create zipcode not informed')
			elif not data['customer']['address'].get('street', None):
				raise RequiredParameters('Transaction create street not informed')
			elif not data['customer']['address'].get('street_number', None):
				raise RequiredParameters('Transaction create street_number not informed')
			elif not data['customer']['address'].get('neighborhood', None):
				raise RequiredParameters('Transaction create neighborhood not informed')
			elif not data['customer'].get('phone', None):
				raise RequiredParameters('Transaction create phone not informed')
			elif not data['customer']['phone'].get('ddd', None):
				raise RequiredParameters('Transaction create ddd not informed')
			elif not data['customer']['phone'].get('number', None):
				raise RequiredParameters('Transaction create number not informed')
		else:
			if not data.get('payment_method', None) or data.get('card_hash', None):
				raise RequiredParameters('Transaction create payment_method or card_hash not informed')
		url = self.api.get_url(['transactions'])
		return super(Transaction, self).create(url, data)

	def find(self, id):
		url = self.api.get_url(['transactions', id])
		return super(Transaction, self).search(url)

	def list(self, data={}):
		url = self.api.get_url(['transactions'])
		return super(Transaction, self).list(url, data)

	def create_key(self, data):
		if not data.get('encryption_key', None):
			raise RequiredParameters('Transaction create_key encryption_key not informed')
		url = self.api.get_url(['transactions', 'card_hash_key'])
		return super(Transaction, self).list(url, data)

	def split_rule(self, transaction_id):
		url = self.api.get_url(['transactions', transaction_id , 'split_rules'])
		return super(Transaction, self).list(url)

	def find_split_rule(self, transaction_id, id):
		url = self.api.get_url(['transactions', transaction_id , 'split_rules', id])
		return super(Transaction, self).list(url)

	def payable(self, transaction_id):
		url = self.api.get_url(['transactions', transaction_id , 'payables'])
		return super(Transaction, self).list(url)

	def find_payable(self, transaction_id, id):
		url = self.api.get_url(['transactions', transaction_id , 'payables', id])
		return super(Transaction, self).list(url)

	def antifraud_analyse(self, transaction_id):
		url = self.api.get_url(['transactions', transaction_id , 'antifraud_analyses'])
		return super(Transaction, self).list(url)

	def find_antifraud_analyse(self, transaction_id, id):
		url = self.api.get_url(['transactions', transaction_id , 'antifraud_analyses', id])
		return super(Transaction, self).list(url)

	def postback(self, transaction_id):
		url = self.api.get_url(['transactions', transaction_id , 'postbacks'])
		return super(Transaction, self).list(url)

	def find_postback(self, transaction_id, id):
		url = self.api.get_url(['transactions', transaction_id , 'postbacks', id])
		return super(Transaction, self).list(url)

	def redeliver_postback(self, transaction_id, id):
		url = self.api.get_url(['transactions', transaction_id , 'postbacks', id, 'redeliver'])
		return super(Transaction, self).list(url)

	def event(self, transaction_id):
		url = self.api.get_url(['transactions', transaction_id , 'events'])
		return super(Transaction, self).list(url)

	def operation(self, transaction_id):
		url = self.api.get_url(['transactions', transaction_id , 'operations'])
		return super(Transaction, self).list(url)

	def collect_payment(self, transaction_id, data):
		if not transaction_id:
			raise RequiredParameters('Transaction collect_payment transaction_id not informed')
		elif not data.get('email', None):
			raise RequiredParameters('Transaction collect_payment email not informed')
		url = self.api.get_url(['transactions', transaction_id, 'collect_payment'])
		return super(Transaction, self).create(url, data)

	def capture(self, id):
		url = self.api.get_url(['transactions', id , 'capture'])
		return super(Transaction, self).list(url)

	def refund(self, id):
		url = self.api.get_url(['transactions', id , 'refund'])
		return super(Transaction, self).refund_post(url)

	def partial_refund(self, id):
		if not data.get('amount', None):
			raise RequiredParameters('Transaction partial_refund amount not informed')
		url = self.api.get_url(['transactions', id , 'refund'])
		return super(Transaction, self).refund_post(url)

	def calculate_installments_amount(self, data):
		if not data.get('email', None):
			raise RequiredParameters('Transaction calculate_installments_amount interest_rate not informed')
		elif not data.get('amount', None):
			raise RequiredParameters('Transaction calculate_installments_amount amount not informed')
		url = self.api.get_url(['transactions', 'calculate_installments_amount'])
		return super(Transaction, self).create(url, data)

	def test_ticket(self, id, data):
		if not data.get('status', None):
			raise RequiredParameters('Transaction test_ticket status not informed')
		url = self.api.get_url(['transactions', id])
		return super(Transaction, self).create(url, data)
