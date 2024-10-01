
def insert_country(database_connection_object, query_executor, selection_object, insertion_object, country_id, code, name, currency, flag, coat_of_arms):

	query_executor.execute(selection_object.select_country(country_id))
	country_check_query_result = query_executor.fetchall()
	result_list_length = len(country_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_country(country_id))
		database_connection_object.commit()

	if len(str(code).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_country_code(country_id, code))
		database_connection_object.commit()


	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_country_name(country_id, name))
		database_connection_object.commit()


	if len(str(currency).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_country_currency(country_id, currency))
		database_connection_object.commit()


	if len(str(flag).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_country_flag(country_id, flag))
		database_connection_object.commit()


	if len(str(coat_of_arms).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_country_coat_of_arms(country_id, coat_of_arms))
		database_connection_object.commit()



def insert_fiscal_year(database_connection_object, query_executor, selection_object, insertion_object, fiscal_year_id, start_date, end_date):

	query_executor.execute(selection_object.select_fiscal_year(fiscal_year_id))
	fiscal_year_check_query_result = query_executor.fetchall()
	result_list_length = len(fiscal_year_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_fiscal_year(fiscal_year_id))
		database_connection_object.commit()

	if len(str(start_date).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_fiscal_year_start_date(fiscal_year_id, start_date))
		database_connection_object.commit()


	if len(str(end_date).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_fiscal_year_end_date(fiscal_year_id, end_date))
		database_connection_object.commit()



