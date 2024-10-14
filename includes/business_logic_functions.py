import psycopg2



def get_fiscal_years(selection_object, query_executor):
	fiscal_year_dictionary = {}
	cursor = query_executor.cursor(cursor_factory = psycopg2.extras.DictCursor)
	cursor.execute(selection_object.select_fiscal_year())
	result_dictionary = cursor.fetchall()
	for row in result_dictionary:
		fiscal_year = row['fiscal_year']
		fiscal_year_dictionary[fiscal_year] = {}
		if len(str(fiscal_year)) > 0:
			fiscal_year_dictionary[fiscal_year]['id'] = fiscal_year
			fiscal_year_dictionary[fiscal_year]['start_date'] =  fiscal_year[:4] + "-07-01"
			fiscal_year_dictionary[fiscal_year]['end_date'] = fiscal_year[-4:] + "-06-30"

	return fiscal_year_dictionary


def get_plans(selection_object, query_executor):

	plan_dictionary = {}
	cursor = query_executor.cursor(cursor_factory = psycopg2.extras.DictCursor)
	cursor.execute(selection_object.select_from_planning())
	result_dictionary = cursor.fetchall()
	for row in result_dictionary:
		plan_id = row['id']
		plan_dictionary[plan_id] = get_specific_plan(selection_object, query_executor, plan_id)
	return plan_dictionary


def get_specific_fiscal_year_plans(selection_object, query_executor, fiscal_year_id):
	plan_dictionary = {}
	cursor = query_executor.cursor(cursor_factory = psycopg2.extras.DictCursor)
	cursor.execute(selection_object.select_fiscal_year_planning(fiscal_year_id))
	result_dictionary = cursor.fetchall()
	for row in result_dictionary:
		plan_id = row['id']
		plan_dictionary[plan_id] = row
	return plan_dictionary


def get_specific_party_fiscal_year_plans(selection_object, query_executor, fiscal_year_id, party_id):
	planning_dictionary = {}
	cursor = query_executor.cursor(cursor_factory = psycopg2.extras.DictCursor)
	cursor.execute(selection_object.select_party_fiscal_year_planning(fiscal_year_id, party_id))
	result_dictionary = cursor.fetchall()
	for row in result_dictionary:
		plan_id = row['id']
		plan_dictionary = get_plan_dictionary(row)
		# RPPA specific
		plan_dictionary['submission_date_and_time'] = row['created_at']
		# end of RPPA specific data
		planning_dictionary[plan_id] = plan_dictionary

	return planning_dictionary


def get_specific_plan(selection_object, query_executor, plan_id):

	planning_dictionary = {}

	cursor = query_executor.cursor(cursor_factory = psycopg2.extras.DictCursor)
	cursor.execute(selection_object.select_planning(plan_id))
	result_dictionary = cursor.fetchall()

	for row in result_dictionary:
		plan_id = row['id']
		plan_dictionary = get_plan_dictionary(row)
		planning_dictionary[plan_id] = plan_dictionary

	return plan_dictionary


def get_plan_dictionary(row):
	plan_dictionary = {}
	plan_dictionary['id'] = row['id']
	plan_dictionary['language'] = row['language']
	plan_dictionary['rationale'] = row['rationale']
	plan_dictionary['budget_id'] = row['budget_id']
	plan_dictionary['budget_description'] = row['budget_description']
	plan_dictionary['budget_project'] = row['budget_project']
	plan_dictionary['budget_project_id'] = row['budget_project_id']
	plan_dictionary['budget_amount'] = row['budget_amount']
	plan_dictionary['budget_currency'] = row['budget_currency']
	plan_dictionary['budget_uri'] = row['budget_uri']
	plan_dictionary['ext_contract_period_code'] = row['ext_contract_period_code']
	plan_dictionary['ext_pe_code'] = row['ext_pe_code']
	plan_dictionary['ext_fiscal_year'] = row['ext_fiscal_year']
	plan_dictionary['ext_tender_type_code'] = row['ext_tender_type_code']
	plan_dictionary['ext_tender_method_code'] = row['ext_tender_method_code']
	plan_dictionary['ext_mod_date'] = row['ext_mod_date']
	plan_dictionary['ext_revw_serno'] = row['ext_revw_serno']
	plan_dictionary['ext_other_info_content'] = row['ext_other_info_content']
	plan_dictionary['is_test_data'] = row['is_test_data']
	plan_dictionary['legacy_id'] = row['legacy_id']
	plan_dictionary['version'] = row['version']
	plan_dictionary['hash'] = row['hash']
	plan_dictionary['created_at'] = row['created_at']
	plan_dictionary['deleted_at'] = row['deleted_at']
	plan_dictionary['updated_at'] = row['updated_at']
	plan_dictionary['status'] = row['status']
	plan_dictionary['ext_pay_pe_code'] = row['ext_pay_pe_code']
	plan_dictionary['ext_highest_amount'] = row['ext_highest_amount']
	plan_dictionary['ext_highest_donor'] = row['ext_highest_donor']
	plan_dictionary['ext_highest_bgt_line'] = row['ext_highest_bgt_line']

	return plan_dictionary



