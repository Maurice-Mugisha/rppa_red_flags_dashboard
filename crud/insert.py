


class Insert:

	def  __init__(self, instance_name):
		self.instance_name = instance_name

	def  __str__(self):
		return self.instance_name


	def insert_country(self, country_id):
		query = "INSERT INTO country VALUES('" + country_id + "');"
		return query

	def insert_country_code(self, country_id, code):
		query = "INSERT INTO country_code VALUES('" + country_id + "', '" + code + "');"
		return query

	def insert_country_name(self, country_id, name):
		query = "INSERT INTO country_name VALUES('" + country_id + "', '" + name + "');"
		return query

	def insert_country_currency(self, country_id, currency):
		query = "INSERT INTO country_currency VALUES('" + country_id + "', '" + currency + "');"
		return query

	def insert_country_flag(self, country_id, flag):
		query = "INSERT INTO country_flag VALUES('" + country_id + "', '" + flag + "');"
		return query

	def insert_country_coat_of_arms(self, country_id, coat_of_arms):
		query = "INSERT INTO country_coat_of_arms VALUES('" + country_id + "', '" + coat_of_arms + "');"
		return query

	def insert_fiscal_year(self, fiscal_year_id):
		query = "INSERT INTO fiscal_year VALUES('" + fiscal_year_id + "');"
		return query

	def insert_fiscal_year_start_date(self, fiscal_year_id, start_date):
		query = "INSERT INTO fiscal_year_start_date VALUES('" + fiscal_year_id + "', '" + start_date + "');"
		return query

	def insert_fiscal_year_end_date(self, fiscal_year_id, end_date):
		query = "INSERT INTO fiscal_year_end_date VALUES('" + fiscal_year_id + "', '" + end_date + "');"
		return query

	def insert_configuration(self, configuration_id):
		query = "INSERT INTO configuration VALUES('" + configuration_id + "');"
		return query

	def insert_configuration_name(self, configuration_id, name):
		query = "INSERT INTO configuration_name VALUES('" + configuration_id + "', '" + name + "');"
		return query

	def insert_configuration_description(self, configuration_id, description):
		query = "INSERT INTO configuration_description VALUES('" + configuration_id + "', '" + description + "');"
		return query

	def insert_configuration_value(self, configuration_id, value):
		query = "INSERT INTO configuration_value VALUES('" + configuration_id + "', '" + value + "');"
		return query

	def insert_configuration_status(self, configuration_id, status):
		query = "INSERT INTO configuration_status VALUES('" + configuration_id + "', '" + status + "');"
		return query

	def insert_red_flag(self, red_flag_id):
		query = "INSERT INTO red_flag VALUES('" + red_flag_id + "');"
		return query

	def insert_red_flag_name(self, red_flag_id, name):
		query = "INSERT INTO red_flag_name VALUES('" + red_flag_id + "', '" + name + "');"
		return query

	def insert_red_flag_description(self, red_flag_id, description):
		query = "INSERT INTO red_flag_description VALUES('" + red_flag_id + "', '" + description + "');"
		return query

	def insert_red_flag_status(self, red_flag_id, status):
		query = "INSERT INTO red_flag_status VALUES('" + red_flag_id + "', '" + status + "');"
		return query

	def insert_illicit_scheme(self, illicit_scheme_id):
		query = "INSERT INTO illicit_scheme VALUES('" + illicit_scheme_id + "');"
		return query

	def insert_illicit_scheme_name(self, illicit_scheme_id, name):
		query = "INSERT INTO illicit_scheme_name VALUES('" + illicit_scheme_id + "', '" + name + "');"
		return query

	def insert_illicit_scheme_description(self, illicit_scheme_id, description):
		query = "INSERT INTO illicit_scheme_description VALUES('" + illicit_scheme_id + "', '" + description + "');"
		return query

	def insert_procurement_stage(self, procurement_stage_id):
		query = "INSERT INTO procurement_stage VALUES('" + procurement_stage_id + "');"
		return query

	def insert_procurement_stage_name(self, procurement_stage_id, name):
		query = "INSERT INTO procurement_stage_name VALUES('" + procurement_stage_id + "', '" + name + "');"
		return query

	def insert_procurement_stage_description(self, procurement_stage_id, description):
		query = "INSERT INTO procurement_stage_description VALUES('" + procurement_stage_id + "', '" + description + "');"
		return query

	def insert_submission(self, submission_id):
		query = "INSERT INTO submission VALUES('" + submission_id + "');"
		return query

	def insert_submission_name(self, submission_id, name):
		query = "INSERT INTO submission_name VALUES('" + submission_id + "', '" + name + "');"
		return query

	def insert_submission_description(self, submission_id, description):
		query = "INSERT INTO submission_description VALUES('" + submission_id + "', '" + description + "');"
		return query

	def insert_submission_reception_date_and_time(self, submission_id, reception_date_and_time):
		query = "INSERT INTO submission_reception_date_and_time VALUES('" + submission_id + "', '" + reception_date_and_time + "');"
		return query

	def insert_submission_cut_off_date_and_time(self, submission_id, cut_off_date_and_time):
		query = "INSERT INTO submission_cut_off_date_and_time VALUES('" + submission_id + "', '" + cut_off_date_and_time + "');"
		return query

	def insert_procurement_type(self, procurement_type_id):
		query = "INSERT INTO procurement_type VALUES('" + procurement_type_id + "');"
		return query

	def insert_procurement_type_code(self, procurement_type_id, code):
		query = "INSERT INTO procurement_type_code VALUES('" + procurement_type_id + "', '" + code + "');"
		return query

	def insert_procurement_type_name(self, procurement_type_id, name):
		query = "INSERT INTO procurement_type_name VALUES('" + procurement_type_id + "', '" + name + "');"
		return query

	def insert_procurement_type_description(self, procurement_type_id, description):
		query = "INSERT INTO procurement_type_description VALUES('" + procurement_type_id + "', '" + description + "');"
		return query

	def insert_procurement_method(self, procurement_method_id):
		query = "INSERT INTO procurement_method VALUES('" + procurement_method_id + "');"
		return query

	def insert_procurement_method_code(self, procurement_method_id, code):
		query = "INSERT INTO procurement_method_code VALUES('" + procurement_method_id + "', '" + code + "');"
		return query

	def insert_procurement_method_name(self, procurement_method_id, name):
		query = "INSERT INTO procurement_method_name VALUES('" + procurement_method_id + "', '" + name + "');"
		return query

	def insert_procurement_method_description(self, procurement_method_id, description):
		query = "INSERT INTO procurement_method_description VALUES('" + procurement_method_id + "', '" + description + "');"
		return query

	def insert_bid(self, bid_id):
		query = "INSERT INTO bid VALUES('" + bid_id + "');"
		return query

	def insert_bid_submission_date(self, bid_id, submission_date):
		query = "INSERT INTO bid_submission_date VALUES('" + bid_id + "', '" + submission_date + "');"
		return query

	def insert_bid_amount(self, bid_id, amount):
		query = "INSERT INTO bid_amount VALUES('" + bid_id + "', " + amount + ");"
		return query

	def insert_bid_extra_information(self, bid_id, extra_information):
		query = "INSERT INTO bid_extra_information VALUES('" + bid_id + "', '" + extra_information + "');"
		return query

	def insert_item(self, item_id):
		query = "INSERT INTO item VALUES('" + item_id + "');"
		return query

	def insert_item_code(self, item_id, code):
		query = "INSERT INTO item_code VALUES('" + item_id + "', '" + code + "');"
		return query

	def insert_item_name(self, item_id, name):
		query = "INSERT INTO item_name VALUES('" + item_id + "', '" + name + "');"
		return query

	def insert_item_unit_cost(self, item_id, unit_cost):
		query = "INSERT INTO item_unit_cost VALUES('" + item_id + "', " + unit_cost + ");"
		return query

	def insert_item_description(self, item_id, description):
		query = "INSERT INTO item_description VALUES('" + item_id + "', '" + description + "');"
		return query

	def insert_procuring_entity(self, procuring_entity_id):
		query = "INSERT INTO procuring_entity VALUES('" + procuring_entity_id + "');"
		return query

	def insert_procuring_entity_name(self, procuring_entity_id, name):
		query = "INSERT INTO procuring_entity_name VALUES('" + procuring_entity_id + "', '" + name + "');"
		return query

	def insert_procuring_entity_tax_identifier(self, procuring_entity_id, tax_identifier):
		query = "INSERT INTO procuring_entity_tax_identifier VALUES('" + procuring_entity_id + "', '" + tax_identifier + "');"
		return query

	def insert_procuring_entity_tax_identifier_value(self, procuring_entity_id, tax_identifier_value):
		query = "INSERT INTO procuring_entity_tax_identifier_value VALUES('" + procuring_entity_id + "', '" + tax_identifier_value + "');"
		return query

	def insert_procuring_entity_registration_number(self, procuring_entity_id, registration_number):
		query = "INSERT INTO procuring_entity_registration_number VALUES('" + procuring_entity_id + "', '" + registration_number + "');"
		return query

	def insert_procuring_entity_registration_date(self, procuring_entity_id, registration_date):
		query = "INSERT INTO procuring_entity_registration_date VALUES('" + procuring_entity_id + "', '" + registration_date + "');"
		return query

	def insert_procuring_entity_status(self, procuring_entity_id, status):
		query = "INSERT INTO procuring_entity_status VALUES('" + procuring_entity_id + "', '" + status + "');"
		return query

	def insert_supplying_entity(self, supplying_entity_id):
		query = "INSERT INTO supplying_entity VALUES('" + supplying_entity_id + "');"
		return query

	def insert_supplying_entity_name(self, supplying_entity_id, name):
		query = "INSERT INTO supplying_entity_name VALUES('" + supplying_entity_id + "', '" + name + "');"
		return query

	def insert_supplying_entity_tax_identifier(self, supplying_entity_id, tax_identifier):
		query = "INSERT INTO supplying_entity_tax_identifier VALUES('" + supplying_entity_id + "', '" + tax_identifier + "');"
		return query

	def insert_supplying_entity_tax_identifier_value(self, supplying_entity_id, tax_identifier_value):
		query = "INSERT INTO supplying_entity_tax_identifier_value VALUES('" + supplying_entity_id + "', '" + tax_identifier_value + "');"
		return query

	def insert_supplying_entity_registration_number(self, supplying_entity_id, registration_number):
		query = "INSERT INTO supplying_entity_registration_number VALUES('" + supplying_entity_id + "', '" + registration_number + "');"
		return query

	def insert_supplying_entity_registration_date(self, supplying_entity_id, registration_date):
		query = "INSERT INTO supplying_entity_registration_date VALUES('" + supplying_entity_id + "', '" + registration_date + "');"
		return query

	def insert_supplying_entity_status(self, supplying_entity_id, status):
		query = "INSERT INTO supplying_entity_status VALUES('" + supplying_entity_id + "', '" + status + "');"
		return query

	def insert_address(self, address_id):
		query = "INSERT INTO address VALUES('" + address_id + "');"
		return query

	def insert_address_country(self, address_id, country):
		query = "INSERT INTO address_country VALUES('" + address_id + "', '" + country + "');"
		return query

	def insert_address_address_line_1(self, address_id, address_line_1):
		query = "INSERT INTO address_address_line_1 VALUES('" + address_id + "', '" + address_line_1 + "');"
		return query

	def insert_address_address_line_2(self, address_id, address_line_2):
		query = "INSERT INTO address_address_line_2 VALUES('" + address_id + "', '" + address_line_2 + "');"
		return query

	def insert_address_address_line_3(self, address_id, address_line_3):
		query = "INSERT INTO address_address_line_3 VALUES('" + address_id + "', '" + address_line_3 + "');"
		return query

	def insert_address_address_line_4(self, address_id, address_line_4):
		query = "INSERT INTO address_address_line_4 VALUES('" + address_id + "', '" + address_line_4 + "');"
		return query

	def insert_address_address_line_5(self, address_id, address_line_5):
		query = "INSERT INTO address_address_line_5 VALUES('" + address_id + "', '" + address_line_5 + "');"
		return query

	def insert_address_address_line_6(self, address_id, address_line_6):
		query = "INSERT INTO address_address_line_6 VALUES('" + address_id + "', '" + address_line_6 + "');"
		return query

	def insert_address_address_line_7(self, address_id, address_line_7):
		query = "INSERT INTO address_address_line_7 VALUES('" + address_id + "', '" + address_line_7 + "');"
		return query

	def insert_address_address_line_8(self, address_id, address_line_8):
		query = "INSERT INTO address_address_line_8 VALUES('" + address_id + "', '" + address_line_8 + "');"
		return query

	def insert_address_address_line_9(self, address_id, address_line_9):
		query = "INSERT INTO address_address_line_9 VALUES('" + address_id + "', '" + address_line_9 + "');"
		return query

	def insert_address_x_coord(self, address_id, x_coord):
		query = "INSERT INTO address_x_coord VALUES('" + address_id + "', " + x_coord + ");"
		return query

	def insert_address_y_coord(self, address_id, y_coord):
		query = "INSERT INTO address_y_coord VALUES('" + address_id + "', " + y_coord + ");"
		return query

	def insert_address_status(self, address_id, status):
		query = "INSERT INTO address_status VALUES('" + address_id + "', '" + status + "');"
		return query

	def insert_address_description(self, address_id, description):
		query = "INSERT INTO address_description VALUES('" + address_id + "', '" + description + "');"
		return query

	def insert_address_short_form(self, address_id, short_form):
		query = "INSERT INTO address_short_form VALUES('" + address_id + "', '" + short_form + "');"
		return query

	def insert_tender(self, tender_id):
		query = "INSERT INTO tender VALUES('" + tender_id + "');"
		return query

	def insert_tender_title(self, tender_id, title):
		query = "INSERT INTO tender_title VALUES('" + tender_id + "', '" + title + "');"
		return query

	def insert_tender_description(self, tender_id, description):
		query = "INSERT INTO tender_description VALUES('" + tender_id + "', '" + description + "');"
		return query

	def insert_tender_budget(self, tender_id, budget):
		query = "INSERT INTO tender_budget VALUES('" + tender_id + "', " + budget + ");"
		return query

	def insert_tender_status(self, tender_id, status):
		query = "INSERT INTO tender_status VALUES('" + tender_id + "', '" + status + "');"
		return query

	def insert_tender_evaluate_mechanism(self, tender_id, evaluate_mechanism):
		query = "INSERT INTO tender_evaluate_mechanism VALUES('" + tender_id + "', '" + evaluate_mechanism + "');"
		return query

	def insert_tender_publication_date_and_time(self, tender_id, publication_date_and_time):
		query = "INSERT INTO tender_publication_date_and_time VALUES('" + tender_id + "', '" + publication_date_and_time + "');"
		return query

	def insert_tender_submission_cut_off_date_and_time(self, tender_id, submission_cut_off_date_and_time):
		query = "INSERT INTO tender_submission_cut_off_date_and_time VALUES('" + tender_id + "', '" + submission_cut_off_date_and_time + "');"
		return query

	def insert_tender_award_notice_date(self, tender_id, award_notice_date):
		query = "INSERT INTO tender_award_notice_date VALUES('" + tender_id + "', '" + award_notice_date + "');"
		return query

	def insert_tender_contract_notice_date(self, tender_id, contract_notice_date):
		query = "INSERT INTO tender_contract_notice_date VALUES('" + tender_id + "', '" + contract_notice_date + "');"
		return query

	def insert_attachment(self, attachment_id):
		query = "INSERT INTO attachment VALUES('" + attachment_id + "');"
		return query

	def insert_attachment_type(self, attachment_id, type):
		query = "INSERT INTO attachment_type VALUES('" + attachment_id + "', '" + type + "');"
		return query

	def insert_attachment_name(self, attachment_id, name):
		query = "INSERT INTO attachment_name VALUES('" + attachment_id + "', '" + name + "');"
		return query

	def insert_attachment_description(self, attachment_id, description):
		query = "INSERT INTO attachment_description VALUES('" + attachment_id + "', '" + description + "');"
		return query

	def insert_attachment_link(self, attachment_id, link):
		query = "INSERT INTO attachment_link VALUES('" + attachment_id + "', '" + link + "');"
		return query

	def insert_award(self, award_id):
		query = "INSERT INTO award VALUES('" + award_id + "');"
		return query

	def insert_award_is_accepted(self, award_id, is_accepted):
		query = "INSERT INTO award_is_accepted VALUES('" + award_id + "', " + is_accepted + ");"
		return query

	def insert_award_date_replied(self, award_id, date_replied):
		query = "INSERT INTO award_date_replied VALUES('" + award_id + "', '" + date_replied + "');"
		return query

	def insert_award_reply_reason(self, award_id, reply_reason):
		query = "INSERT INTO award_reply_reason VALUES('" + award_id + "', '" + reply_reason + "');"
		return query

	def insert_award_award_amount(self, award_id, award_amount):
		query = "INSERT INTO award_award_amount VALUES('" + award_id + "', " + award_amount + ");"
		return query

	def insert_contact(self, contact_id):
		query = "INSERT INTO contact VALUES('" + contact_id + "');"
		return query

	def insert_contact_name(self, contact_id, name):
		query = "INSERT INTO contact_name VALUES('" + contact_id + "', '" + name + "');"
		return query

	def insert_contact_value(self, contact_id, value):
		query = "INSERT INTO contact_value VALUES('" + contact_id + "', '" + value + "');"
		return query

	def insert_contact_status(self, contact_id, status):
		query = "INSERT INTO contact_status VALUES('" + contact_id + "', '" + status + "');"
		return query

	def insert_contract(self, contract_id):
		query = "INSERT INTO contract VALUES('" + contract_id + "');"
		return query

	def insert_contract_title(self, contract_id, title):
		query = "INSERT INTO contract_title VALUES('" + contract_id + "', '" + title + "');"
		return query

	def insert_contract_amount(self, contract_id, amount):
		query = "INSERT INTO contract_amount VALUES('" + contract_id + "', " + amount + ");"
		return query

	def insert_contract_status(self, contract_id, status):
		query = "INSERT INTO contract_status VALUES('" + contract_id + "', '" + status + "');"
		return query

	def insert_contract_description(self, contract_id, description):
		query = "INSERT INTO contract_description VALUES('" + contract_id + "', '" + description + "');"
		return query

	def insert_fee(self, fee_id):
		query = "INSERT INTO fee VALUES('" + fee_id + "');"
		return query

	def insert_fee_name(self, fee_id, name):
		query = "INSERT INTO fee_name VALUES('" + fee_id + "', '" + name + "');"
		return query

	def insert_fee_amount(self, fee_id, amount):
		query = "INSERT INTO fee_amount VALUES('" + fee_id + "', " + amount + ");"
		return query

	def insert_fee_type(self, fee_id, type):
		query = "INSERT INTO fee_type VALUES('" + fee_id + "', '" + type + "');"
		return query

	def insert_payment(self, payment_id):
		query = "INSERT INTO payment VALUES('" + payment_id + "');"
		return query

	def insert_payment_transaction_id(self, payment_id, transaction_id):
		query = "INSERT INTO payment_transaction_id VALUES('" + payment_id + "', '" + transaction_id + "');"
		return query

	def insert_payment_date_received(self, payment_id, date_received):
		query = "INSERT INTO payment_date_received VALUES('" + payment_id + "', '" + date_received + "');"
		return query

	def insert_payment_amount(self, payment_id, amount):
		query = "INSERT INTO payment_amount VALUES('" + payment_id + "', " + amount + ");"
		return query

	def insert_payment_currency(self, payment_id, currency):
		query = "INSERT INTO payment_currency VALUES('" + payment_id + "', '" + currency + "');"
		return query

	def insert_payment_status(self, payment_id, status):
		query = "INSERT INTO payment_status VALUES('" + payment_id + "', '" + status + "');"
		return query

	def insert_payment_extra_information(self, payment_id, extra_information):
		query = "INSERT INTO payment_extra_information VALUES('" + payment_id + "', '" + extra_information + "');"
		return query

	def insert_plan(self, plan_id):
		query = "INSERT INTO plan VALUES('" + plan_id + "');"
		return query

	def insert_plan_budget(self, plan_id, budget):
		query = "INSERT INTO plan_budget VALUES('" + plan_id + "', " + budget + ");"
		return query

	def insert_plan_submission_date_and_time(self, plan_id, submission_date_and_time):
		query = "INSERT INTO plan_submission_date_and_time VALUES('" + plan_id + "', '" + submission_date_and_time + "');"
		return query

	def insert_plan_description(self, plan_id, description):
		query = "INSERT INTO plan_description VALUES('" + plan_id + "', '" + description + "');"
		return query

	def insert_alert(self, alert_id):
		query = "INSERT INTO alert VALUES('" + alert_id + "');"
		return query

	def insert_alert_subject(self, alert_id, subject):
		query = "INSERT INTO alert_subject VALUES('" + alert_id + "', '" + subject + "');"
		return query

	def insert_alert_description(self, alert_id, description):
		query = "INSERT INTO alert_description VALUES('" + alert_id + "', '" + description + "');"
		return query

	def insert_alert_authority(self, alert_authority_id):
		query = "INSERT INTO alert_authority VALUES('" + alert_authority_id + "');"
		return query

	def insert_alert_authority_name(self, alert_authority_id, name):
		query = "INSERT INTO alert_authority_name VALUES('" + alert_authority_id + "', '" + name + "');"
		return query

	def insert_alert_authority_description(self, alert_authority_id, description):
		query = "INSERT INTO alert_authority_description VALUES('" + alert_authority_id + "', '" + description + "');"
		return query

	def insert_alert_level(self, alert_level_id):
		query = "INSERT INTO alert_level VALUES('" + alert_level_id + "');"
		return query

	def insert_alert_level_name(self, alert_level_id, name):
		query = "INSERT INTO alert_level_name VALUES('" + alert_level_id + "', '" + name + "');"
		return query

	def insert_alert_level_description(self, alert_level_id, description):
		query = "INSERT INTO alert_level_description VALUES('" + alert_level_id + "', '" + description + "');"
		return query

	def insert_user_account(self, user_account_id):
		query = "INSERT INTO user_account VALUES('" + user_account_id + "');"
		return query

	def insert_user_account_national_id_number(self, user_account_id, national_id_number):
		query = "INSERT INTO user_account_national_id_number VALUES('" + user_account_id + "', '" + national_id_number + "');"
		return query

	def insert_user_account_category(self, user_account_id, category):
		query = "INSERT INTO user_account_category VALUES('" + user_account_id + "', '" + category + "');"
		return query

	def insert_user_account_first_name(self, user_account_id, first_name):
		query = "INSERT INTO user_account_first_name VALUES('" + user_account_id + "', '" + first_name + "');"
		return query

	def insert_user_account_last_name(self, user_account_id, last_name):
		query = "INSERT INTO user_account_last_name VALUES('" + user_account_id + "', '" + last_name + "');"
		return query

	def insert_user_account_other_names(self, user_account_id, other_names):
		query = "INSERT INTO user_account_other_names VALUES('" + user_account_id + "', '" + other_names + "');"
		return query

	def insert_user_account_date_of_birth(self, user_account_id, date_of_birth):
		query = "INSERT INTO user_account_date_of_birth VALUES('" + user_account_id + "', '" + date_of_birth + "');"
		return query

	def insert_user_account_gender(self, user_account_id, gender):
		query = "INSERT INTO user_account_gender VALUES('" + user_account_id + "', '" + gender + "');"
		return query

	def insert_user_account_status(self, user_account_id, status):
		query = "INSERT INTO user_account_status VALUES('" + user_account_id + "', '" + status + "');"
		return query

	def insert_user_account_email(self, user_account_id, email):
		query = "INSERT INTO user_account_email VALUES('" + user_account_id + "', '" + email + "');"
		return query

	def insert_user_account_password(self, user_account_id, password):
		query = "INSERT INTO user_account_password VALUES('" + user_account_id + "', '" + password + "');"
		return query

	def insert_user_account_photo(self, user_account_id, photo):
		query = "INSERT INTO user_account_photo VALUES('" + user_account_id + "', '" + photo + "');"
		return query

	def insert_appeal(self, appeal_id):
		query = "INSERT INTO appeal VALUES('" + appeal_id + "');"
		return query

	def insert_appeal_subject(self, appeal_id, subject):
		query = "INSERT INTO appeal_subject VALUES('" + appeal_id + "', '" + subject + "');"
		return query

	def insert_appeal_description(self, appeal_id, description):
		query = "INSERT INTO appeal_description VALUES('" + appeal_id + "', '" + description + "');"
		return query

	def insert_countryfiscal_yearmap(self, key_column, country_id, fiscal_year_id):
		query = "INSERT INTO countryfiscal_yearmap VALUES('" + key_column + "', '" + country_id + "', '" + fiscal_year_id + "');"
		return query

	def insert_countryprocurement_stagemap(self, key_column, country_id, procurement_stage_id):
		query = "INSERT INTO countryprocurement_stagemap VALUES('" + key_column + "', '" + country_id + "', '" + procurement_stage_id + "');"
		return query

	def insert_countryprocurement_typemap(self, key_column, country_id, procurement_type_id):
		query = "INSERT INTO countryprocurement_typemap VALUES('" + key_column + "', '" + country_id + "', '" + procurement_type_id + "');"
		return query

	def insert_countryprocurement_methodmap(self, key_column, country_id, procurement_method_id):
		query = "INSERT INTO countryprocurement_methodmap VALUES('" + key_column + "', '" + country_id + "', '" + procurement_method_id + "');"
		return query

	def insert_countryprocuring_entitymap(self, key_column, country_id, procuring_entity_id):
		query = "INSERT INTO countryprocuring_entitymap VALUES('" + key_column + "', '" + country_id + "', '" + procuring_entity_id + "');"
		return query

	def insert_countrysupplying_entitymap(self, key_column, country_id, supplying_entity_id):
		query = "INSERT INTO countrysupplying_entitymap VALUES('" + key_column + "', '" + country_id + "', '" + supplying_entity_id + "');"
		return query

	def insert_countryred_flagmap(self, key_column, country_id, red_flag_id):
		query = "INSERT INTO countryred_flagmap VALUES('" + key_column + "', '" + country_id + "', '" + red_flag_id + "');"
		return query

	def insert_countryillicit_schememap(self, key_column, country_id, illicit_scheme_id):
		query = "INSERT INTO countryillicit_schememap VALUES('" + key_column + "', '" + country_id + "', '" + illicit_scheme_id + "');"
		return query

	def insert_fiscal_yeartendermap(self, key_column, fiscal_year_id, tender_id):
		query = "INSERT INTO fiscal_yeartendermap VALUES('" + key_column + "', '" + fiscal_year_id + "', '" + tender_id + "');"
		return query

	def insert_fiscal_yearillicit_schememap(self, key_column, fiscal_year_id, illicit_scheme_id):
		query = "INSERT INTO fiscal_yearillicit_schememap VALUES('" + key_column + "', '" + fiscal_year_id + "', '" + illicit_scheme_id + "');"
		return query

	def insert_fiscal_yearred_flagmap(self, key_column, fiscal_year_id, red_flag_id):
		query = "INSERT INTO fiscal_yearred_flagmap VALUES('" + key_column + "', '" + fiscal_year_id + "', '" + red_flag_id + "');"
		return query

	def insert_fiscal_yearprocurement_stagemap(self, key_column, fiscal_year_id, procurement_stage_id):
		query = "INSERT INTO fiscal_yearprocurement_stagemap VALUES('" + key_column + "', '" + fiscal_year_id + "', '" + procurement_stage_id + "');"
		return query

	def insert_fiscal_yearprocurement_typemap(self, key_column, fiscal_year_id, procurement_type_id):
		query = "INSERT INTO fiscal_yearprocurement_typemap VALUES('" + key_column + "', '" + fiscal_year_id + "', '" + procurement_type_id + "');"
		return query

	def insert_fiscal_yearprocurement_methodmap(self, key_column, fiscal_year_id, procurement_method_id):
		query = "INSERT INTO fiscal_yearprocurement_methodmap VALUES('" + key_column + "', '" + fiscal_year_id + "', '" + procurement_method_id + "');"
		return query

	def insert_fiscal_yearbidmap(self, key_column, fiscal_year_id, bid_id):
		query = "INSERT INTO fiscal_yearbidmap VALUES('" + key_column + "', '" + fiscal_year_id + "', '" + bid_id + "');"
		return query

	def insert_fiscal_yearitemmap(self, key_column, fiscal_year_id, item_id):
		query = "INSERT INTO fiscal_yearitemmap VALUES('" + key_column + "', '" + fiscal_year_id + "', '" + item_id + "');"
		return query

	def insert_fiscal_yearcontractmap(self, key_column, fiscal_year_id, contract_id):
		query = "INSERT INTO fiscal_yearcontractmap VALUES('" + key_column + "', '" + fiscal_year_id + "', '" + contract_id + "');"
		return query

	def insert_fiscal_yearconfigurationmap(self, key_column, fiscal_year_id, configuration_id):
		query = "INSERT INTO fiscal_yearconfigurationmap VALUES('" + key_column + "', '" + fiscal_year_id + "', '" + configuration_id + "');"
		return query

	def insert_fiscal_yearfeemap(self, key_column, fiscal_year_id, fee_id):
		query = "INSERT INTO fiscal_yearfeemap VALUES('" + key_column + "', '" + fiscal_year_id + "', '" + fee_id + "');"
		return query

	def insert_fiscal_yearprocuring_entitymap(self, key_column, fiscal_year_id, procuring_entity_id):
		query = "INSERT INTO fiscal_yearprocuring_entitymap VALUES('" + key_column + "', '" + fiscal_year_id + "', '" + procuring_entity_id + "');"
		return query

	def insert_fiscal_yearsupplying_entitymap(self, key_column, fiscal_year_id, supplying_entity_id):
		query = "INSERT INTO fiscal_yearsupplying_entitymap VALUES('" + key_column + "', '" + fiscal_year_id + "', '" + supplying_entity_id + "');"
		return query

	def insert_fiscal_yearawardmap(self, key_column, fiscal_year_id, award_id):
		query = "INSERT INTO fiscal_yearawardmap VALUES('" + key_column + "', '" + fiscal_year_id + "', '" + award_id + "');"
		return query

	def insert_fiscal_yearplanmap(self, key_column, fiscal_year_id, plan_id):
		query = "INSERT INTO fiscal_yearplanmap VALUES('" + key_column + "', '" + fiscal_year_id + "', '" + plan_id + "');"
		return query

	def insert_red_flagconfigurationmap(self, key_column, red_flag_id, configuration_id):
		query = "INSERT INTO red_flagconfigurationmap VALUES('" + key_column + "', '" + red_flag_id + "', '" + configuration_id + "');"
		return query

	def insert_procurement_stagered_flagmap(self, key_column, procurement_stage_id, red_flag_id):
		query = "INSERT INTO procurement_stagered_flagmap VALUES('" + key_column + "', '" + procurement_stage_id + "', '" + red_flag_id + "');"
		return query

	def insert_procuring_entityred_flagmap(self, key_column, procuring_entity_id, red_flag_id):
		query = "INSERT INTO procuring_entityred_flagmap VALUES('" + key_column + "', '" + procuring_entity_id + "', '" + red_flag_id + "');"
		return query

	def insert_supplying_entityred_flagmap(self, key_column, supplying_entity_id, red_flag_id):
		query = "INSERT INTO supplying_entityred_flagmap VALUES('" + key_column + "', '" + supplying_entity_id + "', '" + red_flag_id + "');"
		return query

	def insert_procurement_typered_flagmap(self, key_column, procurement_type_id, red_flag_id):
		query = "INSERT INTO procurement_typered_flagmap VALUES('" + key_column + "', '" + procurement_type_id + "', '" + red_flag_id + "');"
		return query

	def insert_procurement_methodred_flagmap(self, key_column, procurement_method_id, red_flag_id):
		query = "INSERT INTO procurement_methodred_flagmap VALUES('" + key_column + "', '" + procurement_method_id + "', '" + red_flag_id + "');"
		return query

	def insert_tenderred_flagmap(self, key_column, tender_id, red_flag_id):
		query = "INSERT INTO tenderred_flagmap VALUES('" + key_column + "', '" + tender_id + "', '" + red_flag_id + "');"
		return query

	def insert_bidred_flagmap(self, key_column, bid_id, red_flag_id):
		query = "INSERT INTO bidred_flagmap VALUES('" + key_column + "', '" + bid_id + "', '" + red_flag_id + "');"
		return query

	def insert_itemred_flagmap(self, key_column, item_id, red_flag_id):
		query = "INSERT INTO itemred_flagmap VALUES('" + key_column + "', '" + item_id + "', '" + red_flag_id + "');"
		return query

	def insert_contractred_flagmap(self, key_column, contract_id, red_flag_id):
		query = "INSERT INTO contractred_flagmap VALUES('" + key_column + "', '" + contract_id + "', '" + red_flag_id + "');"
		return query

	def insert_illicit_schemered_flagmap(self, key_column, illicit_scheme_id, red_flag_id):
		query = "INSERT INTO illicit_schemered_flagmap VALUES('" + key_column + "', '" + illicit_scheme_id + "', '" + red_flag_id + "');"
		return query

	def insert_bidfeemap(self, key_column, bid_id, fee_id):
		query = "INSERT INTO bidfeemap VALUES('" + key_column + "', '" + bid_id + "', '" + fee_id + "');"
		return query

	def insert_bidpaymentmap(self, key_column, bid_id, payment_id):
		query = "INSERT INTO bidpaymentmap VALUES('" + key_column + "', '" + bid_id + "', '" + payment_id + "');"
		return query

	def insert_bidawardmap(self, key_column, bid_id, award_id):
		query = "INSERT INTO bidawardmap VALUES('" + key_column + "', '" + bid_id + "', '" + award_id + "');"
		return query

	def insert_tenderbidmap(self, key_column, tender_id, bid_id):
		query = "INSERT INTO tenderbidmap VALUES('" + key_column + "', '" + tender_id + "', '" + bid_id + "');"
		return query

	def insert_tenderfeemap(self, key_column, tender_id, fee_id):
		query = "INSERT INTO tenderfeemap VALUES('" + key_column + "', '" + tender_id + "', '" + fee_id + "');"
		return query

	def insert_tenderpaymentmap(self, key_column, tender_id, payment_id):
		query = "INSERT INTO tenderpaymentmap VALUES('" + key_column + "', '" + tender_id + "', '" + payment_id + "');"
		return query

	def insert_awardappealmap(self, key_column, award_id, appeal_id):
		query = "INSERT INTO awardappealmap VALUES('" + key_column + "', '" + award_id + "', '" + appeal_id + "');"
		return query

	def insert_procuring_entityprocurement_typemap(self, key_column, procuring_entity_id, procurement_type_id):
		query = "INSERT INTO procuring_entityprocurement_typemap VALUES('" + key_column + "', '" + procuring_entity_id + "', '" + procurement_type_id + "');"
		return query

	def insert_procuring_entityprocurement_methodmap(self, key_column, procuring_entity_id, procurement_method_id):
		query = "INSERT INTO procuring_entityprocurement_methodmap VALUES('" + key_column + "', '" + procuring_entity_id + "', '" + procurement_method_id + "');"
		return query

	def insert_procuring_entityprocurement_stagemap(self, key_column, procuring_entity_id, procurement_stage_id):
		query = "INSERT INTO procuring_entityprocurement_stagemap VALUES('" + key_column + "', '" + procuring_entity_id + "', '" + procurement_stage_id + "');"
		return query

	def insert_procuring_entitybidmap(self, key_column, procuring_entity_id, bid_id):
		query = "INSERT INTO procuring_entitybidmap VALUES('" + key_column + "', '" + procuring_entity_id + "', '" + bid_id + "');"
		return query

	def insert_procuring_entitytendermap(self, key_column, procuring_entity_id, tender_id):
		query = "INSERT INTO procuring_entitytendermap VALUES('" + key_column + "', '" + procuring_entity_id + "', '" + tender_id + "');"
		return query

	def insert_procuring_entitycontractmap(self, key_column, procuring_entity_id, contract_id):
		query = "INSERT INTO procuring_entitycontractmap VALUES('" + key_column + "', '" + procuring_entity_id + "', '" + contract_id + "');"
		return query

	def insert_procuring_entityillicit_schememap(self, key_column, procuring_entity_id, illicit_scheme_id):
		query = "INSERT INTO procuring_entityillicit_schememap VALUES('" + key_column + "', '" + procuring_entity_id + "', '" + illicit_scheme_id + "');"
		return query

	def insert_procuring_entityaddressmap(self, key_column, procuring_entity_id, address_id):
		query = "INSERT INTO procuring_entityaddressmap VALUES('" + key_column + "', '" + procuring_entity_id + "', '" + address_id + "');"
		return query

	def insert_procuring_entityattachmentmap(self, key_column, procuring_entity_id, attachment_id):
		query = "INSERT INTO procuring_entityattachmentmap VALUES('" + key_column + "', '" + procuring_entity_id + "', '" + attachment_id + "');"
		return query

	def insert_procuring_entityplanmap(self, key_column, procuring_entity_id, plan_id):
		query = "INSERT INTO procuring_entityplanmap VALUES('" + key_column + "', '" + procuring_entity_id + "', '" + plan_id + "');"
		return query

	def insert_procuring_entityawardmap(self, key_column, procuring_entity_id, award_id):
		query = "INSERT INTO procuring_entityawardmap VALUES('" + key_column + "', '" + procuring_entity_id + "', '" + award_id + "');"
		return query

	def insert_procuring_entitycontactmap(self, key_column, procuring_entity_id, contact_id):
		query = "INSERT INTO procuring_entitycontactmap VALUES('" + key_column + "', '" + procuring_entity_id + "', '" + contact_id + "');"
		return query

	def insert_procuring_entitypaymentmap(self, key_column, procuring_entity_id, payment_id):
		query = "INSERT INTO procuring_entitypaymentmap VALUES('" + key_column + "', '" + procuring_entity_id + "', '" + payment_id + "');"
		return query

	def insert_procuring_entityuser_accountmap(self, key_column, procuring_entity_id, user_account_id):
		query = "INSERT INTO procuring_entityuser_accountmap VALUES('" + key_column + "', '" + procuring_entity_id + "', '" + user_account_id + "');"
		return query

	def insert_procuring_entitysupplying_entitymap(self, key_column, procuring_entity_id, supplying_entity_id):
		query = "INSERT INTO procuring_entitysupplying_entitymap VALUES('" + key_column + "', '" + procuring_entity_id + "', '" + supplying_entity_id + "');"
		return query

	def insert_supplying_entityprocurement_typemap(self, key_column, supplying_entity_id, procurement_type_id):
		query = "INSERT INTO supplying_entityprocurement_typemap VALUES('" + key_column + "', '" + supplying_entity_id + "', '" + procurement_type_id + "');"
		return query

	def insert_supplying_entityprocurement_methodmap(self, key_column, supplying_entity_id, procurement_method_id):
		query = "INSERT INTO supplying_entityprocurement_methodmap VALUES('" + key_column + "', '" + supplying_entity_id + "', '" + procurement_method_id + "');"
		return query

	def insert_supplying_entityprocurement_stagemap(self, key_column, supplying_entity_id, procurement_stage_id):
		query = "INSERT INTO supplying_entityprocurement_stagemap VALUES('" + key_column + "', '" + supplying_entity_id + "', '" + procurement_stage_id + "');"
		return query

	def insert_supplying_entitybidmap(self, key_column, supplying_entity_id, bid_id):
		query = "INSERT INTO supplying_entitybidmap VALUES('" + key_column + "', '" + supplying_entity_id + "', '" + bid_id + "');"
		return query

	def insert_supplying_entitytendermap(self, key_column, supplying_entity_id, tender_id):
		query = "INSERT INTO supplying_entitytendermap VALUES('" + key_column + "', '" + supplying_entity_id + "', '" + tender_id + "');"
		return query

	def insert_supplying_entitycontractmap(self, key_column, supplying_entity_id, contract_id):
		query = "INSERT INTO supplying_entitycontractmap VALUES('" + key_column + "', '" + supplying_entity_id + "', '" + contract_id + "');"
		return query

	def insert_supplying_entityillicit_schememap(self, key_column, supplying_entity_id, illicit_scheme_id):
		query = "INSERT INTO supplying_entityillicit_schememap VALUES('" + key_column + "', '" + supplying_entity_id + "', '" + illicit_scheme_id + "');"
		return query

	def insert_supplying_entityaddressmap(self, key_column, supplying_entity_id, address_id):
		query = "INSERT INTO supplying_entityaddressmap VALUES('" + key_column + "', '" + supplying_entity_id + "', '" + address_id + "');"
		return query

	def insert_supplying_entityattachmentmap(self, key_column, supplying_entity_id, attachment_id):
		query = "INSERT INTO supplying_entityattachmentmap VALUES('" + key_column + "', '" + supplying_entity_id + "', '" + attachment_id + "');"
		return query

	def insert_supplying_entityawardmap(self, key_column, supplying_entity_id, award_id):
		query = "INSERT INTO supplying_entityawardmap VALUES('" + key_column + "', '" + supplying_entity_id + "', '" + award_id + "');"
		return query

	def insert_supplying_entitycontactmap(self, key_column, supplying_entity_id, contact_id):
		query = "INSERT INTO supplying_entitycontactmap VALUES('" + key_column + "', '" + supplying_entity_id + "', '" + contact_id + "');"
		return query

	def insert_supplying_entitypaymentmap(self, key_column, supplying_entity_id, payment_id):
		query = "INSERT INTO supplying_entitypaymentmap VALUES('" + key_column + "', '" + supplying_entity_id + "', '" + payment_id + "');"
		return query

	def insert_supplying_entityuser_accountmap(self, key_column, supplying_entity_id, user_account_id):
		query = "INSERT INTO supplying_entityuser_accountmap VALUES('" + key_column + "', '" + supplying_entity_id + "', '" + user_account_id + "');"
		return query

	def insert_contractawardmap(self, key_column, contract_id, award_id):
		query = "INSERT INTO contractawardmap VALUES('" + key_column + "', '" + contract_id + "', '" + award_id + "');"
		return query

	def insert_paymentfeemap(self, key_column, payment_id, fee_id):
		query = "INSERT INTO paymentfeemap VALUES('" + key_column + "', '" + payment_id + "', '" + fee_id + "');"
		return query

	def insert_alert_authorityuser_accountmap(self, key_column, alert_authority_id, user_account_id):
		query = "INSERT INTO alert_authorityuser_accountmap VALUES('" + key_column + "', '" + alert_authority_id + "', '" + user_account_id + "');"
		return query

	def insert_alert_authorityalert_levelmap(self, key_column, alert_authority_id, alert_level_id):
		query = "INSERT INTO alert_authorityalert_levelmap VALUES('" + key_column + "', '" + alert_authority_id + "', '" + alert_level_id + "');"
		return query

	def insert_alert_authorityalertmap(self, key_column, alert_authority_id, alert_id):
		query = "INSERT INTO alert_authorityalertmap VALUES('" + key_column + "', '" + alert_authority_id + "', '" + alert_id + "');"
		return query

	def insert_alert_authorityaddressmap(self, key_column, alert_authority_id, address_id):
		query = "INSERT INTO alert_authorityaddressmap VALUES('" + key_column + "', '" + alert_authority_id + "', '" + address_id + "');"
		return query

	def insert_alert_leveluser_accountmap(self, key_column, alert_level_id, user_account_id):
		query = "INSERT INTO alert_leveluser_accountmap VALUES('" + key_column + "', '" + alert_level_id + "', '" + user_account_id + "');"
		return query

	def insert_alert_levelred_flagmap(self, key_column, alert_level_id, red_flag_id):
		query = "INSERT INTO alert_levelred_flagmap VALUES('" + key_column + "', '" + alert_level_id + "', '" + red_flag_id + "');"
		return query

	def insert_alert_leveladdressmap(self, key_column, alert_level_id, address_id):
		query = "INSERT INTO alert_leveladdressmap VALUES('" + key_column + "', '" + alert_level_id + "', '" + address_id + "');"
		return query

	def insert_alertred_flagmap(self, key_column, alert_id, red_flag_id):
		query = "INSERT INTO alertred_flagmap VALUES('" + key_column + "', '" + alert_id + "', '" + red_flag_id + "');"
		return query

	def insert_alertattachmentmap(self, key_column, alert_id, attachment_id):
		query = "INSERT INTO alertattachmentmap VALUES('" + key_column + "', '" + alert_id + "', '" + attachment_id + "');"
		return query

	def insert_alert_authoritycontactmap(self, key_column, alert_authority_id, contact_id):
		query = "INSERT INTO alert_authoritycontactmap VALUES('" + key_column + "', '" + alert_authority_id + "', '" + contact_id + "');"
		return query

	def insert_alert_levelcontactmap(self, key_column, alert_level_id, contact_id):
		query = "INSERT INTO alert_levelcontactmap VALUES('" + key_column + "', '" + alert_level_id + "', '" + contact_id + "');"
		return query

	def insert_user_accountcontactmap(self, key_column, user_account_id, contact_id):
		query = "INSERT INTO user_accountcontactmap VALUES('" + key_column + "', '" + user_account_id + "', '" + contact_id + "');"
		return query

	def insert_user_accountaddressmap(self, key_column, user_account_id, address_id):
		query = "INSERT INTO user_accountaddressmap VALUES('" + key_column + "', '" + user_account_id + "', '" + address_id + "');"
		return query

	def insert_user_accountsubmissionmap(self, key_column, user_account_id, submission_id):
		query = "INSERT INTO user_accountsubmissionmap VALUES('" + key_column + "', '" + user_account_id + "', '" + submission_id + "');"
		return query

	def insert_procurement_stagesubmissionmap(self, key_column, procurement_stage_id, submission_id):
		query = "INSERT INTO procurement_stagesubmissionmap VALUES('" + key_column + "', '" + procurement_stage_id + "', '" + submission_id + "');"
		return query

	def insert_plansubmissionmap(self, key_column, plan_id, submission_id):
		query = "INSERT INTO plansubmissionmap VALUES('" + key_column + "', '" + plan_id + "', '" + submission_id + "');"
		return query

	def insert_submissionattachmentmap(self, key_column, submission_id, attachment_id):
		query = "INSERT INTO submissionattachmentmap VALUES('" + key_column + "', '" + submission_id + "', '" + attachment_id + "');"
		return query

	def insert_appealattachmentmap(self, key_column, appeal_id, attachment_id):
		query = "INSERT INTO appealattachmentmap VALUES('" + key_column + "', '" + appeal_id + "', '" + attachment_id + "');"
		return query

	def insert_user_accountattachmentmap(self, key_column, user_account_id, attachment_id):
		query = "INSERT INTO user_accountattachmentmap VALUES('" + key_column + "', '" + user_account_id + "', '" + attachment_id + "');"
		return query

	def insert_awardsubmissionmap(self, key_column, award_id, submission_id):
		query = "INSERT INTO awardsubmissionmap VALUES('" + key_column + "', '" + award_id + "', '" + submission_id + "');"
		return query

	def insert_user_accountplanmap(self, key_column, user_account_id, plan_id):
		query = "INSERT INTO user_accountplanmap VALUES('" + key_column + "', '" + user_account_id + "', '" + plan_id + "');"
		return query

	def insert_awardtendermap(self, key_column, award_id, tender_id):
		query = "INSERT INTO awardtendermap VALUES('" + key_column + "', '" + award_id + "', '" + tender_id + "');"
		return query

	def insert_bidsubmissionmap(self, key_column, bid_id, submission_id):
		query = "INSERT INTO bidsubmissionmap VALUES('" + key_column + "', '" + bid_id + "', '" + submission_id + "');"
		return query

	def insert_tenderappealmap(self, key_column, tender_id, appeal_id):
		query = "INSERT INTO tenderappealmap VALUES('" + key_column + "', '" + tender_id + "', '" + appeal_id + "');"
		return query