def insert_configuration(database_connection_object, query_executor, selection_object, insertion_object, configuration_id, name, description, value, status):

	query_executor.execute(selection_object.select_configuration(configuration_id))
	configuration_check_query_result = query_executor.fetchall()
	result_list_length = len(configuration_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_configuration(configuration_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_configuration_name(configuration_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_configuration_description(configuration_id, description))
		database_connection_object.commit()


	if len(str(value).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_configuration_value(configuration_id, value))
		database_connection_object.commit()


	if len(str(status).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_configuration_status(configuration_id, status))
		database_connection_object.commit()



def insert_red_flag(database_connection_object, query_executor, selection_object, insertion_object, red_flag_id, name, description, status):

	query_executor.execute(selection_object.select_red_flag(red_flag_id))
	red_flag_check_query_result = query_executor.fetchall()
	result_list_length = len(red_flag_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_red_flag(red_flag_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_red_flag_name(red_flag_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_red_flag_description(red_flag_id, description))
		database_connection_object.commit()


	if len(str(status).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_red_flag_status(red_flag_id, status))
		database_connection_object.commit()



def insert_illicit_scheme(database_connection_object, query_executor, selection_object, insertion_object, illicit_scheme_id, name, description):

	query_executor.execute(selection_object.select_illicit_scheme(illicit_scheme_id))
	illicit_scheme_check_query_result = query_executor.fetchall()
	result_list_length = len(illicit_scheme_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_illicit_scheme(illicit_scheme_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_illicit_scheme_name(illicit_scheme_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_illicit_scheme_description(illicit_scheme_id, description))
		database_connection_object.commit()



def insert_procurement_stage(database_connection_object, query_executor, selection_object, insertion_object, procurement_stage_id, name, description):

	query_executor.execute(selection_object.select_procurement_stage(procurement_stage_id))
	procurement_stage_check_query_result = query_executor.fetchall()
	result_list_length = len(procurement_stage_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_stage(procurement_stage_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_stage_name(procurement_stage_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_stage_description(procurement_stage_id, description))
		database_connection_object.commit()



def insert_submission(database_connection_object, query_executor, selection_object, insertion_object, submission_id, name, description, reception_date_and_time, cut_off_date_and_time):

	query_executor.execute(selection_object.select_submission(submission_id))
	submission_check_query_result = query_executor.fetchall()
	result_list_length = len(submission_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_submission(submission_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_submission_name(submission_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_submission_description(submission_id, description))
		database_connection_object.commit()


	if len(str(reception_date_and_time).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_submission_reception_date_and_time(submission_id, reception_date_and_time))
		database_connection_object.commit()


	if len(str(cut_off_date_and_time).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_submission_cut_off_date_and_time(submission_id, cut_off_date_and_time))
		database_connection_object.commit()



def insert_procurement_type(database_connection_object, query_executor, selection_object, insertion_object, procurement_type_id, code, name, description):

	query_executor.execute(selection_object.select_procurement_type(procurement_type_id))
	procurement_type_check_query_result = query_executor.fetchall()
	result_list_length = len(procurement_type_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_type(procurement_type_id))
		database_connection_object.commit()

	if len(str(code).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_type_code(procurement_type_id, code))
		database_connection_object.commit()


	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_type_name(procurement_type_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_type_description(procurement_type_id, description))
		database_connection_object.commit()



def insert_procurement_method(database_connection_object, query_executor, selection_object, insertion_object, procurement_method_id, code, name, description):

	query_executor.execute(selection_object.select_procurement_method(procurement_method_id))
	procurement_method_check_query_result = query_executor.fetchall()
	result_list_length = len(procurement_method_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_method(procurement_method_id))
		database_connection_object.commit()

	if len(str(code).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_method_code(procurement_method_id, code))
		database_connection_object.commit()


	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_method_name(procurement_method_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_method_description(procurement_method_id, description))
		database_connection_object.commit()



def insert_bid(database_connection_object, query_executor, selection_object, insertion_object, bid_id, submission_date, amount, extra_information):

	query_executor.execute(selection_object.select_bid(bid_id))
	bid_check_query_result = query_executor.fetchall()
	result_list_length = len(bid_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_bid(bid_id))
		database_connection_object.commit()

	if len(str(submission_date).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_bid_submission_date(bid_id, submission_date))
		database_connection_object.commit()


	if len(str(amount).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_bid_amount(bid_id, amount))
		database_connection_object.commit()


	if len(str(extra_information).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_bid_extra_information(bid_id, extra_information))
		database_connection_object.commit()



def insert_item(database_connection_object, query_executor, selection_object, insertion_object, item_id, code, name, unit_cost, description):

	query_executor.execute(selection_object.select_item(item_id))
	item_check_query_result = query_executor.fetchall()
	result_list_length = len(item_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_item(item_id))
		database_connection_object.commit()

	if len(str(code).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_item_code(item_id, code))
		database_connection_object.commit()


	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_item_name(item_id, name))
		database_connection_object.commit()


	if len(str(unit_cost).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_item_unit_cost(item_id, unit_cost))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_item_description(item_id, description))
		database_connection_object.commit()



def insert_procuring_entity(database_connection_object, query_executor, selection_object, insertion_object, procuring_entity_id, name, tax_identifier, tax_identifier_value, registration_number, registration_date, status):

	query_executor.execute(selection_object.select_procuring_entity(procuring_entity_id))
	procuring_entity_check_query_result = query_executor.fetchall()
	result_list_length = len(procuring_entity_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entity(procuring_entity_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entity_name(procuring_entity_id, name))
		database_connection_object.commit()


	if len(str(tax_identifier).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entity_tax_identifier(procuring_entity_id, tax_identifier))
		database_connection_object.commit()


	if len(str(tax_identifier_value).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entity_tax_identifier_value(procuring_entity_id, tax_identifier_value))
		database_connection_object.commit()


	if len(str(registration_number).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entity_registration_number(procuring_entity_id, registration_number))
		database_connection_object.commit()


	if len(str(registration_date).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entity_registration_date(procuring_entity_id, registration_date))
		database_connection_object.commit()


	if len(str(status).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entity_status(procuring_entity_id, status))
		database_connection_object.commit()



def insert_supplying_entity(database_connection_object, query_executor, selection_object, insertion_object, supplying_entity_id, name, tax_identifier, tax_identifier_value, registration_number, registration_date, status):

	query_executor.execute(selection_object.select_supplying_entity(supplying_entity_id))
	supplying_entity_check_query_result = query_executor.fetchall()
	result_list_length = len(supplying_entity_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entity(supplying_entity_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entity_name(supplying_entity_id, name))
		database_connection_object.commit()


	if len(str(tax_identifier).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entity_tax_identifier(supplying_entity_id, tax_identifier))
		database_connection_object.commit()


	if len(str(tax_identifier_value).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entity_tax_identifier_value(supplying_entity_id, tax_identifier_value))
		database_connection_object.commit()


	if len(str(registration_number).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entity_registration_number(supplying_entity_id, registration_number))
		database_connection_object.commit()


	if len(str(registration_date).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entity_registration_date(supplying_entity_id, registration_date))
		database_connection_object.commit()


	if len(str(status).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entity_status(supplying_entity_id, status))
		database_connection_object.commit()



def insert_address(database_connection_object, query_executor, selection_object, insertion_object, address_id, country, address_line_1, address_line_2, address_line_3, address_line_4, address_line_5, address_line_6, address_line_7, address_line_8, address_line_9, x_coord, y_coord, status, description, short_form):

	query_executor.execute(selection_object.select_address(address_id))
	address_check_query_result = query_executor.fetchall()
	result_list_length = len(address_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_address(address_id))
		database_connection_object.commit()

	if len(str(country).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_country(address_id, country))
		database_connection_object.commit()


	if len(str(address_line_1).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_address_line_1(address_id, address_line_1))
		database_connection_object.commit()


	if len(str(address_line_2).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_address_line_2(address_id, address_line_2))
		database_connection_object.commit()


	if len(str(address_line_3).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_address_line_3(address_id, address_line_3))
		database_connection_object.commit()


	if len(str(address_line_4).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_address_line_4(address_id, address_line_4))
		database_connection_object.commit()


	if len(str(address_line_5).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_address_line_5(address_id, address_line_5))
		database_connection_object.commit()


	if len(str(address_line_6).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_address_line_6(address_id, address_line_6))
		database_connection_object.commit()


	if len(str(address_line_7).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_address_line_7(address_id, address_line_7))
		database_connection_object.commit()


	if len(str(address_line_8).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_address_line_8(address_id, address_line_8))
		database_connection_object.commit()


	if len(str(address_line_9).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_address_line_9(address_id, address_line_9))
		database_connection_object.commit()


	if len(str(x_coord).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_x_coord(address_id, x_coord))
		database_connection_object.commit()


	if len(str(y_coord).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_y_coord(address_id, y_coord))
		database_connection_object.commit()


	if len(str(status).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_status(address_id, status))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_description(address_id, description))
		database_connection_object.commit()


	if len(str(short_form).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_short_form(address_id, short_form))
		database_connection_object.commit()



def insert_tender(database_connection_object, query_executor, selection_object, insertion_object, tender_id, title, description, budget, status, evaluate_mechanism, publication_date_and_time, submission_cut_off_date_and_time, award_notice_date, contract_notice_date):

	query_executor.execute(selection_object.select_tender(tender_id))
	tender_check_query_result = query_executor.fetchall()
	result_list_length = len(tender_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_tender(tender_id))
		database_connection_object.commit()

	if len(str(title).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_tender_title(tender_id, title))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_tender_description(tender_id, description))
		database_connection_object.commit()


	if len(str(budget).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_tender_budget(tender_id, budget))
		database_connection_object.commit()


	if len(str(status).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_tender_status(tender_id, status))
		database_connection_object.commit()


	if len(str(evaluate_mechanism).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_tender_evaluate_mechanism(tender_id, evaluate_mechanism))
		database_connection_object.commit()


	if len(str(publication_date_and_time).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_tender_publication_date_and_time(tender_id, publication_date_and_time))
		database_connection_object.commit()


	if len(str(submission_cut_off_date_and_time).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_tender_submission_cut_off_date_and_time(tender_id, submission_cut_off_date_and_time))
		database_connection_object.commit()


	if len(str(award_notice_date).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_tender_award_notice_date(tender_id, award_notice_date))
		database_connection_object.commit()


	if len(str(contract_notice_date).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_tender_contract_notice_date(tender_id, contract_notice_date))
		database_connection_object.commit()



def insert_attachment(database_connection_object, query_executor, selection_object, insertion_object, attachment_id, type, name, description, link):

	query_executor.execute(selection_object.select_attachment(attachment_id))
	attachment_check_query_result = query_executor.fetchall()
	result_list_length = len(attachment_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_attachment(attachment_id))
		database_connection_object.commit()

	if len(str(type).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_attachment_type(attachment_id, type))
		database_connection_object.commit()


	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_attachment_name(attachment_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_attachment_description(attachment_id, description))
		database_connection_object.commit()


	if len(str(link).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_attachment_link(attachment_id, link))
		database_connection_object.commit()



def insert_award(database_connection_object, query_executor, selection_object, insertion_object, award_id, is_accepted, date_replied, reply_reason, award_amount):

	query_executor.execute(selection_object.select_award(award_id))
	award_check_query_result = query_executor.fetchall()
	result_list_length = len(award_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_award(award_id))
		database_connection_object.commit()

	if len(str(is_accepted).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_award_is_accepted(award_id, is_accepted))
		database_connection_object.commit()


	if len(str(date_replied).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_award_date_replied(award_id, date_replied))
		database_connection_object.commit()


	if len(str(reply_reason).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_award_reply_reason(award_id, reply_reason))
		database_connection_object.commit()


	if len(str(award_amount).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_award_award_amount(award_id, award_amount))
		database_connection_object.commit()



def insert_contact(database_connection_object, query_executor, selection_object, insertion_object, contact_id, name, value, status):

	query_executor.execute(selection_object.select_contact(contact_id))
	contact_check_query_result = query_executor.fetchall()
	result_list_length = len(contact_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_contact(contact_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_contact_name(contact_id, name))
		database_connection_object.commit()


	if len(str(value).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_contact_value(contact_id, value))
		database_connection_object.commit()


	if len(str(status).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_contact_status(contact_id, status))
		database_connection_object.commit()



def insert_contract(database_connection_object, query_executor, selection_object, insertion_object, contract_id, title, amount, status, description):

	query_executor.execute(selection_object.select_contract(contract_id))
	contract_check_query_result = query_executor.fetchall()
	result_list_length = len(contract_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_contract(contract_id))
		database_connection_object.commit()

	if len(str(title).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_contract_title(contract_id, title))
		database_connection_object.commit()


	if len(str(amount).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_contract_amount(contract_id, amount))
		database_connection_object.commit()


	if len(str(status).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_contract_status(contract_id, status))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_contract_description(contract_id, description))
		database_connection_object.commit()



def insert_fee(database_connection_object, query_executor, selection_object, insertion_object, fee_id, name, amount, type):

	query_executor.execute(selection_object.select_fee(fee_id))
	fee_check_query_result = query_executor.fetchall()
	result_list_length = len(fee_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_fee(fee_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_fee_name(fee_id, name))
		database_connection_object.commit()


	if len(str(amount).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_fee_amount(fee_id, amount))
		database_connection_object.commit()


	if len(str(type).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_fee_type(fee_id, type))
		database_connection_object.commit()



def insert_payment(database_connection_object, query_executor, selection_object, insertion_object, payment_id, transaction_id, date_received, amount, currency, status, extra_information):

	query_executor.execute(selection_object.select_payment(payment_id))
	payment_check_query_result = query_executor.fetchall()
	result_list_length = len(payment_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_payment(payment_id))
		database_connection_object.commit()

	if len(str(transaction_id).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_payment_transaction_id(payment_id, transaction_id))
		database_connection_object.commit()


	if len(str(date_received).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_payment_date_received(payment_id, date_received))
		database_connection_object.commit()


	if len(str(amount).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_payment_amount(payment_id, amount))
		database_connection_object.commit()


	if len(str(currency).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_payment_currency(payment_id, currency))
		database_connection_object.commit()


	if len(str(status).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_payment_status(payment_id, status))
		database_connection_object.commit()


	if len(str(extra_information).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_payment_extra_information(payment_id, extra_information))
		database_connection_object.commit()



def insert_plan(database_connection_object, query_executor, selection_object, insertion_object, plan_id, budget, submission_date_and_time, description):

	query_executor.execute(selection_object.select_plan(plan_id))
	plan_check_query_result = query_executor.fetchall()
	result_list_length = len(plan_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_plan(plan_id))
		database_connection_object.commit()

	if len(str(budget).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_plan_budget(plan_id, budget))
		database_connection_object.commit()


	if len(str(submission_date_and_time).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_plan_submission_date_and_time(plan_id, submission_date_and_time))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_plan_description(plan_id, description))
		database_connection_object.commit()



def insert_alert(database_connection_object, query_executor, selection_object, insertion_object, alert_id, subject, description):

	query_executor.execute(selection_object.select_alert(alert_id))
	alert_check_query_result = query_executor.fetchall()
	result_list_length = len(alert_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert(alert_id))
		database_connection_object.commit()

	if len(str(subject).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_subject(alert_id, subject))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_description(alert_id, description))
		database_connection_object.commit()



def insert_alert_authority(database_connection_object, query_executor, selection_object, insertion_object, alert_authority_id, name, description):

	query_executor.execute(selection_object.select_alert_authority(alert_authority_id))
	alert_authority_check_query_result = query_executor.fetchall()
	result_list_length = len(alert_authority_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_authority(alert_authority_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_authority_name(alert_authority_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_authority_description(alert_authority_id, description))
		database_connection_object.commit()



def insert_alert_level(database_connection_object, query_executor, selection_object, insertion_object, alert_level_id, name, description):

	query_executor.execute(selection_object.select_alert_level(alert_level_id))
	alert_level_check_query_result = query_executor.fetchall()
	result_list_length = len(alert_level_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_level(alert_level_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_level_name(alert_level_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_level_description(alert_level_id, description))
		database_connection_object.commit()



def insert_user_account(database_connection_object, query_executor, selection_object, insertion_object, user_account_id, national_id_number, category, first_name, last_name, other_names, date_of_birth, gender, status, email, password, photo):

	query_executor.execute(selection_object.select_user_account(user_account_id))
	user_account_check_query_result = query_executor.fetchall()
	result_list_length = len(user_account_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_account(user_account_id))
		database_connection_object.commit()

	if len(str(national_id_number).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_account_national_id_number(user_account_id, national_id_number))
		database_connection_object.commit()


	if len(str(category).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_account_category(user_account_id, category))
		database_connection_object.commit()


	if len(str(first_name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_account_first_name(user_account_id, first_name))
		database_connection_object.commit()


	if len(str(last_name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_account_last_name(user_account_id, last_name))
		database_connection_object.commit()


	if len(str(other_names).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_account_other_names(user_account_id, other_names))
		database_connection_object.commit()


	if len(str(date_of_birth).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_account_date_of_birth(user_account_id, date_of_birth))
		database_connection_object.commit()


	if len(str(gender).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_account_gender(user_account_id, gender))
		database_connection_object.commit()


	if len(str(status).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_account_status(user_account_id, status))
		database_connection_object.commit()


	if len(str(email).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_account_email(user_account_id, email))
		database_connection_object.commit()


	if len(str(password).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_account_password(user_account_id, password))
		database_connection_object.commit()


	if len(str(photo).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_account_photo(user_account_id, photo))
		database_connection_object.commit()



def insert_appeal(database_connection_object, query_executor, selection_object, insertion_object, appeal_id, subject, description):

	query_executor.execute(selection_object.select_appeal(appeal_id))
	appeal_check_query_result = query_executor.fetchall()
	result_list_length = len(appeal_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_appeal(appeal_id))
		database_connection_object.commit()

	if len(str(subject).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_appeal_subject(appeal_id, subject))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_appeal_description(appeal_id, description))
		database_connection_object.commit()



def insert_countryfiscal_yearmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, country_id, fiscal_year_id):

	query_executor.execute(selection_object.select_countryfiscal_yearmap(key_column, country_id, fiscal_year_id))
	countryfiscal_yearmap_check_query_result = query_executor.fetchall()
	result_list_length = len(countryfiscal_yearmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_countryfiscal_yearmap(key_column, country_id, fiscal_year_id))
		database_connection_object.commit()


def insert_countryprocurement_stagemap(database_connection_object, query_executor, selection_object, insertion_object, key_column, country_id, procurement_stage_id):

	query_executor.execute(selection_object.select_countryprocurement_stagemap(key_column, country_id, procurement_stage_id))
	countryprocurement_stagemap_check_query_result = query_executor.fetchall()
	result_list_length = len(countryprocurement_stagemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_countryprocurement_stagemap(key_column, country_id, procurement_stage_id))
		database_connection_object.commit()


def insert_countryprocurement_typemap(database_connection_object, query_executor, selection_object, insertion_object, key_column, country_id, procurement_type_id):

	query_executor.execute(selection_object.select_countryprocurement_typemap(key_column, country_id, procurement_type_id))
	countryprocurement_typemap_check_query_result = query_executor.fetchall()
	result_list_length = len(countryprocurement_typemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_countryprocurement_typemap(key_column, country_id, procurement_type_id))
		database_connection_object.commit()


def insert_countryprocurement_methodmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, country_id, procurement_method_id):

	query_executor.execute(selection_object.select_countryprocurement_methodmap(key_column, country_id, procurement_method_id))
	countryprocurement_methodmap_check_query_result = query_executor.fetchall()
	result_list_length = len(countryprocurement_methodmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_countryprocurement_methodmap(key_column, country_id, procurement_method_id))
		database_connection_object.commit()


def insert_countryprocuring_entitymap(database_connection_object, query_executor, selection_object, insertion_object, key_column, country_id, procuring_entity_id):

	query_executor.execute(selection_object.select_countryprocuring_entitymap(key_column, country_id, procuring_entity_id))
	countryprocuring_entitymap_check_query_result = query_executor.fetchall()
	result_list_length = len(countryprocuring_entitymap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_countryprocuring_entitymap(key_column, country_id, procuring_entity_id))
		database_connection_object.commit()


def insert_countrysupplying_entitymap(database_connection_object, query_executor, selection_object, insertion_object, key_column, country_id, supplying_entity_id):

	query_executor.execute(selection_object.select_countrysupplying_entitymap(key_column, country_id, supplying_entity_id))
	countrysupplying_entitymap_check_query_result = query_executor.fetchall()
	result_list_length = len(countrysupplying_entitymap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_countrysupplying_entitymap(key_column, country_id, supplying_entity_id))
		database_connection_object.commit()


def insert_countryred_flagmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, country_id, red_flag_id):

	query_executor.execute(selection_object.select_countryred_flagmap(key_column, country_id, red_flag_id))
	countryred_flagmap_check_query_result = query_executor.fetchall()
	result_list_length = len(countryred_flagmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_countryred_flagmap(key_column, country_id, red_flag_id))
		database_connection_object.commit()


def insert_countryillicit_schememap(database_connection_object, query_executor, selection_object, insertion_object, key_column, country_id, illicit_scheme_id):

	query_executor.execute(selection_object.select_countryillicit_schememap(key_column, country_id, illicit_scheme_id))
	countryillicit_schememap_check_query_result = query_executor.fetchall()
	result_list_length = len(countryillicit_schememap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_countryillicit_schememap(key_column, country_id, illicit_scheme_id))
		database_connection_object.commit()


def insert_fiscal_yeartendermap(database_connection_object, query_executor, selection_object, insertion_object, key_column, fiscal_year_id, tender_id):

	query_executor.execute(selection_object.select_fiscal_yeartendermap(key_column, fiscal_year_id, tender_id))
	fiscal_yeartendermap_check_query_result = query_executor.fetchall()
	result_list_length = len(fiscal_yeartendermap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_fiscal_yeartendermap(key_column, fiscal_year_id, tender_id))
		database_connection_object.commit()


def insert_fiscal_yearillicit_schememap(database_connection_object, query_executor, selection_object, insertion_object, key_column, fiscal_year_id, illicit_scheme_id):

	query_executor.execute(selection_object.select_fiscal_yearillicit_schememap(key_column, fiscal_year_id, illicit_scheme_id))
	fiscal_yearillicit_schememap_check_query_result = query_executor.fetchall()
	result_list_length = len(fiscal_yearillicit_schememap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_fiscal_yearillicit_schememap(key_column, fiscal_year_id, illicit_scheme_id))
		database_connection_object.commit()


def insert_fiscal_yearred_flagmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, fiscal_year_id, red_flag_id):

	query_executor.execute(selection_object.select_fiscal_yearred_flagmap(key_column, fiscal_year_id, red_flag_id))
	fiscal_yearred_flagmap_check_query_result = query_executor.fetchall()
	result_list_length = len(fiscal_yearred_flagmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_fiscal_yearred_flagmap(key_column, fiscal_year_id, red_flag_id))
		database_connection_object.commit()


def insert_fiscal_yearprocurement_stagemap(database_connection_object, query_executor, selection_object, insertion_object, key_column, fiscal_year_id, procurement_stage_id):

	query_executor.execute(selection_object.select_fiscal_yearprocurement_stagemap(key_column, fiscal_year_id, procurement_stage_id))
	fiscal_yearprocurement_stagemap_check_query_result = query_executor.fetchall()
	result_list_length = len(fiscal_yearprocurement_stagemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_fiscal_yearprocurement_stagemap(key_column, fiscal_year_id, procurement_stage_id))
		database_connection_object.commit()


def insert_fiscal_yearprocurement_typemap(database_connection_object, query_executor, selection_object, insertion_object, key_column, fiscal_year_id, procurement_type_id):

	query_executor.execute(selection_object.select_fiscal_yearprocurement_typemap(key_column, fiscal_year_id, procurement_type_id))
	fiscal_yearprocurement_typemap_check_query_result = query_executor.fetchall()
	result_list_length = len(fiscal_yearprocurement_typemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_fiscal_yearprocurement_typemap(key_column, fiscal_year_id, procurement_type_id))
		database_connection_object.commit()


def insert_fiscal_yearprocurement_methodmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, fiscal_year_id, procurement_method_id):

	query_executor.execute(selection_object.select_fiscal_yearprocurement_methodmap(key_column, fiscal_year_id, procurement_method_id))
	fiscal_yearprocurement_methodmap_check_query_result = query_executor.fetchall()
	result_list_length = len(fiscal_yearprocurement_methodmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_fiscal_yearprocurement_methodmap(key_column, fiscal_year_id, procurement_method_id))
		database_connection_object.commit()


def insert_fiscal_yearbidmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, fiscal_year_id, bid_id):

	query_executor.execute(selection_object.select_fiscal_yearbidmap(key_column, fiscal_year_id, bid_id))
	fiscal_yearbidmap_check_query_result = query_executor.fetchall()
	result_list_length = len(fiscal_yearbidmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_fiscal_yearbidmap(key_column, fiscal_year_id, bid_id))
		database_connection_object.commit()


def insert_fiscal_yearitemmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, fiscal_year_id, item_id):

	query_executor.execute(selection_object.select_fiscal_yearitemmap(key_column, fiscal_year_id, item_id))
	fiscal_yearitemmap_check_query_result = query_executor.fetchall()
	result_list_length = len(fiscal_yearitemmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_fiscal_yearitemmap(key_column, fiscal_year_id, item_id))
		database_connection_object.commit()


def insert_fiscal_yearcontractmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, fiscal_year_id, contract_id):

	query_executor.execute(selection_object.select_fiscal_yearcontractmap(key_column, fiscal_year_id, contract_id))
	fiscal_yearcontractmap_check_query_result = query_executor.fetchall()
	result_list_length = len(fiscal_yearcontractmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_fiscal_yearcontractmap(key_column, fiscal_year_id, contract_id))
		database_connection_object.commit()


def insert_fiscal_yearconfigurationmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, fiscal_year_id, configuration_id):

	query_executor.execute(selection_object.select_fiscal_yearconfigurationmap(key_column, fiscal_year_id, configuration_id))
	fiscal_yearconfigurationmap_check_query_result = query_executor.fetchall()
	result_list_length = len(fiscal_yearconfigurationmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_fiscal_yearconfigurationmap(key_column, fiscal_year_id, configuration_id))
		database_connection_object.commit()


def insert_fiscal_yearfeemap(database_connection_object, query_executor, selection_object, insertion_object, key_column, fiscal_year_id, fee_id):

	query_executor.execute(selection_object.select_fiscal_yearfeemap(key_column, fiscal_year_id, fee_id))
	fiscal_yearfeemap_check_query_result = query_executor.fetchall()
	result_list_length = len(fiscal_yearfeemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_fiscal_yearfeemap(key_column, fiscal_year_id, fee_id))
		database_connection_object.commit()


def insert_fiscal_yearprocuring_entitymap(database_connection_object, query_executor, selection_object, insertion_object, key_column, fiscal_year_id, procuring_entity_id):

	query_executor.execute(selection_object.select_fiscal_yearprocuring_entitymap(key_column, fiscal_year_id, procuring_entity_id))
	fiscal_yearprocuring_entitymap_check_query_result = query_executor.fetchall()
	result_list_length = len(fiscal_yearprocuring_entitymap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_fiscal_yearprocuring_entitymap(key_column, fiscal_year_id, procuring_entity_id))
		database_connection_object.commit()


def insert_fiscal_yearsupplying_entitymap(database_connection_object, query_executor, selection_object, insertion_object, key_column, fiscal_year_id, supplying_entity_id):

	query_executor.execute(selection_object.select_fiscal_yearsupplying_entitymap(key_column, fiscal_year_id, supplying_entity_id))
	fiscal_yearsupplying_entitymap_check_query_result = query_executor.fetchall()
	result_list_length = len(fiscal_yearsupplying_entitymap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_fiscal_yearsupplying_entitymap(key_column, fiscal_year_id, supplying_entity_id))
		database_connection_object.commit()


def insert_fiscal_yearawardmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, fiscal_year_id, award_id):

	query_executor.execute(selection_object.select_fiscal_yearawardmap(key_column, fiscal_year_id, award_id))
	fiscal_yearawardmap_check_query_result = query_executor.fetchall()
	result_list_length = len(fiscal_yearawardmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_fiscal_yearawardmap(key_column, fiscal_year_id, award_id))
		database_connection_object.commit()


def insert_fiscal_yearplanmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, fiscal_year_id, plan_id):

	query_executor.execute(selection_object.select_fiscal_yearplanmap(key_column, fiscal_year_id, plan_id))
	fiscal_yearplanmap_check_query_result = query_executor.fetchall()
	result_list_length = len(fiscal_yearplanmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_fiscal_yearplanmap(key_column, fiscal_year_id, plan_id))
		database_connection_object.commit()


def insert_red_flagconfigurationmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, red_flag_id, configuration_id):

	query_executor.execute(selection_object.select_red_flagconfigurationmap(key_column, red_flag_id, configuration_id))
	red_flagconfigurationmap_check_query_result = query_executor.fetchall()
	result_list_length = len(red_flagconfigurationmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_red_flagconfigurationmap(key_column, red_flag_id, configuration_id))
		database_connection_object.commit()