def get_procurement_actor(selection_object, query_executor, party):

	procurement_actor_dictionary = {}
	cursor = query_executor.cursor(cursor_factory = psycopg2.extras.DictCursor)
	cursor.execute(selection_object.select_party(party))
	result_dictionary = cursor.fetchall()

	for row in result_dictionary:
		party_id = row['id']
		actor_dictionary = get_procurement_actor_dictionary(row)
		procurement_actor_dictionary[party_id] = actor_dictionary

	return procurement_actor_dictionary



def get_fiscal_year_supplying_entity(selection_object, query_executor, party, fiscal_year_id):

	procurement_actor_dictionary = {}
	cursor = query_executor.cursor(cursor_factory = psycopg2.extras.DictCursor)
	cursor.execute(selection_object.select_fiscal_year_supplying_entity(party, fiscal_year_id))
	result_dictionary = cursor.fetchall()

	for row in result_dictionary:
		party_id = row['id']
		actor_dictionary = get_procurement_actor_dictionary(row)
		procurement_actor_dictionary[party_id] = actor_dictionary

	return procurement_actor_dictionary



def get_procurement_actor_dictionary(row):

	actor_dictionary = {}
	actor_dictionary['id'] = row['id']
	actor_dictionary['name'] = row['name']
	actor_dictionary['roles'] = row['roles']
	actor_dictionary['identifier_scheme'] = row['identifier_scheme']
	actor_dictionary['identifier_id'] = row['identifier_id']
	actor_dictionary['identifier_legal_name'] = row['identifier_legal_name']
	actor_dictionary['address_street'] = row['address_street']
	actor_dictionary['address_locality'] = row['address_locality']
	actor_dictionary['address_region'] = row['address_region']
	actor_dictionary['address_postal_code'] = row['address_postal_code']
	actor_dictionary['address_country_name'] = row['address_country_name']
	actor_dictionary['contact_point_name'] = row['contact_point_name']
	actor_dictionary['contact_point_email'] = row['contact_point_email']
	actor_dictionary['contact_point_telephone'] = row['contact_point_telephone']
	actor_dictionary['contact_point_fax_number'] = row['contact_point_fax_number']
	actor_dictionary['contact_point_url'] = row['contact_point_url']
	actor_dictionary['contact_person_nat_id'] = row['contact_person_nat_id']
	actor_dictionary['contact_person_nationality'] = row['contact_person_nationality']
	actor_dictionary['ext_bank_name'] = row['ext_bank_name']
	actor_dictionary['ext_bank_code'] = row['ext_bank_code']
	actor_dictionary['ext_tin'] = row['ext_tin']
	actor_dictionary['ext_mod_date'] = row['ext_mod_date']
	actor_dictionary['legacy_id'] = row['legacy_id']
	actor_dictionary['version'] = row['version']
	actor_dictionary['hash'] = row['hash']
	actor_dictionary['created_at'] = row['created_at']
	actor_dictionary['deleted_at'] = row['deleted_at']
	actor_dictionary['updated_at'] = row['updated_at']
	actor_dictionary['status'] = row['status']

	return actor_dictionary



def get_specific_fiscal_year_tenders(selection_object, query_executor, fiscal_year_id):
	fiscal_year_tender_dictionary = {}
	cursor = query_executor.cursor(cursor_factory = psycopg2.extras.DictCursor)
	cursor.execute(selection_object.select_fiscal_year_tender(fiscal_year_id))
	result_dictionary = cursor.fetchall()
	for row in result_dictionary:
		tender_id = row['id']
		fiscal_year_tender_dictionary[tender_id] = get_tender_dictionary(row)
	return fiscal_year_tender_dictionary


