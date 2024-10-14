

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

	def select_fiscal_year_supplying_entity(self, party, fiscal_year_id):
		query = "SELECT party.* FROM party, bidder, tender WHERE party.roles = '" + party + "' AND bidder.ext_tin = party.ext_tin AND bidder.ext_tender_reference_number = tender.legacy_id AND tender.ext_fiscal_year = '" + fiscal_year_id + "';"
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
		query = "SELECT * FROM planning WHERE ext_fiscal_year = '" + fiscal_year_id + "' AND ext_pe_code = '" + party_id + "' LIMIT 1;"
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

	def select_fiscal_year_bids(self, fiscal_year_id):
		query = "select bidder.* from bidder, tender where tender.ext_fiscal_year = '" + fiscal_year_id + "' AND bidder.ext_tender_reference_number = tender.legacy_id;"
		return query

	def select_fiscal_year_bidder(self, fiscal_year_id, bidder_id):
		query = "select bidder.*, tender.ext_fiscal_year as ext_fiscal_year from bidder RIGHT JOIN tender ON tender.legacy_id = bidder.ext_tender_reference_number where tender.ext_fiscal_year = '" + fiscal_year_id + "' AND ext_tin = '" + bidder_id + "';"
		return query

	def select_from_award(self):
		query = "SELECT * FROM award;"
		return query

	def select_award(self, award_id):
		query = "SELECT * FROM award WHERE id = '" + award_id + "';"
		return query

	def select_fiscal_year_award(self, fiscal_year_id):
		query = "SELECT * FROM award WHERE ext_fiscal_year = '" + fiscal_year_id + "';"
		return query

	def select_supplying_entity_award(self, party_id):
		query = "SELECT * FROM award WHERE ext_tin = '" + party_id + "';"
		return query

	def select_fiscal_year_supplying_entity_award(self, fiscal_year_id, party_id):
		query = "SELECT * FROM award WHERE ext_fiscal_year = '" + fiscal_year_id + "' AND ext_tin = '" + party_id + "';"
		return query

	def select_fiscal_year_procuring_entity_award(self, fiscal_year_id, party_id):
		query = "SELECT * FROM award WHERE ext_fiscal_year = '" + fiscal_year_id + "' AND ext_pe_code = '" + party_id + "';"
		return query

	def select_award_supplying_entity(self, award_id):
		query = "SELECT party.*, award.ext_pe_code, award.legacy_id AS award_id, award.ext_tender_method_code FROM party, award WHERE party.ext_tin = award.ext_tin AND award.legacy_id = '" + award_id + "';" # award_legacy_id
		return query

	def select_tender_award(self, tender_id):
		query = "SELECT * FROM award WHERE ext_tender_reference_number = '" + str(tender_id) + "';"
		return query

	def select_award_tender(self, award_id):
		query = "SELECT tender.* FROM tender, award WHERE award.ext_tender_reference_number = tender.legacy_id AND award.id = '" + award_id + "';"
		return query

	def select_from_contract(self):
		query = "SELECT * FROM contract;"
		return query

	def select_award(self, contract_id):
		query = "SELECT * FROM contract WHERE id = '" + contract_id + "';"
		return query

	def select_fiscal_year_tender(self, fiscal_year_id):
		query = "SELECT * FROM tender WHERE ext_fiscal_year = '" + fiscal_year_id + "';"
		return query

	def select_fiscal_year_procuring_entity_tender(self, fiscal_year_id, party_id):
		query = "SELECT * FROM tender WHERE ext_fiscal_year = '" + fiscal_year_id + "' AND ext_pe_code = '" + party_id + "';"
		return query

	def select_tender_bidder(self, tender_id):
		query = "SELECT * FROM bidder, tender WHERE bidder.ext_tender_reference_number = '" + tender_id + "';"
		return query