def insert_procurement_stagered_flagmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, procurement_stage_id, red_flag_id):

	query_executor.execute(selection_object.select_procurement_stagered_flagmap(key_column, procurement_stage_id, red_flag_id))
	procurement_stagered_flagmap_check_query_result = query_executor.fetchall()
	result_list_length = len(procurement_stagered_flagmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_stagered_flagmap(key_column, procurement_stage_id, red_flag_id))
		database_connection_object.commit()


def insert_procuring_entityred_flagmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, procuring_entity_id, red_flag_id):

	query_executor.execute(selection_object.select_procuring_entityred_flagmap(key_column, procuring_entity_id, red_flag_id))
	procuring_entityred_flagmap_check_query_result = query_executor.fetchall()
	result_list_length = len(procuring_entityred_flagmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entityred_flagmap(key_column, procuring_entity_id, red_flag_id))
		database_connection_object.commit()


def insert_supplying_entityred_flagmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, supplying_entity_id, red_flag_id):

	query_executor.execute(selection_object.select_supplying_entityred_flagmap(key_column, supplying_entity_id, red_flag_id))
	supplying_entityred_flagmap_check_query_result = query_executor.fetchall()
	result_list_length = len(supplying_entityred_flagmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entityred_flagmap(key_column, supplying_entity_id, red_flag_id))
		database_connection_object.commit()