def get_tender_dictionary(row):
	tender_dictionary = {}
	tender_dictionary['id'] = row['id']
	tender_dictionary['language'] = row['language']
	tender_dictionary['title'] = row['title']
	tender_dictionary['description'] = row['description']
	tender_dictionary['main_procurement_category'] = row['main_procurement_category']
	tender_dictionary['tender_status'] = row['tender_status']
	tender_dictionary['min_value_amount'] = row['min_value_amount']
	tender_dictionary['min_value_currency'] = row['min_value_currency']
	tender_dictionary['value_amount'] = row['value_amount']
	tender_dictionary['value_currency'] = row['value_currency']
	tender_dictionary['procurement_method'] = row['procurement_method']
	tender_dictionary['procurement_method_details'] = row['procurement_method_details']
	tender_dictionary['procurement_method_rationale'] = row['procurement_method_rationale']
	tender_dictionary['award_criteria'] = row['award_criteria']
	tender_dictionary['award_criteria_details'] = row['award_criteria_details']
	tender_dictionary['submission_method'] = row['submission_method']
	tender_dictionary['has_enquiries'] = row['has_enquiries']
	tender_dictionary['tender_period_start_date'] = row['tender_period_start_date']
	tender_dictionary['tender_period_end_date'] = row['tender_period_end_date']
	tender_dictionary['tender_period_duration_in_days'] = row['tender_period_duration_in_days']
	tender_dictionary['enquiry_period_start_date'] = row['enquiry_period_start_date']
	tender_dictionary['enquiry_period_end_date'] = row['enquiry_period_end_date']
	tender_dictionary['enquiry_period_duration_in_days'] = row['enquiry_period_duration_in_days']
	tender_dictionary['participation_fees_id'] = row['participation_fees_id']
	tender_dictionary['participation_fees_value_amount'] = row['participation_fees_value_amount']
	tender_dictionary['participation_fees_value_currency'] = row['participation_fees_value_currency']
	tender_dictionary['ext_tender_fee_amount'] = row['ext_tender_fee_amount']
	tender_dictionary['ext_total_tender_security_amount'] = row['ext_total_tender_security_amount']
	tender_dictionary['ext_simpld_yn'] = row['ext_simpld_yn']
	tender_dictionary['ext_jv_yn'] = row['ext_jv_yn']
	tender_dictionary['ext_consult_selt_mthod'] = row['ext_consult_selt_mthod']
	tender_dictionary['ext_tender_estimated_value'] = row['ext_tender_estimated_value']
	tender_dictionary['ext_tender_estimated_currency'] = row['ext_tender_estimated_currency']
	tender_dictionary['ext_planning_reference_number'] = row['ext_planning_reference_number']
	tender_dictionary['ext_pe_code'] = row['ext_pe_code']
	tender_dictionary['ext_fiscal_year'] = row['ext_fiscal_year']
	tender_dictionary['ext_tender_type_code'] = row['ext_tender_type_code']
	tender_dictionary['ext_tender_method_code'] = row['ext_tender_method_code']
	tender_dictionary['ext_mod_date'] = row['ext_mod_date']
	tender_dictionary['ext_rgt_type_code'] = row['ext_rgt_type_code']
	tender_dictionary['ext_tender_stage_code'] = row['ext_tender_stage_code']
	tender_dictionary['legacy_id'] = row['legacy_id']
	tender_dictionary['is_test_data'] = row['is_test_data']
	tender_dictionary['version'] = row['version']
	tender_dictionary['hash'] = row['hash']
	tender_dictionary['created_at'] = row['created_at']
	tender_dictionary['deleted_at'] = row['deleted_at']
	tender_dictionary['updated_at'] = row['updated_at']
	tender_dictionary['status'] = row['status']

	return tender_dictionary



def get_tender_bidders(selection_object, query_executor, tender_id):
	bidder_dictionary = {}
	cursor = query_executor.cursor(cursor_factory = psycopg2.extras.DictCursor)
	cursor.execute(selection_object.select_tender_bidder(tender_id))
	result_dictionary = cursor.fetchall()
	for row in result_dictionary:
		bidder_id = row['id']
		bidder_dictionary[bidder_id] = row
	return bidder_dictionary


def get_specific_fiscal_year_bidder(selection_object, query_executor, fiscal_year_id):
	fiscal_year_bidder_dictionary = {}
	cursor = query_executor.cursor(cursor_factory = psycopg2.extras.DictCursor)
	cursor.execute(selection_object.select_fiscal_year_bids(fiscal_year_id))
	result_dictionary = cursor.fetchall()
	for row in result_dictionary:
		bidder_id = row['id']
		fiscal_year_bidder_dictionary[bidder_id] = row
	return fiscal_year_bidder_dictionary


def get_specific_fiscal_year_supplying_entity_bids(selection_object, query_executor, fiscal_year_id, bidder_id):
	fiscal_year_bidder_dictionary = {}
	cursor = query_executor.cursor(cursor_factory = psycopg2.extras.DictCursor)
	cursor.execute(selection_object.select_fiscal_year_bidder(fiscal_year_id, bidder_id))
	result_dictionary = cursor.fetchall()
	for row in result_dictionary:
		bidder_id = row['id']
		fiscal_year_bidder_dictionary[bidder_id] = row
	return fiscal_year_bidder_dictionary


