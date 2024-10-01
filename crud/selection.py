

class Select:

	def  __init__(self, instance_name):
		self.instance_name = instance_name

	def  __str__(self):
		return self.instance_name

	def select_fiscal_year(self):
		query = "SELECT DISTINCT(ext_fiscal_year) AS fiscal_year FROM planning ORDER BY ext_fiscal_year DESC;"
		return query

	def select_fiscal_year_plan_id(self, fiscal_year_id):
		query = "SELECT id FROM planning WHERE ext_fiscal_year = '" + fiscal_year_id + "';"
		return query

	def select_from_party(self):
		query = "SELECT * FROM party;"
		return query

	def select_party(self, party_id):
		query = "SELECT * FROM party WHERE roles = '" + party_id + "';"
		return query

	def select_from_planning(self):
		query = "SELECT * FROM planning;"
		return query

	def select_planning(self, plan_id):
		query = "SELECT * FROM planning WHERE id = '" + plan_id + "';"
		return query

	def select_fiscal_year_planning(self, fiscal_year_id):
		query = "SELECT * FROM planning WHERE ext_fiscal_year = '" + fiscal_year_id + "';"
		return query

	def select_party_fiscal_year_planning(self, fiscal_year_id, party_id):
		query = "SELECT * FROM planning WHERE ext_fiscal_year = '" + fiscal_year_id + "' AND ext_pe_code = '" + party_id + "';"
		return query

	def select_from_tender(self):
		query = "SELECT * FROM tender;"
		return query

	def select_tender(self, tender_id):
		query = "SELECT * FROM tender WHERE id = '" + tender_id + "';"
		return query

	def select_from_bidder(self):
		query = "SELECT * FROM bidder;"
		return query

	def select_bidder(self, bidder_id):
		query = "SELECT * FROM bidder WHERE id = '" + bidder_id + "';"
		return query

	def select_from_award(self):
		query = "SELECT * FROM award;"
		return query

	def select_award(self, award_id):
		query = "SELECT * FROM award WHERE id = '" + award_id + "';"
		return query

	def select_from_contract(self):
		query = "SELECT * FROM contract;"
		return query

	def select_award(self, contract_id):
		query = "SELECT * FROM contract WHERE id = '" + contract_id + "';"
		return query