def insert_procurement_typered_flagmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, procurement_type_id, red_flag_id):

	query_executor.execute(selection_object.select_procurement_typered_flagmap(key_column, procurement_type_id, red_flag_id))
	procurement_typered_flagmap_check_query_result = query_executor.fetchall()
	result_list_length = len(procurement_typered_flagmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_typered_flagmap(key_column, procurement_type_id, red_flag_id))
		database_connection_object.commit()


def insert_procurement_methodred_flagmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, procurement_method_id, red_flag_id):

	query_executor.execute(selection_object.select_procurement_methodred_flagmap(key_column, procurement_method_id, red_flag_id))
	procurement_methodred_flagmap_check_query_result = query_executor.fetchall()
	result_list_length = len(procurement_methodred_flagmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_methodred_flagmap(key_column, procurement_method_id, red_flag_id))
		database_connection_object.commit()


def insert_tenderred_flagmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, tender_id, red_flag_id):

	query_executor.execute(selection_object.select_tenderred_flagmap(key_column, tender_id, red_flag_id))
	tenderred_flagmap_check_query_result = query_executor.fetchall()
	result_list_length = len(tenderred_flagmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_tenderred_flagmap(key_column, tender_id, red_flag_id))
		database_connection_object.commit()


def insert_bidred_flagmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, bid_id, red_flag_id):

	query_executor.execute(selection_object.select_bidred_flagmap(key_column, bid_id, red_flag_id))
	bidred_flagmap_check_query_result = query_executor.fetchall()
	result_list_length = len(bidred_flagmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_bidred_flagmap(key_column, bid_id, red_flag_id))
		database_connection_object.commit()