def get_specific_fiscal_year_awards(selection_object, query_executor, fiscal_year_id):
	award_dictionary = {}
	cursor = query_executor.cursor(cursor_factory = psycopg2.extras.DictCursor)
	cursor.execute(selection_object.select_fiscal_year_award(fiscal_year_id))
	result_dictionary = cursor.fetchall()
	for row in result_dictionary:
		bidder_id = row['id']
		award_dictionary[bidder_id] = row
	return award_dictionary


def get_specific_supplying_entity_awards(selection_object, query_executor, supplying_entity_id):
	award_dictionary = {}
	cursor = query_executor.cursor(cursor_factory = psycopg2.extras.DictCursor)
	cursor.execute(selection_object.select_supplying_entity_award(supplying_entity_id))
	result_dictionary = cursor.fetchall()
	for row in result_dictionary:
		award_id = row['id']
		award_dictionary[award_id] = row
	return award_dictionary


def get_fiscal_year_supplying_entity_awards(selection_object, query_executor, fiscal_year_id, supplying_entity_id):
	award_dictionary = {}
	cursor = query_executor.cursor(cursor_factory = psycopg2.extras.DictCursor)
	cursor.execute(selection_object.select_fiscal_year_supplying_entity_award(fiscal_year_id, supplying_entity_id))
	result_dictionary = cursor.fetchall()
	for row in result_dictionary:
		award_id = row['id']
		award_dictionary[award_id] = row
	return award_dictionary


def get_fiscal_year_procuring_entity_awards(selection_object, query_executor, fiscal_year_id, procuring_entity_id):
	award_dictionary = {}
	cursor = query_executor.cursor(cursor_factory = psycopg2.extras.DictCursor)
	cursor.execute(selection_object.select_fiscal_year_procuring_entity_award(fiscal_year_id, procuring_entity_id))
	result_dictionary = cursor.fetchall()
	for row in result_dictionary:
		award_id = row['id']
		award_dictionary[award_id] = get_award_dictionary(row)
	return award_dictionary


def get_award_dictionary(row):
	award_dictionary = {}
	award_dictionary['id'] = row['id']
	award_dictionary['language'] = row['language']
	award_dictionary['title'] = row['title']
	award_dictionary['description'] = row['description']
	award_dictionary['award_status'] = row['award_status']
	award_dictionary['date'] = row['date']
	award_dictionary['value_amount'] = row['value_amount']
	award_dictionary['value_currency'] = row['value_currency']
	award_dictionary['ext_lot_number'] = row['ext_lot_number']
	award_dictionary['ext_tin'] = row['ext_tin']
	award_dictionary['ext_planning_reference_number'] = row['ext_planning_reference_number']
	award_dictionary['ext_pe_code'] = row['ext_pe_code']
	award_dictionary['ext_tender_reference_number'] = row['ext_tender_reference_number']
	award_dictionary['ext_fiscal_year'] = row['ext_fiscal_year']
	award_dictionary['ext_tender_type_code'] = row['ext_tender_type_code']
	award_dictionary['ext_tender_method_code'] = row['ext_tender_method_code']
	award_dictionary['ext_mod_date'] = row['ext_mod_date']
	award_dictionary['legacy_id'] = row['legacy_id']
	award_dictionary['is_test_data'] = row['is_test_data']
	award_dictionary['version'] = row['version']
	award_dictionary['hash'] = row['hash']
	award_dictionary['created_at'] = row['created_at']
	award_dictionary['deleted_at'] = row['deleted_at']
	award_dictionary['updated_at'] = row['updated_at']
	award_dictionary['status'] = row['status']

	return award_dictionary


def get_specific_award_supplying_entities(selection_object, query_executor, award_id):
		supplying_entity_dictionary = {}
		cursor = query_executor.cursor(cursor_factory = psycopg2.extras.DictCursor)
		cursor.execute(selection_object.select_award_supplying_entity(award_id))
		result_dictionary = cursor.fetchall()
		for row in result_dictionary:
			supplying_entity_id = row['ext_tin']
			supplying_entity_dictionary[supplying_entity_id] = get_procurement_actor_dictionary(row)
		return supplying_entity_dictionary


def get_specific_tender_awards(selection_object, query_executor, tender_id):
	award_dictionary = {}
	cursor = query_executor.cursor(cursor_factory = psycopg2.extras.DictCursor)
	cursor.execute(selection_object.select_tender_award(tender_id))
	result_dictionary = cursor.fetchall()
	for row in result_dictionary:
		award_id = row['id']
		award_dictionary[award_id] = row
	return award_dictionary


def get_specific_award_tenders(selection_object, query_executor, award_id):
	tender_dictionary = {}
	cursor = query_executor.cursor(cursor_factory = psycopg2.extras.DictCursor)
	cursor.execute(selection_object.select_award_tender(award_id))
	result_dictionary = cursor.fetchall()
	for row in result_dictionary:
		tender_id = row['id']
		tender_dictionary[tender_id] = row
	return tender_dictionary
