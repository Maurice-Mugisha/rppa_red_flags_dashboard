import psycopg2



def get_fiscal_years(selection_obj, query_executor):
	fiscal_year_dictionary = {}
	cursor = query_executor.cursor(cursor_factory = psycopg2.extras.DictCursor)
	cursor.execute(selection_obj.select_fiscal_year())
	result_dictionary = cursor.fetchall()
	for row in result_dictionary:
		fiscal_year = row['fiscal_year']
		if len(str(fiscal_year)) > 0:
			fiscal_year_dictionary[fiscal_year] = fiscal_year
	return fiscal_year_dictionary


def get_plans(selection_obj, query_executor):

	plan_dictionary = {}
	cursor = query_executor.cursor(cursor_factory = psycopg2.extras.DictCursor)
	cursor.execute(selection_obj.select_from_planning())
	result_dictionary = cursor.fetchall()
	for row in result_dictionary:
		plan_id = row['id']
		plan_dictionary[plan_id] = get_specific_plan(selection_obj, query_executor, plan_id)
	return plan_dictionary


def specific_fiscal_year_plans(selection_obj, query_executor, fiscal_year_id):
	plan_dictionary = {}
	cursor = query_executor.cursor(cursor_factory = psycopg2.extras.DictCursor)
	cursor.execute(selection_obj.select_fiscal_year_planning(fiscal_year_id))
	result_dictionary = cursor.fetchall()
	for row in result_dictionary:
		plan_id = row['id']
		plan_dictionary[plan_id] = row
	return plan_dictionary


def specific_party_fiscal_year_plans(selection_obj, query_executor, fiscal_year_id, party_id):
	plan_dictionary = {}
	cursor = query_executor.cursor(cursor_factory = psycopg2.extras.DictCursor)
	cursor.execute(selection_obj.select_party_fiscal_year_planning(fiscal_year_id, party_id))
	result_dictionary = cursor.fetchall()
	for row in result_dictionary:
		plan_id = row['id']
		plan_dictionary[plan_id] = row
	return plan_dictionary


def get_specific_plan(selection_obj, query_executor, plan_id):

	planning_dictionary = {}

	cursor = query_executor.cursor(cursor_factory = psycopg2.extras.DictCursor)
	cursor.execute(selection_obj.select_planning(plan_id))
	result_dictionary = cursor.fetchall()

	for row in result_dictionary:
		plan_id = row['id']
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
		planning_dictionary[plan_id] = plan_dictionary

	return plan_dictionary


def procurement_actor(selection_obj, query_executor, party):

	procurement_actor_dictionary = {}
	cursor = query_executor.cursor(cursor_factory = psycopg2.extras.DictCursor)
	cursor.execute(selection_obj.select_party(party))
	result_dictionary = cursor.fetchall()

	for row in result_dictionary:
		party_id = row['id']
		actor_dictionary = {}
		actor_dictionary['id'] = party_id
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
		procurement_actor_dictionary[party_id] = actor_dictionary

	return procurement_actor_dictionary