def insert_itemred_flagmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, item_id, red_flag_id):

	query_executor.execute(selection_object.select_itemred_flagmap(key_column, item_id, red_flag_id))
	itemred_flagmap_check_query_result = query_executor.fetchall()
	result_list_length = len(itemred_flagmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_itemred_flagmap(key_column, item_id, red_flag_id))
		database_connection_object.commit()


def insert_contractred_flagmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, contract_id, red_flag_id):

	query_executor.execute(selection_object.select_contractred_flagmap(key_column, contract_id, red_flag_id))
	contractred_flagmap_check_query_result = query_executor.fetchall()
	result_list_length = len(contractred_flagmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_contractred_flagmap(key_column, contract_id, red_flag_id))
		database_connection_object.commit()


def insert_illicit_schemered_flagmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, illicit_scheme_id, red_flag_id):

	query_executor.execute(selection_object.select_illicit_schemered_flagmap(key_column, illicit_scheme_id, red_flag_id))
	illicit_schemered_flagmap_check_query_result = query_executor.fetchall()
	result_list_length = len(illicit_schemered_flagmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_illicit_schemered_flagmap(key_column, illicit_scheme_id, red_flag_id))
		database_connection_object.commit()


def insert_bidfeemap(database_connection_object, query_executor, selection_object, insertion_object, key_column, bid_id, fee_id):

	query_executor.execute(selection_object.select_bidfeemap(key_column, bid_id, fee_id))
	bidfeemap_check_query_result = query_executor.fetchall()
	result_list_length = len(bidfeemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_bidfeemap(key_column, bid_id, fee_id))
		database_connection_object.commit()


def insert_bidpaymentmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, bid_id, payment_id):

	query_executor.execute(selection_object.select_bidpaymentmap(key_column, bid_id, payment_id))
	bidpaymentmap_check_query_result = query_executor.fetchall()
	result_list_length = len(bidpaymentmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_bidpaymentmap(key_column, bid_id, payment_id))
		database_connection_object.commit()


def insert_bidawardmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, bid_id, award_id):

	query_executor.execute(selection_object.select_bidawardmap(key_column, bid_id, award_id))
	bidawardmap_check_query_result = query_executor.fetchall()
	result_list_length = len(bidawardmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_bidawardmap(key_column, bid_id, award_id))
		database_connection_object.commit()


def insert_tenderbidmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, tender_id, bid_id):

	query_executor.execute(selection_object.select_tenderbidmap(key_column, tender_id, bid_id))
	tenderbidmap_check_query_result = query_executor.fetchall()
	result_list_length = len(tenderbidmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_tenderbidmap(key_column, tender_id, bid_id))
		database_connection_object.commit()


def insert_tenderfeemap(database_connection_object, query_executor, selection_object, insertion_object, key_column, tender_id, fee_id):

	query_executor.execute(selection_object.select_tenderfeemap(key_column, tender_id, fee_id))
	tenderfeemap_check_query_result = query_executor.fetchall()
	result_list_length = len(tenderfeemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_tenderfeemap(key_column, tender_id, fee_id))
		database_connection_object.commit()


def insert_tenderpaymentmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, tender_id, payment_id):

	query_executor.execute(selection_object.select_tenderpaymentmap(key_column, tender_id, payment_id))
	tenderpaymentmap_check_query_result = query_executor.fetchall()
	result_list_length = len(tenderpaymentmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_tenderpaymentmap(key_column, tender_id, payment_id))
		database_connection_object.commit()


def insert_awardappealmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, award_id, appeal_id):

	query_executor.execute(selection_object.select_awardappealmap(key_column, award_id, appeal_id))
	awardappealmap_check_query_result = query_executor.fetchall()
	result_list_length = len(awardappealmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_awardappealmap(key_column, award_id, appeal_id))
		database_connection_object.commit()


def insert_procuring_entityprocurement_typemap(database_connection_object, query_executor, selection_object, insertion_object, key_column, procuring_entity_id, procurement_type_id):

	query_executor.execute(selection_object.select_procuring_entityprocurement_typemap(key_column, procuring_entity_id, procurement_type_id))
	procuring_entityprocurement_typemap_check_query_result = query_executor.fetchall()
	result_list_length = len(procuring_entityprocurement_typemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entityprocurement_typemap(key_column, procuring_entity_id, procurement_type_id))
		database_connection_object.commit()


def insert_procuring_entityprocurement_methodmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, procuring_entity_id, procurement_method_id):

	query_executor.execute(selection_object.select_procuring_entityprocurement_methodmap(key_column, procuring_entity_id, procurement_method_id))
	procuring_entityprocurement_methodmap_check_query_result = query_executor.fetchall()
	result_list_length = len(procuring_entityprocurement_methodmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entityprocurement_methodmap(key_column, procuring_entity_id, procurement_method_id))
		database_connection_object.commit()


def insert_procuring_entityprocurement_stagemap(database_connection_object, query_executor, selection_object, insertion_object, key_column, procuring_entity_id, procurement_stage_id):

	query_executor.execute(selection_object.select_procuring_entityprocurement_stagemap(key_column, procuring_entity_id, procurement_stage_id))
	procuring_entityprocurement_stagemap_check_query_result = query_executor.fetchall()
	result_list_length = len(procuring_entityprocurement_stagemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entityprocurement_stagemap(key_column, procuring_entity_id, procurement_stage_id))
		database_connection_object.commit()


def insert_procuring_entitybidmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, procuring_entity_id, bid_id):

	query_executor.execute(selection_object.select_procuring_entitybidmap(key_column, procuring_entity_id, bid_id))
	procuring_entitybidmap_check_query_result = query_executor.fetchall()
	result_list_length = len(procuring_entitybidmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entitybidmap(key_column, procuring_entity_id, bid_id))
		database_connection_object.commit()


def insert_procuring_entitytendermap(database_connection_object, query_executor, selection_object, insertion_object, key_column, procuring_entity_id, tender_id):

	query_executor.execute(selection_object.select_procuring_entitytendermap(key_column, procuring_entity_id, tender_id))
	procuring_entitytendermap_check_query_result = query_executor.fetchall()
	result_list_length = len(procuring_entitytendermap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entitytendermap(key_column, procuring_entity_id, tender_id))
		database_connection_object.commit()


def insert_procuring_entitycontractmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, procuring_entity_id, contract_id):

	query_executor.execute(selection_object.select_procuring_entitycontractmap(key_column, procuring_entity_id, contract_id))
	procuring_entitycontractmap_check_query_result = query_executor.fetchall()
	result_list_length = len(procuring_entitycontractmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entitycontractmap(key_column, procuring_entity_id, contract_id))
		database_connection_object.commit()


def insert_procuring_entityillicit_schememap(database_connection_object, query_executor, selection_object, insertion_object, key_column, procuring_entity_id, illicit_scheme_id):

	query_executor.execute(selection_object.select_procuring_entityillicit_schememap(key_column, procuring_entity_id, illicit_scheme_id))
	procuring_entityillicit_schememap_check_query_result = query_executor.fetchall()
	result_list_length = len(procuring_entityillicit_schememap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entityillicit_schememap(key_column, procuring_entity_id, illicit_scheme_id))
		database_connection_object.commit()


def insert_procuring_entityaddressmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, procuring_entity_id, address_id):

	query_executor.execute(selection_object.select_procuring_entityaddressmap(key_column, procuring_entity_id, address_id))
	procuring_entityaddressmap_check_query_result = query_executor.fetchall()
	result_list_length = len(procuring_entityaddressmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entityaddressmap(key_column, procuring_entity_id, address_id))
		database_connection_object.commit()


def insert_procuring_entityattachmentmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, procuring_entity_id, attachment_id):

	query_executor.execute(selection_object.select_procuring_entityattachmentmap(key_column, procuring_entity_id, attachment_id))
	procuring_entityattachmentmap_check_query_result = query_executor.fetchall()
	result_list_length = len(procuring_entityattachmentmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entityattachmentmap(key_column, procuring_entity_id, attachment_id))
		database_connection_object.commit()


def insert_procuring_entityplanmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, procuring_entity_id, plan_id):

	query_executor.execute(selection_object.select_procuring_entityplanmap(key_column, procuring_entity_id, plan_id))
	procuring_entityplanmap_check_query_result = query_executor.fetchall()
	result_list_length = len(procuring_entityplanmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entityplanmap(key_column, procuring_entity_id, plan_id))
		database_connection_object.commit()


def insert_procuring_entityawardmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, procuring_entity_id, award_id):

	query_executor.execute(selection_object.select_procuring_entityawardmap(key_column, procuring_entity_id, award_id))
	procuring_entityawardmap_check_query_result = query_executor.fetchall()
	result_list_length = len(procuring_entityawardmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entityawardmap(key_column, procuring_entity_id, award_id))
		database_connection_object.commit()


def insert_procuring_entitycontactmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, procuring_entity_id, contact_id):

	query_executor.execute(selection_object.select_procuring_entitycontactmap(key_column, procuring_entity_id, contact_id))
	procuring_entitycontactmap_check_query_result = query_executor.fetchall()
	result_list_length = len(procuring_entitycontactmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entitycontactmap(key_column, procuring_entity_id, contact_id))
		database_connection_object.commit()


def insert_procuring_entitypaymentmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, procuring_entity_id, payment_id):

	query_executor.execute(selection_object.select_procuring_entitypaymentmap(key_column, procuring_entity_id, payment_id))
	procuring_entitypaymentmap_check_query_result = query_executor.fetchall()
	result_list_length = len(procuring_entitypaymentmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entitypaymentmap(key_column, procuring_entity_id, payment_id))
		database_connection_object.commit()


def insert_procuring_entityuser_accountmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, procuring_entity_id, user_account_id):

	query_executor.execute(selection_object.select_procuring_entityuser_accountmap(key_column, procuring_entity_id, user_account_id))
	procuring_entityuser_accountmap_check_query_result = query_executor.fetchall()
	result_list_length = len(procuring_entityuser_accountmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entityuser_accountmap(key_column, procuring_entity_id, user_account_id))
		database_connection_object.commit()


def insert_procuring_entitysupplying_entitymap(database_connection_object, query_executor, selection_object, insertion_object, key_column, procuring_entity_id, supplying_entity_id):

	query_executor.execute(selection_object.select_procuring_entitysupplying_entitymap(key_column, procuring_entity_id, supplying_entity_id))
	procuring_entitysupplying_entitymap_check_query_result = query_executor.fetchall()
	result_list_length = len(procuring_entitysupplying_entitymap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entitysupplying_entitymap(key_column, procuring_entity_id, supplying_entity_id))
		database_connection_object.commit()


def insert_supplying_entityprocurement_typemap(database_connection_object, query_executor, selection_object, insertion_object, key_column, supplying_entity_id, procurement_type_id):

	query_executor.execute(selection_object.select_supplying_entityprocurement_typemap(key_column, supplying_entity_id, procurement_type_id))
	supplying_entityprocurement_typemap_check_query_result = query_executor.fetchall()
	result_list_length = len(supplying_entityprocurement_typemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entityprocurement_typemap(key_column, supplying_entity_id, procurement_type_id))
		database_connection_object.commit()


def insert_supplying_entityprocurement_methodmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, supplying_entity_id, procurement_method_id):

	query_executor.execute(selection_object.select_supplying_entityprocurement_methodmap(key_column, supplying_entity_id, procurement_method_id))
	supplying_entityprocurement_methodmap_check_query_result = query_executor.fetchall()
	result_list_length = len(supplying_entityprocurement_methodmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entityprocurement_methodmap(key_column, supplying_entity_id, procurement_method_id))
		database_connection_object.commit()


def insert_supplying_entityprocurement_stagemap(database_connection_object, query_executor, selection_object, insertion_object, key_column, supplying_entity_id, procurement_stage_id):

	query_executor.execute(selection_object.select_supplying_entityprocurement_stagemap(key_column, supplying_entity_id, procurement_stage_id))
	supplying_entityprocurement_stagemap_check_query_result = query_executor.fetchall()
	result_list_length = len(supplying_entityprocurement_stagemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entityprocurement_stagemap(key_column, supplying_entity_id, procurement_stage_id))
		database_connection_object.commit()


def insert_supplying_entitybidmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, supplying_entity_id, bid_id):

	query_executor.execute(selection_object.select_supplying_entitybidmap(key_column, supplying_entity_id, bid_id))
	supplying_entitybidmap_check_query_result = query_executor.fetchall()
	result_list_length = len(supplying_entitybidmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entitybidmap(key_column, supplying_entity_id, bid_id))
		database_connection_object.commit()


def insert_supplying_entitytendermap(database_connection_object, query_executor, selection_object, insertion_object, key_column, supplying_entity_id, tender_id):

	query_executor.execute(selection_object.select_supplying_entitytendermap(key_column, supplying_entity_id, tender_id))
	supplying_entitytendermap_check_query_result = query_executor.fetchall()
	result_list_length = len(supplying_entitytendermap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entitytendermap(key_column, supplying_entity_id, tender_id))
		database_connection_object.commit()


def insert_supplying_entitycontractmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, supplying_entity_id, contract_id):

	query_executor.execute(selection_object.select_supplying_entitycontractmap(key_column, supplying_entity_id, contract_id))
	supplying_entitycontractmap_check_query_result = query_executor.fetchall()
	result_list_length = len(supplying_entitycontractmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entitycontractmap(key_column, supplying_entity_id, contract_id))
		database_connection_object.commit()


def insert_supplying_entityillicit_schememap(database_connection_object, query_executor, selection_object, insertion_object, key_column, supplying_entity_id, illicit_scheme_id):

	query_executor.execute(selection_object.select_supplying_entityillicit_schememap(key_column, supplying_entity_id, illicit_scheme_id))
	supplying_entityillicit_schememap_check_query_result = query_executor.fetchall()
	result_list_length = len(supplying_entityillicit_schememap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entityillicit_schememap(key_column, supplying_entity_id, illicit_scheme_id))
		database_connection_object.commit()


def insert_supplying_entityaddressmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, supplying_entity_id, address_id):

	query_executor.execute(selection_object.select_supplying_entityaddressmap(key_column, supplying_entity_id, address_id))
	supplying_entityaddressmap_check_query_result = query_executor.fetchall()
	result_list_length = len(supplying_entityaddressmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entityaddressmap(key_column, supplying_entity_id, address_id))
		database_connection_object.commit()


def insert_supplying_entityattachmentmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, supplying_entity_id, attachment_id):

	query_executor.execute(selection_object.select_supplying_entityattachmentmap(key_column, supplying_entity_id, attachment_id))
	supplying_entityattachmentmap_check_query_result = query_executor.fetchall()
	result_list_length = len(supplying_entityattachmentmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entityattachmentmap(key_column, supplying_entity_id, attachment_id))
		database_connection_object.commit()


def insert_supplying_entityawardmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, supplying_entity_id, award_id):

	query_executor.execute(selection_object.select_supplying_entityawardmap(key_column, supplying_entity_id, award_id))
	supplying_entityawardmap_check_query_result = query_executor.fetchall()
	result_list_length = len(supplying_entityawardmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entityawardmap(key_column, supplying_entity_id, award_id))
		database_connection_object.commit()


def insert_supplying_entitycontactmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, supplying_entity_id, contact_id):

	query_executor.execute(selection_object.select_supplying_entitycontactmap(key_column, supplying_entity_id, contact_id))
	supplying_entitycontactmap_check_query_result = query_executor.fetchall()
	result_list_length = len(supplying_entitycontactmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entitycontactmap(key_column, supplying_entity_id, contact_id))
		database_connection_object.commit()


def insert_supplying_entitypaymentmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, supplying_entity_id, payment_id):

	query_executor.execute(selection_object.select_supplying_entitypaymentmap(key_column, supplying_entity_id, payment_id))
	supplying_entitypaymentmap_check_query_result = query_executor.fetchall()
	result_list_length = len(supplying_entitypaymentmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entitypaymentmap(key_column, supplying_entity_id, payment_id))
		database_connection_object.commit()


def insert_supplying_entityuser_accountmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, supplying_entity_id, user_account_id):

	query_executor.execute(selection_object.select_supplying_entityuser_accountmap(key_column, supplying_entity_id, user_account_id))
	supplying_entityuser_accountmap_check_query_result = query_executor.fetchall()
	result_list_length = len(supplying_entityuser_accountmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entityuser_accountmap(key_column, supplying_entity_id, user_account_id))
		database_connection_object.commit()


def insert_contractawardmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, contract_id, award_id):

	query_executor.execute(selection_object.select_contractawardmap(key_column, contract_id, award_id))
	contractawardmap_check_query_result = query_executor.fetchall()
	result_list_length = len(contractawardmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_contractawardmap(key_column, contract_id, award_id))
		database_connection_object.commit()


def insert_paymentfeemap(database_connection_object, query_executor, selection_object, insertion_object, key_column, payment_id, fee_id):

	query_executor.execute(selection_object.select_paymentfeemap(key_column, payment_id, fee_id))
	paymentfeemap_check_query_result = query_executor.fetchall()
	result_list_length = len(paymentfeemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_paymentfeemap(key_column, payment_id, fee_id))
		database_connection_object.commit()


def insert_alert_authorityuser_accountmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, alert_authority_id, user_account_id):

	query_executor.execute(selection_object.select_alert_authorityuser_accountmap(key_column, alert_authority_id, user_account_id))
	alert_authorityuser_accountmap_check_query_result = query_executor.fetchall()
	result_list_length = len(alert_authorityuser_accountmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_authorityuser_accountmap(key_column, alert_authority_id, user_account_id))
		database_connection_object.commit()


def insert_alert_authorityalert_levelmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, alert_authority_id, alert_level_id):

	query_executor.execute(selection_object.select_alert_authorityalert_levelmap(key_column, alert_authority_id, alert_level_id))
	alert_authorityalert_levelmap_check_query_result = query_executor.fetchall()
	result_list_length = len(alert_authorityalert_levelmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_authorityalert_levelmap(key_column, alert_authority_id, alert_level_id))
		database_connection_object.commit()


def insert_alert_authorityalertmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, alert_authority_id, alert_id):

	query_executor.execute(selection_object.select_alert_authorityalertmap(key_column, alert_authority_id, alert_id))
	alert_authorityalertmap_check_query_result = query_executor.fetchall()
	result_list_length = len(alert_authorityalertmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_authorityalertmap(key_column, alert_authority_id, alert_id))
		database_connection_object.commit()


def insert_alert_authorityaddressmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, alert_authority_id, address_id):

	query_executor.execute(selection_object.select_alert_authorityaddressmap(key_column, alert_authority_id, address_id))
	alert_authorityaddressmap_check_query_result = query_executor.fetchall()
	result_list_length = len(alert_authorityaddressmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_authorityaddressmap(key_column, alert_authority_id, address_id))
		database_connection_object.commit()


def insert_alert_leveluser_accountmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, alert_level_id, user_account_id):

	query_executor.execute(selection_object.select_alert_leveluser_accountmap(key_column, alert_level_id, user_account_id))
	alert_leveluser_accountmap_check_query_result = query_executor.fetchall()
	result_list_length = len(alert_leveluser_accountmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_leveluser_accountmap(key_column, alert_level_id, user_account_id))
		database_connection_object.commit()


def insert_alert_levelred_flagmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, alert_level_id, red_flag_id):

	query_executor.execute(selection_object.select_alert_levelred_flagmap(key_column, alert_level_id, red_flag_id))
	alert_levelred_flagmap_check_query_result = query_executor.fetchall()
	result_list_length = len(alert_levelred_flagmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_levelred_flagmap(key_column, alert_level_id, red_flag_id))
		database_connection_object.commit()


def insert_alert_leveladdressmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, alert_level_id, address_id):

	query_executor.execute(selection_object.select_alert_leveladdressmap(key_column, alert_level_id, address_id))
	alert_leveladdressmap_check_query_result = query_executor.fetchall()
	result_list_length = len(alert_leveladdressmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_leveladdressmap(key_column, alert_level_id, address_id))
		database_connection_object.commit()


def insert_alertred_flagmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, alert_id, red_flag_id):

	query_executor.execute(selection_object.select_alertred_flagmap(key_column, alert_id, red_flag_id))
	alertred_flagmap_check_query_result = query_executor.fetchall()
	result_list_length = len(alertred_flagmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_alertred_flagmap(key_column, alert_id, red_flag_id))
		database_connection_object.commit()


def insert_alertattachmentmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, alert_id, attachment_id):

	query_executor.execute(selection_object.select_alertattachmentmap(key_column, alert_id, attachment_id))
	alertattachmentmap_check_query_result = query_executor.fetchall()
	result_list_length = len(alertattachmentmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_alertattachmentmap(key_column, alert_id, attachment_id))
		database_connection_object.commit()


def insert_alert_authoritycontactmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, alert_authority_id, contact_id):

	query_executor.execute(selection_object.select_alert_authoritycontactmap(key_column, alert_authority_id, contact_id))
	alert_authoritycontactmap_check_query_result = query_executor.fetchall()
	result_list_length = len(alert_authoritycontactmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_authoritycontactmap(key_column, alert_authority_id, contact_id))
		database_connection_object.commit()


def insert_alert_levelcontactmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, alert_level_id, contact_id):

	query_executor.execute(selection_object.select_alert_levelcontactmap(key_column, alert_level_id, contact_id))
	alert_levelcontactmap_check_query_result = query_executor.fetchall()
	result_list_length = len(alert_levelcontactmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_levelcontactmap(key_column, alert_level_id, contact_id))
		database_connection_object.commit()


def insert_user_accountcontactmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, user_account_id, contact_id):

	query_executor.execute(selection_object.select_user_accountcontactmap(key_column, user_account_id, contact_id))
	user_accountcontactmap_check_query_result = query_executor.fetchall()
	result_list_length = len(user_accountcontactmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_accountcontactmap(key_column, user_account_id, contact_id))
		database_connection_object.commit()


def insert_user_accountaddressmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, user_account_id, address_id):

	query_executor.execute(selection_object.select_user_accountaddressmap(key_column, user_account_id, address_id))
	user_accountaddressmap_check_query_result = query_executor.fetchall()
	result_list_length = len(user_accountaddressmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_accountaddressmap(key_column, user_account_id, address_id))
		database_connection_object.commit()


def insert_user_accountsubmissionmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, user_account_id, submission_id):

	query_executor.execute(selection_object.select_user_accountsubmissionmap(key_column, user_account_id, submission_id))
	user_accountsubmissionmap_check_query_result = query_executor.fetchall()
	result_list_length = len(user_accountsubmissionmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_accountsubmissionmap(key_column, user_account_id, submission_id))
		database_connection_object.commit()


def insert_procurement_stagesubmissionmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, procurement_stage_id, submission_id):

	query_executor.execute(selection_object.select_procurement_stagesubmissionmap(key_column, procurement_stage_id, submission_id))
	procurement_stagesubmissionmap_check_query_result = query_executor.fetchall()
	result_list_length = len(procurement_stagesubmissionmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_stagesubmissionmap(key_column, procurement_stage_id, submission_id))
		database_connection_object.commit()


def insert_plansubmissionmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, plan_id, submission_id):

	query_executor.execute(selection_object.select_plansubmissionmap(key_column, plan_id, submission_id))
	plansubmissionmap_check_query_result = query_executor.fetchall()
	result_list_length = len(plansubmissionmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_plansubmissionmap(key_column, plan_id, submission_id))
		database_connection_object.commit()


def insert_submissionattachmentmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, submission_id, attachment_id):

	query_executor.execute(selection_object.select_submissionattachmentmap(key_column, submission_id, attachment_id))
	submissionattachmentmap_check_query_result = query_executor.fetchall()
	result_list_length = len(submissionattachmentmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_submissionattachmentmap(key_column, submission_id, attachment_id))
		database_connection_object.commit()


def insert_appealattachmentmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, appeal_id, attachment_id):

	query_executor.execute(selection_object.select_appealattachmentmap(key_column, appeal_id, attachment_id))
	appealattachmentmap_check_query_result = query_executor.fetchall()
	result_list_length = len(appealattachmentmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_appealattachmentmap(key_column, appeal_id, attachment_id))
		database_connection_object.commit()


def insert_user_accountattachmentmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, user_account_id, attachment_id):

	query_executor.execute(selection_object.select_user_accountattachmentmap(key_column, user_account_id, attachment_id))
	user_accountattachmentmap_check_query_result = query_executor.fetchall()
	result_list_length = len(user_accountattachmentmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_accountattachmentmap(key_column, user_account_id, attachment_id))
		database_connection_object.commit()


def insert_awardsubmissionmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, award_id, submission_id):

	query_executor.execute(selection_object.select_awardsubmissionmap(key_column, award_id, submission_id))
	awardsubmissionmap_check_query_result = query_executor.fetchall()
	result_list_length = len(awardsubmissionmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_awardsubmissionmap(key_column, award_id, submission_id))
		database_connection_object.commit()


def insert_user_accountplanmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, user_account_id, plan_id):

	query_executor.execute(selection_object.select_user_accountplanmap(key_column, user_account_id, plan_id))
	user_accountplanmap_check_query_result = query_executor.fetchall()
	result_list_length = len(user_accountplanmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_accountplanmap(key_column, user_account_id, plan_id))
		database_connection_object.commit()


def insert_awardtendermap(database_connection_object, query_executor, selection_object, insertion_object, key_column, award_id, tender_id):

	query_executor.execute(selection_object.select_awardtendermap(key_column, award_id, tender_id))
	awardtendermap_check_query_result = query_executor.fetchall()
	result_list_length = len(awardtendermap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_awardtendermap(key_column, award_id, tender_id))
		database_connection_object.commit()


def insert_bidsubmissionmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, bid_id, submission_id):

	query_executor.execute(selection_object.select_bidsubmissionmap(key_column, bid_id, submission_id))
	bidsubmissionmap_check_query_result = query_executor.fetchall()
	result_list_length = len(bidsubmissionmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_bidsubmissionmap(key_column, bid_id, submission_id))
		database_connection_object.commit()


def insert_tenderappealmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, tender_id, appeal_id):

	query_executor.execute(selection_object.select_tenderappealmap(key_column, tender_id, appeal_id))
	tenderappealmap_check_query_result = query_executor.fetchall()
	result_list_length = len(tenderappealmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_tenderappealmap(key_column, tender_id, appeal_id))
		database_connection_object.commit()

