


class Delete:

	def  __init__(self, instance_name):
		self.instance_name = instance_name

	def  __str__(self):
		return self.instance_name


	def delete_from_country(self):
		query = "DELETE FROM country;"
		return query

	def delete_country(self, country_id):
		query = "DELETE FROM country WHERE country_id  =  '" + country_id + "';"
		return query

	def delete_from_country_code(self):
		query = "DELETE FROM country_code;"
		return query

	def delete_country_code(self, country_id):
		query = "DELETE FROM country_code WHERE country_id  =  '" + country_id + "';"
		return query

	def delete_from_country_name(self):
		query = "DELETE FROM country_name;"
		return query

	def delete_country_name(self, country_id):
		query = "DELETE FROM country_name WHERE country_id  =  '" + country_id + "';"
		return query

	def delete_from_country_currency(self):
		query = "DELETE FROM country_currency;"
		return query

	def delete_country_currency(self, country_id):
		query = "DELETE FROM country_currency WHERE country_id  =  '" + country_id + "';"
		return query

	def delete_from_country_flag(self):
		query = "DELETE FROM country_flag;"
		return query

	def delete_country_flag(self, country_id):
		query = "DELETE FROM country_flag WHERE country_id  =  '" + country_id + "';"
		return query

	def delete_from_country_coat_of_arms(self):
		query = "DELETE FROM country_coat_of_arms;"
		return query

	def delete_country_coat_of_arms(self, country_id):
		query = "DELETE FROM country_coat_of_arms WHERE country_id  =  '" + country_id + "';"
		return query

	def delete_from_fiscal_year(self):
		query = "DELETE FROM fiscal_year;"
		return query

	def delete_fiscal_year(self, fiscal_year_id):
		query = "DELETE FROM fiscal_year WHERE fiscal_year_id  =  '" + fiscal_year_id + "';"
		return query

	def delete_from_fiscal_year_start_date(self):
		query = "DELETE FROM fiscal_year_start_date;"
		return query

	def delete_fiscal_year_start_date(self, fiscal_year_id):
		query = "DELETE FROM fiscal_year_start_date WHERE fiscal_year_id  =  '" + fiscal_year_id + "';"
		return query

	def delete_from_fiscal_year_end_date(self):
		query = "DELETE FROM fiscal_year_end_date;"
		return query

	def delete_fiscal_year_end_date(self, fiscal_year_id):
		query = "DELETE FROM fiscal_year_end_date WHERE fiscal_year_id  =  '" + fiscal_year_id + "';"
		return query

	def delete_from_configuration(self):
		query = "DELETE FROM configuration;"
		return query

	def delete_configuration(self, configuration_id):
		query = "DELETE FROM configuration WHERE configuration_id  =  '" + configuration_id + "';"
		return query

	def delete_from_configuration_name(self):
		query = "DELETE FROM configuration_name;"
		return query

	def delete_configuration_name(self, configuration_id):
		query = "DELETE FROM configuration_name WHERE configuration_id  =  '" + configuration_id + "';"
		return query

	def delete_from_configuration_description(self):
		query = "DELETE FROM configuration_description;"
		return query

	def delete_configuration_description(self, configuration_id):
		query = "DELETE FROM configuration_description WHERE configuration_id  =  '" + configuration_id + "';"
		return query

	def delete_from_configuration_value(self):
		query = "DELETE FROM configuration_value;"
		return query

	def delete_configuration_value(self, configuration_id):
		query = "DELETE FROM configuration_value WHERE configuration_id  =  '" + configuration_id + "';"
		return query

	def delete_from_configuration_status(self):
		query = "DELETE FROM configuration_status;"
		return query

	def delete_configuration_status(self, configuration_id):
		query = "DELETE FROM configuration_status WHERE configuration_id  =  '" + configuration_id + "';"
		return query

	def delete_from_red_flag(self):
		query = "DELETE FROM red_flag;"
		return query

	def delete_red_flag(self, red_flag_id):
		query = "DELETE FROM red_flag WHERE red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_from_red_flag_name(self):
		query = "DELETE FROM red_flag_name;"
		return query

	def delete_red_flag_name(self, red_flag_id):
		query = "DELETE FROM red_flag_name WHERE red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_from_red_flag_description(self):
		query = "DELETE FROM red_flag_description;"
		return query

	def delete_red_flag_description(self, red_flag_id):
		query = "DELETE FROM red_flag_description WHERE red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_from_red_flag_status(self):
		query = "DELETE FROM red_flag_status;"
		return query

	def delete_red_flag_status(self, red_flag_id):
		query = "DELETE FROM red_flag_status WHERE red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_from_illicit_scheme(self):
		query = "DELETE FROM illicit_scheme;"
		return query

	def delete_illicit_scheme(self, illicit_scheme_id):
		query = "DELETE FROM illicit_scheme WHERE illicit_scheme_id  =  '" + illicit_scheme_id + "';"
		return query

	def delete_from_illicit_scheme_name(self):
		query = "DELETE FROM illicit_scheme_name;"
		return query

	def delete_illicit_scheme_name(self, illicit_scheme_id):
		query = "DELETE FROM illicit_scheme_name WHERE illicit_scheme_id  =  '" + illicit_scheme_id + "';"
		return query

	def delete_from_illicit_scheme_description(self):
		query = "DELETE FROM illicit_scheme_description;"
		return query

	def delete_illicit_scheme_description(self, illicit_scheme_id):
		query = "DELETE FROM illicit_scheme_description WHERE illicit_scheme_id  =  '" + illicit_scheme_id + "';"
		return query

	def delete_from_procurement_stage(self):
		query = "DELETE FROM procurement_stage;"
		return query

	def delete_procurement_stage(self, procurement_stage_id):
		query = "DELETE FROM procurement_stage WHERE procurement_stage_id  =  '" + procurement_stage_id + "';"
		return query

	def delete_from_procurement_stage_name(self):
		query = "DELETE FROM procurement_stage_name;"
		return query

	def delete_procurement_stage_name(self, procurement_stage_id):
		query = "DELETE FROM procurement_stage_name WHERE procurement_stage_id  =  '" + procurement_stage_id + "';"
		return query

	def delete_from_procurement_stage_description(self):
		query = "DELETE FROM procurement_stage_description;"
		return query

	def delete_procurement_stage_description(self, procurement_stage_id):
		query = "DELETE FROM procurement_stage_description WHERE procurement_stage_id  =  '" + procurement_stage_id + "';"
		return query

	def delete_from_submission(self):
		query = "DELETE FROM submission;"
		return query

	def delete_submission(self, submission_id):
		query = "DELETE FROM submission WHERE submission_id  =  '" + submission_id + "';"
		return query

	def delete_from_submission_name(self):
		query = "DELETE FROM submission_name;"
		return query

	def delete_submission_name(self, submission_id):
		query = "DELETE FROM submission_name WHERE submission_id  =  '" + submission_id + "';"
		return query

	def delete_from_submission_description(self):
		query = "DELETE FROM submission_description;"
		return query

	def delete_submission_description(self, submission_id):
		query = "DELETE FROM submission_description WHERE submission_id  =  '" + submission_id + "';"
		return query

	def delete_from_submission_reception_date_and_time(self):
		query = "DELETE FROM submission_reception_date_and_time;"
		return query

	def delete_submission_reception_date_and_time(self, submission_id):
		query = "DELETE FROM submission_reception_date_and_time WHERE submission_id  =  '" + submission_id + "';"
		return query

	def delete_from_submission_cut_off_date_and_time(self):
		query = "DELETE FROM submission_cut_off_date_and_time;"
		return query

	def delete_submission_cut_off_date_and_time(self, submission_id):
		query = "DELETE FROM submission_cut_off_date_and_time WHERE submission_id  =  '" + submission_id + "';"
		return query

	def delete_from_procurement_type(self):
		query = "DELETE FROM procurement_type;"
		return query

	def delete_procurement_type(self, procurement_type_id):
		query = "DELETE FROM procurement_type WHERE procurement_type_id  =  '" + procurement_type_id + "';"
		return query

	def delete_from_procurement_type_code(self):
		query = "DELETE FROM procurement_type_code;"
		return query

	def delete_procurement_type_code(self, procurement_type_id):
		query = "DELETE FROM procurement_type_code WHERE procurement_type_id  =  '" + procurement_type_id + "';"
		return query

	def delete_from_procurement_type_name(self):
		query = "DELETE FROM procurement_type_name;"
		return query

	def delete_procurement_type_name(self, procurement_type_id):
		query = "DELETE FROM procurement_type_name WHERE procurement_type_id  =  '" + procurement_type_id + "';"
		return query

	def delete_from_procurement_type_description(self):
		query = "DELETE FROM procurement_type_description;"
		return query

	def delete_procurement_type_description(self, procurement_type_id):
		query = "DELETE FROM procurement_type_description WHERE procurement_type_id  =  '" + procurement_type_id + "';"
		return query

	def delete_from_procurement_method(self):
		query = "DELETE FROM procurement_method;"
		return query

	def delete_procurement_method(self, procurement_method_id):
		query = "DELETE FROM procurement_method WHERE procurement_method_id  =  '" + procurement_method_id + "';"
		return query

	def delete_from_procurement_method_code(self):
		query = "DELETE FROM procurement_method_code;"
		return query

	def delete_procurement_method_code(self, procurement_method_id):
		query = "DELETE FROM procurement_method_code WHERE procurement_method_id  =  '" + procurement_method_id + "';"
		return query

	def delete_from_procurement_method_name(self):
		query = "DELETE FROM procurement_method_name;"
		return query

	def delete_procurement_method_name(self, procurement_method_id):
		query = "DELETE FROM procurement_method_name WHERE procurement_method_id  =  '" + procurement_method_id + "';"
		return query

	def delete_from_procurement_method_description(self):
		query = "DELETE FROM procurement_method_description;"
		return query

	def delete_procurement_method_description(self, procurement_method_id):
		query = "DELETE FROM procurement_method_description WHERE procurement_method_id  =  '" + procurement_method_id + "';"
		return query

	def delete_from_bid(self):
		query = "DELETE FROM bid;"
		return query

	def delete_bid(self, bid_id):
		query = "DELETE FROM bid WHERE bid_id  =  '" + bid_id + "';"
		return query

	def delete_from_bid_submission_date(self):
		query = "DELETE FROM bid_submission_date;"
		return query

	def delete_bid_submission_date(self, bid_id):
		query = "DELETE FROM bid_submission_date WHERE bid_id  =  '" + bid_id + "';"
		return query

	def delete_from_bid_amount(self):
		query = "DELETE FROM bid_amount;"
		return query

	def delete_bid_amount(self, bid_id):
		query = "DELETE FROM bid_amount WHERE bid_id  =  '" + bid_id + "';"
		return query

	def delete_from_bid_extra_information(self):
		query = "DELETE FROM bid_extra_information;"
		return query

	def delete_bid_extra_information(self, bid_id):
		query = "DELETE FROM bid_extra_information WHERE bid_id  =  '" + bid_id + "';"
		return query

	def delete_from_item(self):
		query = "DELETE FROM item;"
		return query

	def delete_item(self, item_id):
		query = "DELETE FROM item WHERE item_id  =  '" + item_id + "';"
		return query

	def delete_from_item_code(self):
		query = "DELETE FROM item_code;"
		return query

	def delete_item_code(self, item_id):
		query = "DELETE FROM item_code WHERE item_id  =  '" + item_id + "';"
		return query

	def delete_from_item_name(self):
		query = "DELETE FROM item_name;"
		return query

	def delete_item_name(self, item_id):
		query = "DELETE FROM item_name WHERE item_id  =  '" + item_id + "';"
		return query

	def delete_from_item_unit_cost(self):
		query = "DELETE FROM item_unit_cost;"
		return query

	def delete_item_unit_cost(self, item_id):
		query = "DELETE FROM item_unit_cost WHERE item_id  =  '" + item_id + "';"
		return query

	def delete_from_item_description(self):
		query = "DELETE FROM item_description;"
		return query

	def delete_item_description(self, item_id):
		query = "DELETE FROM item_description WHERE item_id  =  '" + item_id + "';"
		return query

	def delete_from_procuring_entity(self):
		query = "DELETE FROM procuring_entity;"
		return query

	def delete_procuring_entity(self, procuring_entity_id):
		query = "DELETE FROM procuring_entity WHERE procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_from_procuring_entity_name(self):
		query = "DELETE FROM procuring_entity_name;"
		return query

	def delete_procuring_entity_name(self, procuring_entity_id):
		query = "DELETE FROM procuring_entity_name WHERE procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_from_procuring_entity_tax_identifier(self):
		query = "DELETE FROM procuring_entity_tax_identifier;"
		return query

	def delete_procuring_entity_tax_identifier(self, procuring_entity_id):
		query = "DELETE FROM procuring_entity_tax_identifier WHERE procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_from_procuring_entity_tax_identifier_value(self):
		query = "DELETE FROM procuring_entity_tax_identifier_value;"
		return query

	def delete_procuring_entity_tax_identifier_value(self, procuring_entity_id):
		query = "DELETE FROM procuring_entity_tax_identifier_value WHERE procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_from_procuring_entity_registration_number(self):
		query = "DELETE FROM procuring_entity_registration_number;"
		return query

	def delete_procuring_entity_registration_number(self, procuring_entity_id):
		query = "DELETE FROM procuring_entity_registration_number WHERE procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_from_procuring_entity_registration_date(self):
		query = "DELETE FROM procuring_entity_registration_date;"
		return query

	def delete_procuring_entity_registration_date(self, procuring_entity_id):
		query = "DELETE FROM procuring_entity_registration_date WHERE procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_from_procuring_entity_status(self):
		query = "DELETE FROM procuring_entity_status;"
		return query

	def delete_procuring_entity_status(self, procuring_entity_id):
		query = "DELETE FROM procuring_entity_status WHERE procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_from_supplying_entity(self):
		query = "DELETE FROM supplying_entity;"
		return query

	def delete_supplying_entity(self, supplying_entity_id):
		query = "DELETE FROM supplying_entity WHERE supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_from_supplying_entity_name(self):
		query = "DELETE FROM supplying_entity_name;"
		return query

	def delete_supplying_entity_name(self, supplying_entity_id):
		query = "DELETE FROM supplying_entity_name WHERE supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_from_supplying_entity_tax_identifier(self):
		query = "DELETE FROM supplying_entity_tax_identifier;"
		return query

	def delete_supplying_entity_tax_identifier(self, supplying_entity_id):
		query = "DELETE FROM supplying_entity_tax_identifier WHERE supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_from_supplying_entity_tax_identifier_value(self):
		query = "DELETE FROM supplying_entity_tax_identifier_value;"
		return query

	def delete_supplying_entity_tax_identifier_value(self, supplying_entity_id):
		query = "DELETE FROM supplying_entity_tax_identifier_value WHERE supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_from_supplying_entity_registration_number(self):
		query = "DELETE FROM supplying_entity_registration_number;"
		return query

	def delete_supplying_entity_registration_number(self, supplying_entity_id):
		query = "DELETE FROM supplying_entity_registration_number WHERE supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_from_supplying_entity_registration_date(self):
		query = "DELETE FROM supplying_entity_registration_date;"
		return query

	def delete_supplying_entity_registration_date(self, supplying_entity_id):
		query = "DELETE FROM supplying_entity_registration_date WHERE supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_from_supplying_entity_status(self):
		query = "DELETE FROM supplying_entity_status;"
		return query

	def delete_supplying_entity_status(self, supplying_entity_id):
		query = "DELETE FROM supplying_entity_status WHERE supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_from_address(self):
		query = "DELETE FROM address;"
		return query

	def delete_address(self, address_id):
		query = "DELETE FROM address WHERE address_id  =  '" + address_id + "';"
		return query

	def delete_from_address_country(self):
		query = "DELETE FROM address_country;"
		return query

	def delete_address_country(self, address_id):
		query = "DELETE FROM address_country WHERE address_id  =  '" + address_id + "';"
		return query

	def delete_from_address_address_line_1(self):
		query = "DELETE FROM address_address_line_1;"
		return query

	def delete_address_address_line_1(self, address_id):
		query = "DELETE FROM address_address_line_1 WHERE address_id  =  '" + address_id + "';"
		return query

	def delete_from_address_address_line_2(self):
		query = "DELETE FROM address_address_line_2;"
		return query

	def delete_address_address_line_2(self, address_id):
		query = "DELETE FROM address_address_line_2 WHERE address_id  =  '" + address_id + "';"
		return query

	def delete_from_address_address_line_3(self):
		query = "DELETE FROM address_address_line_3;"
		return query

	def delete_address_address_line_3(self, address_id):
		query = "DELETE FROM address_address_line_3 WHERE address_id  =  '" + address_id + "';"
		return query

	def delete_from_address_address_line_4(self):
		query = "DELETE FROM address_address_line_4;"
		return query

	def delete_address_address_line_4(self, address_id):
		query = "DELETE FROM address_address_line_4 WHERE address_id  =  '" + address_id + "';"
		return query

	def delete_from_address_address_line_5(self):
		query = "DELETE FROM address_address_line_5;"
		return query

	def delete_address_address_line_5(self, address_id):
		query = "DELETE FROM address_address_line_5 WHERE address_id  =  '" + address_id + "';"
		return query

	def delete_from_address_address_line_6(self):
		query = "DELETE FROM address_address_line_6;"
		return query

	def delete_address_address_line_6(self, address_id):
		query = "DELETE FROM address_address_line_6 WHERE address_id  =  '" + address_id + "';"
		return query

	def delete_from_address_address_line_7(self):
		query = "DELETE FROM address_address_line_7;"
		return query

	def delete_address_address_line_7(self, address_id):
		query = "DELETE FROM address_address_line_7 WHERE address_id  =  '" + address_id + "';"
		return query

	def delete_from_address_address_line_8(self):
		query = "DELETE FROM address_address_line_8;"
		return query

	def delete_address_address_line_8(self, address_id):
		query = "DELETE FROM address_address_line_8 WHERE address_id  =  '" + address_id + "';"
		return query

	def delete_from_address_address_line_9(self):
		query = "DELETE FROM address_address_line_9;"
		return query

	def delete_address_address_line_9(self, address_id):
		query = "DELETE FROM address_address_line_9 WHERE address_id  =  '" + address_id + "';"
		return query

	def delete_from_address_x_coord(self):
		query = "DELETE FROM address_x_coord;"
		return query

	def delete_address_x_coord(self, address_id):
		query = "DELETE FROM address_x_coord WHERE address_id  =  '" + address_id + "';"
		return query

	def delete_from_address_y_coord(self):
		query = "DELETE FROM address_y_coord;"
		return query

	def delete_address_y_coord(self, address_id):
		query = "DELETE FROM address_y_coord WHERE address_id  =  '" + address_id + "';"
		return query

	def delete_from_address_status(self):
		query = "DELETE FROM address_status;"
		return query

	def delete_address_status(self, address_id):
		query = "DELETE FROM address_status WHERE address_id  =  '" + address_id + "';"
		return query

	def delete_from_address_description(self):
		query = "DELETE FROM address_description;"
		return query

	def delete_address_description(self, address_id):
		query = "DELETE FROM address_description WHERE address_id  =  '" + address_id + "';"
		return query

	def delete_from_address_short_form(self):
		query = "DELETE FROM address_short_form;"
		return query

	def delete_address_short_form(self, address_id):
		query = "DELETE FROM address_short_form WHERE address_id  =  '" + address_id + "';"
		return query

	def delete_from_tender(self):
		query = "DELETE FROM tender;"
		return query

	def delete_tender(self, tender_id):
		query = "DELETE FROM tender WHERE tender_id  =  '" + tender_id + "';"
		return query

	def delete_from_tender_title(self):
		query = "DELETE FROM tender_title;"
		return query

	def delete_tender_title(self, tender_id):
		query = "DELETE FROM tender_title WHERE tender_id  =  '" + tender_id + "';"
		return query

	def delete_from_tender_description(self):
		query = "DELETE FROM tender_description;"
		return query

	def delete_tender_description(self, tender_id):
		query = "DELETE FROM tender_description WHERE tender_id  =  '" + tender_id + "';"
		return query

	def delete_from_tender_budget(self):
		query = "DELETE FROM tender_budget;"
		return query

	def delete_tender_budget(self, tender_id):
		query = "DELETE FROM tender_budget WHERE tender_id  =  '" + tender_id + "';"
		return query

	def delete_from_tender_status(self):
		query = "DELETE FROM tender_status;"
		return query

	def delete_tender_status(self, tender_id):
		query = "DELETE FROM tender_status WHERE tender_id  =  '" + tender_id + "';"
		return query

	def delete_from_tender_evaluate_mechanism(self):
		query = "DELETE FROM tender_evaluate_mechanism;"
		return query

	def delete_tender_evaluate_mechanism(self, tender_id):
		query = "DELETE FROM tender_evaluate_mechanism WHERE tender_id  =  '" + tender_id + "';"
		return query

	def delete_from_tender_publication_date_and_time(self):
		query = "DELETE FROM tender_publication_date_and_time;"
		return query

	def delete_tender_publication_date_and_time(self, tender_id):
		query = "DELETE FROM tender_publication_date_and_time WHERE tender_id  =  '" + tender_id + "';"
		return query

	def delete_from_tender_submission_cut_off_date_and_time(self):
		query = "DELETE FROM tender_submission_cut_off_date_and_time;"
		return query

	def delete_tender_submission_cut_off_date_and_time(self, tender_id):
		query = "DELETE FROM tender_submission_cut_off_date_and_time WHERE tender_id  =  '" + tender_id + "';"
		return query

	def delete_from_tender_award_notice_date(self):
		query = "DELETE FROM tender_award_notice_date;"
		return query

	def delete_tender_award_notice_date(self, tender_id):
		query = "DELETE FROM tender_award_notice_date WHERE tender_id  =  '" + tender_id + "';"
		return query

	def delete_from_tender_contract_notice_date(self):
		query = "DELETE FROM tender_contract_notice_date;"
		return query

	def delete_tender_contract_notice_date(self, tender_id):
		query = "DELETE FROM tender_contract_notice_date WHERE tender_id  =  '" + tender_id + "';"
		return query

	def delete_from_attachment(self):
		query = "DELETE FROM attachment;"
		return query

	def delete_attachment(self, attachment_id):
		query = "DELETE FROM attachment WHERE attachment_id  =  '" + attachment_id + "';"
		return query

	def delete_from_attachment_type(self):
		query = "DELETE FROM attachment_type;"
		return query

	def delete_attachment_type(self, attachment_id):
		query = "DELETE FROM attachment_type WHERE attachment_id  =  '" + attachment_id + "';"
		return query

	def delete_from_attachment_name(self):
		query = "DELETE FROM attachment_name;"
		return query

	def delete_attachment_name(self, attachment_id):
		query = "DELETE FROM attachment_name WHERE attachment_id  =  '" + attachment_id + "';"
		return query

	def delete_from_attachment_description(self):
		query = "DELETE FROM attachment_description;"
		return query

	def delete_attachment_description(self, attachment_id):
		query = "DELETE FROM attachment_description WHERE attachment_id  =  '" + attachment_id + "';"
		return query

	def delete_from_attachment_link(self):
		query = "DELETE FROM attachment_link;"
		return query

	def delete_attachment_link(self, attachment_id):
		query = "DELETE FROM attachment_link WHERE attachment_id  =  '" + attachment_id + "';"
		return query

	def delete_from_award(self):
		query = "DELETE FROM award;"
		return query

	def delete_award(self, award_id):
		query = "DELETE FROM award WHERE award_id  =  '" + award_id + "';"
		return query

	def delete_from_award_is_accepted(self):
		query = "DELETE FROM award_is_accepted;"
		return query

	def delete_award_is_accepted(self, award_id):
		query = "DELETE FROM award_is_accepted WHERE award_id  =  '" + award_id + "';"
		return query

	def delete_from_award_date_replied(self):
		query = "DELETE FROM award_date_replied;"
		return query

	def delete_award_date_replied(self, award_id):
		query = "DELETE FROM award_date_replied WHERE award_id  =  '" + award_id + "';"
		return query

	def delete_from_award_reply_reason(self):
		query = "DELETE FROM award_reply_reason;"
		return query

	def delete_award_reply_reason(self, award_id):
		query = "DELETE FROM award_reply_reason WHERE award_id  =  '" + award_id + "';"
		return query

	def delete_from_award_award_amount(self):
		query = "DELETE FROM award_award_amount;"
		return query

	def delete_award_award_amount(self, award_id):
		query = "DELETE FROM award_award_amount WHERE award_id  =  '" + award_id + "';"
		return query

	def delete_from_contact(self):
		query = "DELETE FROM contact;"
		return query

	def delete_contact(self, contact_id):
		query = "DELETE FROM contact WHERE contact_id  =  '" + contact_id + "';"
		return query

	def delete_from_contact_name(self):
		query = "DELETE FROM contact_name;"
		return query

	def delete_contact_name(self, contact_id):
		query = "DELETE FROM contact_name WHERE contact_id  =  '" + contact_id + "';"
		return query

	def delete_from_contact_value(self):
		query = "DELETE FROM contact_value;"
		return query

	def delete_contact_value(self, contact_id):
		query = "DELETE FROM contact_value WHERE contact_id  =  '" + contact_id + "';"
		return query

	def delete_from_contact_status(self):
		query = "DELETE FROM contact_status;"
		return query

	def delete_contact_status(self, contact_id):
		query = "DELETE FROM contact_status WHERE contact_id  =  '" + contact_id + "';"
		return query

	def delete_from_contract(self):
		query = "DELETE FROM contract;"
		return query

	def delete_contract(self, contract_id):
		query = "DELETE FROM contract WHERE contract_id  =  '" + contract_id + "';"
		return query

	def delete_from_contract_title(self):
		query = "DELETE FROM contract_title;"
		return query

	def delete_contract_title(self, contract_id):
		query = "DELETE FROM contract_title WHERE contract_id  =  '" + contract_id + "';"
		return query

	def delete_from_contract_amount(self):
		query = "DELETE FROM contract_amount;"
		return query

	def delete_contract_amount(self, contract_id):
		query = "DELETE FROM contract_amount WHERE contract_id  =  '" + contract_id + "';"
		return query

	def delete_from_contract_status(self):
		query = "DELETE FROM contract_status;"
		return query

	def delete_contract_status(self, contract_id):
		query = "DELETE FROM contract_status WHERE contract_id  =  '" + contract_id + "';"
		return query

	def delete_from_contract_description(self):
		query = "DELETE FROM contract_description;"
		return query

	def delete_contract_description(self, contract_id):
		query = "DELETE FROM contract_description WHERE contract_id  =  '" + contract_id + "';"
		return query

	def delete_from_fee(self):
		query = "DELETE FROM fee;"
		return query

	def delete_fee(self, fee_id):
		query = "DELETE FROM fee WHERE fee_id  =  '" + fee_id + "';"
		return query

	def delete_from_fee_name(self):
		query = "DELETE FROM fee_name;"
		return query

	def delete_fee_name(self, fee_id):
		query = "DELETE FROM fee_name WHERE fee_id  =  '" + fee_id + "';"
		return query

	def delete_from_fee_amount(self):
		query = "DELETE FROM fee_amount;"
		return query

	def delete_fee_amount(self, fee_id):
		query = "DELETE FROM fee_amount WHERE fee_id  =  '" + fee_id + "';"
		return query

	def delete_from_fee_type(self):
		query = "DELETE FROM fee_type;"
		return query

	def delete_fee_type(self, fee_id):
		query = "DELETE FROM fee_type WHERE fee_id  =  '" + fee_id + "';"
		return query

	def delete_from_payment(self):
		query = "DELETE FROM payment;"
		return query

	def delete_payment(self, payment_id):
		query = "DELETE FROM payment WHERE payment_id  =  '" + payment_id + "';"
		return query

	def delete_from_payment_transaction_id(self):
		query = "DELETE FROM payment_transaction_id;"
		return query

	def delete_payment_transaction_id(self, payment_id):
		query = "DELETE FROM payment_transaction_id WHERE payment_id  =  '" + payment_id + "';"
		return query

	def delete_from_payment_date_received(self):
		query = "DELETE FROM payment_date_received;"
		return query

	def delete_payment_date_received(self, payment_id):
		query = "DELETE FROM payment_date_received WHERE payment_id  =  '" + payment_id + "';"
		return query

	def delete_from_payment_amount(self):
		query = "DELETE FROM payment_amount;"
		return query

	def delete_payment_amount(self, payment_id):
		query = "DELETE FROM payment_amount WHERE payment_id  =  '" + payment_id + "';"
		return query

	def delete_from_payment_currency(self):
		query = "DELETE FROM payment_currency;"
		return query

	def delete_payment_currency(self, payment_id):
		query = "DELETE FROM payment_currency WHERE payment_id  =  '" + payment_id + "';"
		return query

	def delete_from_payment_status(self):
		query = "DELETE FROM payment_status;"
		return query

	def delete_payment_status(self, payment_id):
		query = "DELETE FROM payment_status WHERE payment_id  =  '" + payment_id + "';"
		return query

	def delete_from_payment_extra_information(self):
		query = "DELETE FROM payment_extra_information;"
		return query

	def delete_payment_extra_information(self, payment_id):
		query = "DELETE FROM payment_extra_information WHERE payment_id  =  '" + payment_id + "';"
		return query

	def delete_from_plan(self):
		query = "DELETE FROM plan;"
		return query

	def delete_plan(self, plan_id):
		query = "DELETE FROM plan WHERE plan_id  =  '" + plan_id + "';"
		return query

	def delete_from_plan_budget(self):
		query = "DELETE FROM plan_budget;"
		return query

	def delete_plan_budget(self, plan_id):
		query = "DELETE FROM plan_budget WHERE plan_id  =  '" + plan_id + "';"
		return query

	def delete_from_plan_submission_date_and_time(self):
		query = "DELETE FROM plan_submission_date_and_time;"
		return query

	def delete_plan_submission_date_and_time(self, plan_id):
		query = "DELETE FROM plan_submission_date_and_time WHERE plan_id  =  '" + plan_id + "';"
		return query

	def delete_from_plan_description(self):
		query = "DELETE FROM plan_description;"
		return query

	def delete_plan_description(self, plan_id):
		query = "DELETE FROM plan_description WHERE plan_id  =  '" + plan_id + "';"
		return query

	def delete_from_alert(self):
		query = "DELETE FROM alert;"
		return query

	def delete_alert(self, alert_id):
		query = "DELETE FROM alert WHERE alert_id  =  '" + alert_id + "';"
		return query

	def delete_from_alert_subject(self):
		query = "DELETE FROM alert_subject;"
		return query

	def delete_alert_subject(self, alert_id):
		query = "DELETE FROM alert_subject WHERE alert_id  =  '" + alert_id + "';"
		return query

	def delete_from_alert_description(self):
		query = "DELETE FROM alert_description;"
		return query

	def delete_alert_description(self, alert_id):
		query = "DELETE FROM alert_description WHERE alert_id  =  '" + alert_id + "';"
		return query

	def delete_from_alert_authority(self):
		query = "DELETE FROM alert_authority;"
		return query

	def delete_alert_authority(self, alert_authority_id):
		query = "DELETE FROM alert_authority WHERE alert_authority_id  =  '" + alert_authority_id + "';"
		return query

	def delete_from_alert_authority_name(self):
		query = "DELETE FROM alert_authority_name;"
		return query

	def delete_alert_authority_name(self, alert_authority_id):
		query = "DELETE FROM alert_authority_name WHERE alert_authority_id  =  '" + alert_authority_id + "';"
		return query

	def delete_from_alert_authority_description(self):
		query = "DELETE FROM alert_authority_description;"
		return query

	def delete_alert_authority_description(self, alert_authority_id):
		query = "DELETE FROM alert_authority_description WHERE alert_authority_id  =  '" + alert_authority_id + "';"
		return query

	def delete_from_alert_level(self):
		query = "DELETE FROM alert_level;"
		return query

	def delete_alert_level(self, alert_level_id):
		query = "DELETE FROM alert_level WHERE alert_level_id  =  '" + alert_level_id + "';"
		return query

	def delete_from_alert_level_name(self):
		query = "DELETE FROM alert_level_name;"
		return query

	def delete_alert_level_name(self, alert_level_id):
		query = "DELETE FROM alert_level_name WHERE alert_level_id  =  '" + alert_level_id + "';"
		return query

	def delete_from_alert_level_description(self):
		query = "DELETE FROM alert_level_description;"
		return query

	def delete_alert_level_description(self, alert_level_id):
		query = "DELETE FROM alert_level_description WHERE alert_level_id  =  '" + alert_level_id + "';"
		return query

	def delete_from_user_account(self):
		query = "DELETE FROM user_account;"
		return query

	def delete_user_account(self, user_account_id):
		query = "DELETE FROM user_account WHERE user_account_id  =  '" + user_account_id + "';"
		return query

	def delete_from_user_account_national_id_number(self):
		query = "DELETE FROM user_account_national_id_number;"
		return query

	def delete_user_account_national_id_number(self, user_account_id):
		query = "DELETE FROM user_account_national_id_number WHERE user_account_id  =  '" + user_account_id + "';"
		return query

	def delete_from_user_account_category(self):
		query = "DELETE FROM user_account_category;"
		return query

	def delete_user_account_category(self, user_account_id):
		query = "DELETE FROM user_account_category WHERE user_account_id  =  '" + user_account_id + "';"
		return query

	def delete_from_user_account_first_name(self):
		query = "DELETE FROM user_account_first_name;"
		return query

	def delete_user_account_first_name(self, user_account_id):
		query = "DELETE FROM user_account_first_name WHERE user_account_id  =  '" + user_account_id + "';"
		return query

	def delete_from_user_account_last_name(self):
		query = "DELETE FROM user_account_last_name;"
		return query

	def delete_user_account_last_name(self, user_account_id):
		query = "DELETE FROM user_account_last_name WHERE user_account_id  =  '" + user_account_id + "';"
		return query

	def delete_from_user_account_other_names(self):
		query = "DELETE FROM user_account_other_names;"
		return query

	def delete_user_account_other_names(self, user_account_id):
		query = "DELETE FROM user_account_other_names WHERE user_account_id  =  '" + user_account_id + "';"
		return query

	def delete_from_user_account_date_of_birth(self):
		query = "DELETE FROM user_account_date_of_birth;"
		return query

	def delete_user_account_date_of_birth(self, user_account_id):
		query = "DELETE FROM user_account_date_of_birth WHERE user_account_id  =  '" + user_account_id + "';"
		return query

	def delete_from_user_account_gender(self):
		query = "DELETE FROM user_account_gender;"
		return query

	def delete_user_account_gender(self, user_account_id):
		query = "DELETE FROM user_account_gender WHERE user_account_id  =  '" + user_account_id + "';"
		return query

	def delete_from_user_account_status(self):
		query = "DELETE FROM user_account_status;"
		return query

	def delete_user_account_status(self, user_account_id):
		query = "DELETE FROM user_account_status WHERE user_account_id  =  '" + user_account_id + "';"
		return query

	def delete_from_user_account_email(self):
		query = "DELETE FROM user_account_email;"
		return query

	def delete_user_account_email(self, user_account_id):
		query = "DELETE FROM user_account_email WHERE user_account_id  =  '" + user_account_id + "';"
		return query

	def delete_from_user_account_password(self):
		query = "DELETE FROM user_account_password;"
		return query

	def delete_user_account_password(self, user_account_id):
		query = "DELETE FROM user_account_password WHERE user_account_id  =  '" + user_account_id + "';"
		return query

	def delete_from_user_account_photo(self):
		query = "DELETE FROM user_account_photo;"
		return query

	def delete_user_account_photo(self, user_account_id):
		query = "DELETE FROM user_account_photo WHERE user_account_id  =  '" + user_account_id + "';"
		return query

	def delete_from_appeal(self):
		query = "DELETE FROM appeal;"
		return query

	def delete_appeal(self, appeal_id):
		query = "DELETE FROM appeal WHERE appeal_id  =  '" + appeal_id + "';"
		return query

	def delete_from_appeal_subject(self):
		query = "DELETE FROM appeal_subject;"
		return query

	def delete_appeal_subject(self, appeal_id):
		query = "DELETE FROM appeal_subject WHERE appeal_id  =  '" + appeal_id + "';"
		return query

	def delete_from_appeal_description(self):
		query = "DELETE FROM appeal_description;"
		return query

	def delete_appeal_description(self, appeal_id):
		query = "DELETE FROM appeal_description WHERE appeal_id  =  '" + appeal_id + "';"
		return query

	def delete_from_countryfiscal_yearmap(self):
		query = "DELETE FROM countryfiscal_yearmap;"
		return query

	def delete_countryfiscal_yearmap(self, key_column, country_id, fiscal_year_id):
		query = "DELETE FROM countryfiscal_yearmap WHERE key_column  =  '" + key_column + "' AND country_id  =  '" + country_id + "' AND fiscal_year_id  =  '" + fiscal_year_id + "';"
		return query

	def delete_countryfiscal_yearmap_by_key_column(self, key_column):
		query = "DELETE FROM countryfiscal_yearmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_countryfiscal_yearmap_by_country_id(self, country_id):
		query = "DELETE FROM countryfiscal_yearmap WHERE country_id  =  '" + country_id + "';"
		return query

	def delete_countryfiscal_yearmap_by_fiscal_year_id(self, fiscal_year_id):
		query = "DELETE FROM countryfiscal_yearmap WHERE fiscal_year_id  =  '" + fiscal_year_id + "';"
		return query

	def delete_from_countryprocurement_stagemap(self):
		query = "DELETE FROM countryprocurement_stagemap;"
		return query

	def delete_countryprocurement_stagemap(self, key_column, country_id, procurement_stage_id):
		query = "DELETE FROM countryprocurement_stagemap WHERE key_column  =  '" + key_column + "' AND country_id  =  '" + country_id + "' AND procurement_stage_id  =  '" + procurement_stage_id + "';"
		return query

	def delete_countryprocurement_stagemap_by_key_column(self, key_column):
		query = "DELETE FROM countryprocurement_stagemap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_countryprocurement_stagemap_by_country_id(self, country_id):
		query = "DELETE FROM countryprocurement_stagemap WHERE country_id  =  '" + country_id + "';"
		return query

	def delete_countryprocurement_stagemap_by_procurement_stage_id(self, procurement_stage_id):
		query = "DELETE FROM countryprocurement_stagemap WHERE procurement_stage_id  =  '" + procurement_stage_id + "';"
		return query

	def delete_from_countryprocurement_typemap(self):
		query = "DELETE FROM countryprocurement_typemap;"
		return query

	def delete_countryprocurement_typemap(self, key_column, country_id, procurement_type_id):
		query = "DELETE FROM countryprocurement_typemap WHERE key_column  =  '" + key_column + "' AND country_id  =  '" + country_id + "' AND procurement_type_id  =  '" + procurement_type_id + "';"
		return query

	def delete_countryprocurement_typemap_by_key_column(self, key_column):
		query = "DELETE FROM countryprocurement_typemap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_countryprocurement_typemap_by_country_id(self, country_id):
		query = "DELETE FROM countryprocurement_typemap WHERE country_id  =  '" + country_id + "';"
		return query

	def delete_countryprocurement_typemap_by_procurement_type_id(self, procurement_type_id):
		query = "DELETE FROM countryprocurement_typemap WHERE procurement_type_id  =  '" + procurement_type_id + "';"
		return query

	def delete_from_countryprocurement_methodmap(self):
		query = "DELETE FROM countryprocurement_methodmap;"
		return query

	def delete_countryprocurement_methodmap(self, key_column, country_id, procurement_method_id):
		query = "DELETE FROM countryprocurement_methodmap WHERE key_column  =  '" + key_column + "' AND country_id  =  '" + country_id + "' AND procurement_method_id  =  '" + procurement_method_id + "';"
		return query

	def delete_countryprocurement_methodmap_by_key_column(self, key_column):
		query = "DELETE FROM countryprocurement_methodmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_countryprocurement_methodmap_by_country_id(self, country_id):
		query = "DELETE FROM countryprocurement_methodmap WHERE country_id  =  '" + country_id + "';"
		return query

	def delete_countryprocurement_methodmap_by_procurement_method_id(self, procurement_method_id):
		query = "DELETE FROM countryprocurement_methodmap WHERE procurement_method_id  =  '" + procurement_method_id + "';"
		return query

	def delete_from_countryprocuring_entitymap(self):
		query = "DELETE FROM countryprocuring_entitymap;"
		return query

	def delete_countryprocuring_entitymap(self, key_column, country_id, procuring_entity_id):
		query = "DELETE FROM countryprocuring_entitymap WHERE key_column  =  '" + key_column + "' AND country_id  =  '" + country_id + "' AND procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_countryprocuring_entitymap_by_key_column(self, key_column):
		query = "DELETE FROM countryprocuring_entitymap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_countryprocuring_entitymap_by_country_id(self, country_id):
		query = "DELETE FROM countryprocuring_entitymap WHERE country_id  =  '" + country_id + "';"
		return query

	def delete_countryprocuring_entitymap_by_procuring_entity_id(self, procuring_entity_id):
		query = "DELETE FROM countryprocuring_entitymap WHERE procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_from_countrysupplying_entitymap(self):
		query = "DELETE FROM countrysupplying_entitymap;"
		return query

	def delete_countrysupplying_entitymap(self, key_column, country_id, supplying_entity_id):
		query = "DELETE FROM countrysupplying_entitymap WHERE key_column  =  '" + key_column + "' AND country_id  =  '" + country_id + "' AND supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_countrysupplying_entitymap_by_key_column(self, key_column):
		query = "DELETE FROM countrysupplying_entitymap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_countrysupplying_entitymap_by_country_id(self, country_id):
		query = "DELETE FROM countrysupplying_entitymap WHERE country_id  =  '" + country_id + "';"
		return query

	def delete_countrysupplying_entitymap_by_supplying_entity_id(self, supplying_entity_id):
		query = "DELETE FROM countrysupplying_entitymap WHERE supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_from_countryred_flagmap(self):
		query = "DELETE FROM countryred_flagmap;"
		return query

	def delete_countryred_flagmap(self, key_column, country_id, red_flag_id):
		query = "DELETE FROM countryred_flagmap WHERE key_column  =  '" + key_column + "' AND country_id  =  '" + country_id + "' AND red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_countryred_flagmap_by_key_column(self, key_column):
		query = "DELETE FROM countryred_flagmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_countryred_flagmap_by_country_id(self, country_id):
		query = "DELETE FROM countryred_flagmap WHERE country_id  =  '" + country_id + "';"
		return query

	def delete_countryred_flagmap_by_red_flag_id(self, red_flag_id):
		query = "DELETE FROM countryred_flagmap WHERE red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_from_countryillicit_schememap(self):
		query = "DELETE FROM countryillicit_schememap;"
		return query

	def delete_countryillicit_schememap(self, key_column, country_id, illicit_scheme_id):
		query = "DELETE FROM countryillicit_schememap WHERE key_column  =  '" + key_column + "' AND country_id  =  '" + country_id + "' AND illicit_scheme_id  =  '" + illicit_scheme_id + "';"
		return query

	def delete_countryillicit_schememap_by_key_column(self, key_column):
		query = "DELETE FROM countryillicit_schememap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_countryillicit_schememap_by_country_id(self, country_id):
		query = "DELETE FROM countryillicit_schememap WHERE country_id  =  '" + country_id + "';"
		return query

	def delete_countryillicit_schememap_by_illicit_scheme_id(self, illicit_scheme_id):
		query = "DELETE FROM countryillicit_schememap WHERE illicit_scheme_id  =  '" + illicit_scheme_id + "';"
		return query

	def delete_from_fiscal_yeartendermap(self):
		query = "DELETE FROM fiscal_yeartendermap;"
		return query

	def delete_fiscal_yeartendermap(self, key_column, fiscal_year_id, tender_id):
		query = "DELETE FROM fiscal_yeartendermap WHERE key_column  =  '" + key_column + "' AND fiscal_year_id  =  '" + fiscal_year_id + "' AND tender_id  =  '" + tender_id + "';"
		return query

	def delete_fiscal_yeartendermap_by_key_column(self, key_column):
		query = "DELETE FROM fiscal_yeartendermap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_fiscal_yeartendermap_by_fiscal_year_id(self, fiscal_year_id):
		query = "DELETE FROM fiscal_yeartendermap WHERE fiscal_year_id  =  '" + fiscal_year_id + "';"
		return query

	def delete_fiscal_yeartendermap_by_tender_id(self, tender_id):
		query = "DELETE FROM fiscal_yeartendermap WHERE tender_id  =  '" + tender_id + "';"
		return query

	def delete_from_fiscal_yearillicit_schememap(self):
		query = "DELETE FROM fiscal_yearillicit_schememap;"
		return query

	def delete_fiscal_yearillicit_schememap(self, key_column, fiscal_year_id, illicit_scheme_id):
		query = "DELETE FROM fiscal_yearillicit_schememap WHERE key_column  =  '" + key_column + "' AND fiscal_year_id  =  '" + fiscal_year_id + "' AND illicit_scheme_id  =  '" + illicit_scheme_id + "';"
		return query

	def delete_fiscal_yearillicit_schememap_by_key_column(self, key_column):
		query = "DELETE FROM fiscal_yearillicit_schememap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_fiscal_yearillicit_schememap_by_fiscal_year_id(self, fiscal_year_id):
		query = "DELETE FROM fiscal_yearillicit_schememap WHERE fiscal_year_id  =  '" + fiscal_year_id + "';"
		return query

	def delete_fiscal_yearillicit_schememap_by_illicit_scheme_id(self, illicit_scheme_id):
		query = "DELETE FROM fiscal_yearillicit_schememap WHERE illicit_scheme_id  =  '" + illicit_scheme_id + "';"
		return query

	def delete_from_fiscal_yearred_flagmap(self):
		query = "DELETE FROM fiscal_yearred_flagmap;"
		return query

	def delete_fiscal_yearred_flagmap(self, key_column, fiscal_year_id, red_flag_id):
		query = "DELETE FROM fiscal_yearred_flagmap WHERE key_column  =  '" + key_column + "' AND fiscal_year_id  =  '" + fiscal_year_id + "' AND red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_fiscal_yearred_flagmap_by_key_column(self, key_column):
		query = "DELETE FROM fiscal_yearred_flagmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_fiscal_yearred_flagmap_by_fiscal_year_id(self, fiscal_year_id):
		query = "DELETE FROM fiscal_yearred_flagmap WHERE fiscal_year_id  =  '" + fiscal_year_id + "';"
		return query

	def delete_fiscal_yearred_flagmap_by_red_flag_id(self, red_flag_id):
		query = "DELETE FROM fiscal_yearred_flagmap WHERE red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_from_fiscal_yearprocurement_stagemap(self):
		query = "DELETE FROM fiscal_yearprocurement_stagemap;"
		return query

	def delete_fiscal_yearprocurement_stagemap(self, key_column, fiscal_year_id, procurement_stage_id):
		query = "DELETE FROM fiscal_yearprocurement_stagemap WHERE key_column  =  '" + key_column + "' AND fiscal_year_id  =  '" + fiscal_year_id + "' AND procurement_stage_id  =  '" + procurement_stage_id + "';"
		return query

	def delete_fiscal_yearprocurement_stagemap_by_key_column(self, key_column):
		query = "DELETE FROM fiscal_yearprocurement_stagemap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_fiscal_yearprocurement_stagemap_by_fiscal_year_id(self, fiscal_year_id):
		query = "DELETE FROM fiscal_yearprocurement_stagemap WHERE fiscal_year_id  =  '" + fiscal_year_id + "';"
		return query

	def delete_fiscal_yearprocurement_stagemap_by_procurement_stage_id(self, procurement_stage_id):
		query = "DELETE FROM fiscal_yearprocurement_stagemap WHERE procurement_stage_id  =  '" + procurement_stage_id + "';"
		return query

	def delete_from_fiscal_yearprocurement_typemap(self):
		query = "DELETE FROM fiscal_yearprocurement_typemap;"
		return query

	def delete_fiscal_yearprocurement_typemap(self, key_column, fiscal_year_id, procurement_type_id):
		query = "DELETE FROM fiscal_yearprocurement_typemap WHERE key_column  =  '" + key_column + "' AND fiscal_year_id  =  '" + fiscal_year_id + "' AND procurement_type_id  =  '" + procurement_type_id + "';"
		return query

	def delete_fiscal_yearprocurement_typemap_by_key_column(self, key_column):
		query = "DELETE FROM fiscal_yearprocurement_typemap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_fiscal_yearprocurement_typemap_by_fiscal_year_id(self, fiscal_year_id):
		query = "DELETE FROM fiscal_yearprocurement_typemap WHERE fiscal_year_id  =  '" + fiscal_year_id + "';"
		return query

	def delete_fiscal_yearprocurement_typemap_by_procurement_type_id(self, procurement_type_id):
		query = "DELETE FROM fiscal_yearprocurement_typemap WHERE procurement_type_id  =  '" + procurement_type_id + "';"
		return query

	def delete_from_fiscal_yearprocurement_methodmap(self):
		query = "DELETE FROM fiscal_yearprocurement_methodmap;"
		return query

	def delete_fiscal_yearprocurement_methodmap(self, key_column, fiscal_year_id, procurement_method_id):
		query = "DELETE FROM fiscal_yearprocurement_methodmap WHERE key_column  =  '" + key_column + "' AND fiscal_year_id  =  '" + fiscal_year_id + "' AND procurement_method_id  =  '" + procurement_method_id + "';"
		return query

	def delete_fiscal_yearprocurement_methodmap_by_key_column(self, key_column):
		query = "DELETE FROM fiscal_yearprocurement_methodmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_fiscal_yearprocurement_methodmap_by_fiscal_year_id(self, fiscal_year_id):
		query = "DELETE FROM fiscal_yearprocurement_methodmap WHERE fiscal_year_id  =  '" + fiscal_year_id + "';"
		return query

	def delete_fiscal_yearprocurement_methodmap_by_procurement_method_id(self, procurement_method_id):
		query = "DELETE FROM fiscal_yearprocurement_methodmap WHERE procurement_method_id  =  '" + procurement_method_id + "';"
		return query

	def delete_from_fiscal_yearbidmap(self):
		query = "DELETE FROM fiscal_yearbidmap;"
		return query

	def delete_fiscal_yearbidmap(self, key_column, fiscal_year_id, bid_id):
		query = "DELETE FROM fiscal_yearbidmap WHERE key_column  =  '" + key_column + "' AND fiscal_year_id  =  '" + fiscal_year_id + "' AND bid_id  =  '" + bid_id + "';"
		return query

	def delete_fiscal_yearbidmap_by_key_column(self, key_column):
		query = "DELETE FROM fiscal_yearbidmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_fiscal_yearbidmap_by_fiscal_year_id(self, fiscal_year_id):
		query = "DELETE FROM fiscal_yearbidmap WHERE fiscal_year_id  =  '" + fiscal_year_id + "';"
		return query

	def delete_fiscal_yearbidmap_by_bid_id(self, bid_id):
		query = "DELETE FROM fiscal_yearbidmap WHERE bid_id  =  '" + bid_id + "';"
		return query

	def delete_from_fiscal_yearitemmap(self):
		query = "DELETE FROM fiscal_yearitemmap;"
		return query

	def delete_fiscal_yearitemmap(self, key_column, fiscal_year_id, item_id):
		query = "DELETE FROM fiscal_yearitemmap WHERE key_column  =  '" + key_column + "' AND fiscal_year_id  =  '" + fiscal_year_id + "' AND item_id  =  '" + item_id + "';"
		return query

	def delete_fiscal_yearitemmap_by_key_column(self, key_column):
		query = "DELETE FROM fiscal_yearitemmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_fiscal_yearitemmap_by_fiscal_year_id(self, fiscal_year_id):
		query = "DELETE FROM fiscal_yearitemmap WHERE fiscal_year_id  =  '" + fiscal_year_id + "';"
		return query

	def delete_fiscal_yearitemmap_by_item_id(self, item_id):
		query = "DELETE FROM fiscal_yearitemmap WHERE item_id  =  '" + item_id + "';"
		return query

	def delete_from_fiscal_yearcontractmap(self):
		query = "DELETE FROM fiscal_yearcontractmap;"
		return query

	def delete_fiscal_yearcontractmap(self, key_column, fiscal_year_id, contract_id):
		query = "DELETE FROM fiscal_yearcontractmap WHERE key_column  =  '" + key_column + "' AND fiscal_year_id  =  '" + fiscal_year_id + "' AND contract_id  =  '" + contract_id + "';"
		return query

	def delete_fiscal_yearcontractmap_by_key_column(self, key_column):
		query = "DELETE FROM fiscal_yearcontractmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_fiscal_yearcontractmap_by_fiscal_year_id(self, fiscal_year_id):
		query = "DELETE FROM fiscal_yearcontractmap WHERE fiscal_year_id  =  '" + fiscal_year_id + "';"
		return query

	def delete_fiscal_yearcontractmap_by_contract_id(self, contract_id):
		query = "DELETE FROM fiscal_yearcontractmap WHERE contract_id  =  '" + contract_id + "';"
		return query

	def delete_from_fiscal_yearconfigurationmap(self):
		query = "DELETE FROM fiscal_yearconfigurationmap;"
		return query

	def delete_fiscal_yearconfigurationmap(self, key_column, fiscal_year_id, configuration_id):
		query = "DELETE FROM fiscal_yearconfigurationmap WHERE key_column  =  '" + key_column + "' AND fiscal_year_id  =  '" + fiscal_year_id + "' AND configuration_id  =  '" + configuration_id + "';"
		return query

	def delete_fiscal_yearconfigurationmap_by_key_column(self, key_column):
		query = "DELETE FROM fiscal_yearconfigurationmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_fiscal_yearconfigurationmap_by_fiscal_year_id(self, fiscal_year_id):
		query = "DELETE FROM fiscal_yearconfigurationmap WHERE fiscal_year_id  =  '" + fiscal_year_id + "';"
		return query

	def delete_fiscal_yearconfigurationmap_by_configuration_id(self, configuration_id):
		query = "DELETE FROM fiscal_yearconfigurationmap WHERE configuration_id  =  '" + configuration_id + "';"
		return query

	def delete_from_fiscal_yearfeemap(self):
		query = "DELETE FROM fiscal_yearfeemap;"
		return query

	def delete_fiscal_yearfeemap(self, key_column, fiscal_year_id, fee_id):
		query = "DELETE FROM fiscal_yearfeemap WHERE key_column  =  '" + key_column + "' AND fiscal_year_id  =  '" + fiscal_year_id + "' AND fee_id  =  '" + fee_id + "';"
		return query

	def delete_fiscal_yearfeemap_by_key_column(self, key_column):
		query = "DELETE FROM fiscal_yearfeemap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_fiscal_yearfeemap_by_fiscal_year_id(self, fiscal_year_id):
		query = "DELETE FROM fiscal_yearfeemap WHERE fiscal_year_id  =  '" + fiscal_year_id + "';"
		return query

	def delete_fiscal_yearfeemap_by_fee_id(self, fee_id):
		query = "DELETE FROM fiscal_yearfeemap WHERE fee_id  =  '" + fee_id + "';"
		return query

	def delete_from_fiscal_yearprocuring_entitymap(self):
		query = "DELETE FROM fiscal_yearprocuring_entitymap;"
		return query

	def delete_fiscal_yearprocuring_entitymap(self, key_column, fiscal_year_id, procuring_entity_id):
		query = "DELETE FROM fiscal_yearprocuring_entitymap WHERE key_column  =  '" + key_column + "' AND fiscal_year_id  =  '" + fiscal_year_id + "' AND procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_fiscal_yearprocuring_entitymap_by_key_column(self, key_column):
		query = "DELETE FROM fiscal_yearprocuring_entitymap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_fiscal_yearprocuring_entitymap_by_fiscal_year_id(self, fiscal_year_id):
		query = "DELETE FROM fiscal_yearprocuring_entitymap WHERE fiscal_year_id  =  '" + fiscal_year_id + "';"
		return query

	def delete_fiscal_yearprocuring_entitymap_by_procuring_entity_id(self, procuring_entity_id):
		query = "DELETE FROM fiscal_yearprocuring_entitymap WHERE procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_from_fiscal_yearsupplying_entitymap(self):
		query = "DELETE FROM fiscal_yearsupplying_entitymap;"
		return query

	def delete_fiscal_yearsupplying_entitymap(self, key_column, fiscal_year_id, supplying_entity_id):
		query = "DELETE FROM fiscal_yearsupplying_entitymap WHERE key_column  =  '" + key_column + "' AND fiscal_year_id  =  '" + fiscal_year_id + "' AND supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_fiscal_yearsupplying_entitymap_by_key_column(self, key_column):
		query = "DELETE FROM fiscal_yearsupplying_entitymap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_fiscal_yearsupplying_entitymap_by_fiscal_year_id(self, fiscal_year_id):
		query = "DELETE FROM fiscal_yearsupplying_entitymap WHERE fiscal_year_id  =  '" + fiscal_year_id + "';"
		return query

	def delete_fiscal_yearsupplying_entitymap_by_supplying_entity_id(self, supplying_entity_id):
		query = "DELETE FROM fiscal_yearsupplying_entitymap WHERE supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_from_fiscal_yearawardmap(self):
		query = "DELETE FROM fiscal_yearawardmap;"
		return query

	def delete_fiscal_yearawardmap(self, key_column, fiscal_year_id, award_id):
		query = "DELETE FROM fiscal_yearawardmap WHERE key_column  =  '" + key_column + "' AND fiscal_year_id  =  '" + fiscal_year_id + "' AND award_id  =  '" + award_id + "';"
		return query

	def delete_fiscal_yearawardmap_by_key_column(self, key_column):
		query = "DELETE FROM fiscal_yearawardmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_fiscal_yearawardmap_by_fiscal_year_id(self, fiscal_year_id):
		query = "DELETE FROM fiscal_yearawardmap WHERE fiscal_year_id  =  '" + fiscal_year_id + "';"
		return query

	def delete_fiscal_yearawardmap_by_award_id(self, award_id):
		query = "DELETE FROM fiscal_yearawardmap WHERE award_id  =  '" + award_id + "';"
		return query

	def delete_from_fiscal_yearplanmap(self):
		query = "DELETE FROM fiscal_yearplanmap;"
		return query

	def delete_fiscal_yearplanmap(self, key_column, fiscal_year_id, plan_id):
		query = "DELETE FROM fiscal_yearplanmap WHERE key_column  =  '" + key_column + "' AND fiscal_year_id  =  '" + fiscal_year_id + "' AND plan_id  =  '" + plan_id + "';"
		return query

	def delete_fiscal_yearplanmap_by_key_column(self, key_column):
		query = "DELETE FROM fiscal_yearplanmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_fiscal_yearplanmap_by_fiscal_year_id(self, fiscal_year_id):
		query = "DELETE FROM fiscal_yearplanmap WHERE fiscal_year_id  =  '" + fiscal_year_id + "';"
		return query

	def delete_fiscal_yearplanmap_by_plan_id(self, plan_id):
		query = "DELETE FROM fiscal_yearplanmap WHERE plan_id  =  '" + plan_id + "';"
		return query

	def delete_from_red_flagconfigurationmap(self):
		query = "DELETE FROM red_flagconfigurationmap;"
		return query

	def delete_red_flagconfigurationmap(self, key_column, red_flag_id, configuration_id):
		query = "DELETE FROM red_flagconfigurationmap WHERE key_column  =  '" + key_column + "' AND red_flag_id  =  '" + red_flag_id + "' AND configuration_id  =  '" + configuration_id + "';"
		return query

	def delete_red_flagconfigurationmap_by_key_column(self, key_column):
		query = "DELETE FROM red_flagconfigurationmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_red_flagconfigurationmap_by_red_flag_id(self, red_flag_id):
		query = "DELETE FROM red_flagconfigurationmap WHERE red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_red_flagconfigurationmap_by_configuration_id(self, configuration_id):
		query = "DELETE FROM red_flagconfigurationmap WHERE configuration_id  =  '" + configuration_id + "';"
		return query

	def delete_from_procurement_stagered_flagmap(self):
		query = "DELETE FROM procurement_stagered_flagmap;"
		return query

	def delete_procurement_stagered_flagmap(self, key_column, procurement_stage_id, red_flag_id):
		query = "DELETE FROM procurement_stagered_flagmap WHERE key_column  =  '" + key_column + "' AND procurement_stage_id  =  '" + procurement_stage_id + "' AND red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_procurement_stagered_flagmap_by_key_column(self, key_column):
		query = "DELETE FROM procurement_stagered_flagmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_procurement_stagered_flagmap_by_procurement_stage_id(self, procurement_stage_id):
		query = "DELETE FROM procurement_stagered_flagmap WHERE procurement_stage_id  =  '" + procurement_stage_id + "';"
		return query

	def delete_procurement_stagered_flagmap_by_red_flag_id(self, red_flag_id):
		query = "DELETE FROM procurement_stagered_flagmap WHERE red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_from_procuring_entityred_flagmap(self):
		query = "DELETE FROM procuring_entityred_flagmap;"
		return query

	def delete_procuring_entityred_flagmap(self, key_column, procuring_entity_id, red_flag_id):
		query = "DELETE FROM procuring_entityred_flagmap WHERE key_column  =  '" + key_column + "' AND procuring_entity_id  =  '" + procuring_entity_id + "' AND red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_procuring_entityred_flagmap_by_key_column(self, key_column):
		query = "DELETE FROM procuring_entityred_flagmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_procuring_entityred_flagmap_by_procuring_entity_id(self, procuring_entity_id):
		query = "DELETE FROM procuring_entityred_flagmap WHERE procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_procuring_entityred_flagmap_by_red_flag_id(self, red_flag_id):
		query = "DELETE FROM procuring_entityred_flagmap WHERE red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_from_supplying_entityred_flagmap(self):
		query = "DELETE FROM supplying_entityred_flagmap;"
		return query

	def delete_supplying_entityred_flagmap(self, key_column, supplying_entity_id, red_flag_id):
		query = "DELETE FROM supplying_entityred_flagmap WHERE key_column  =  '" + key_column + "' AND supplying_entity_id  =  '" + supplying_entity_id + "' AND red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_supplying_entityred_flagmap_by_key_column(self, key_column):
		query = "DELETE FROM supplying_entityred_flagmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_supplying_entityred_flagmap_by_supplying_entity_id(self, supplying_entity_id):
		query = "DELETE FROM supplying_entityred_flagmap WHERE supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_supplying_entityred_flagmap_by_red_flag_id(self, red_flag_id):
		query = "DELETE FROM supplying_entityred_flagmap WHERE red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_from_procurement_typered_flagmap(self):
		query = "DELETE FROM procurement_typered_flagmap;"
		return query

	def delete_procurement_typered_flagmap(self, key_column, procurement_type_id, red_flag_id):
		query = "DELETE FROM procurement_typered_flagmap WHERE key_column  =  '" + key_column + "' AND procurement_type_id  =  '" + procurement_type_id + "' AND red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_procurement_typered_flagmap_by_key_column(self, key_column):
		query = "DELETE FROM procurement_typered_flagmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_procurement_typered_flagmap_by_procurement_type_id(self, procurement_type_id):
		query = "DELETE FROM procurement_typered_flagmap WHERE procurement_type_id  =  '" + procurement_type_id + "';"
		return query

	def delete_procurement_typered_flagmap_by_red_flag_id(self, red_flag_id):
		query = "DELETE FROM procurement_typered_flagmap WHERE red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_from_procurement_methodred_flagmap(self):
		query = "DELETE FROM procurement_methodred_flagmap;"
		return query

	def delete_procurement_methodred_flagmap(self, key_column, procurement_method_id, red_flag_id):
		query = "DELETE FROM procurement_methodred_flagmap WHERE key_column  =  '" + key_column + "' AND procurement_method_id  =  '" + procurement_method_id + "' AND red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_procurement_methodred_flagmap_by_key_column(self, key_column):
		query = "DELETE FROM procurement_methodred_flagmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_procurement_methodred_flagmap_by_procurement_method_id(self, procurement_method_id):
		query = "DELETE FROM procurement_methodred_flagmap WHERE procurement_method_id  =  '" + procurement_method_id + "';"
		return query

	def delete_procurement_methodred_flagmap_by_red_flag_id(self, red_flag_id):
		query = "DELETE FROM procurement_methodred_flagmap WHERE red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_from_tenderred_flagmap(self):
		query = "DELETE FROM tenderred_flagmap;"
		return query

	def delete_tenderred_flagmap(self, key_column, tender_id, red_flag_id):
		query = "DELETE FROM tenderred_flagmap WHERE key_column  =  '" + key_column + "' AND tender_id  =  '" + tender_id + "' AND red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_tenderred_flagmap_by_key_column(self, key_column):
		query = "DELETE FROM tenderred_flagmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_tenderred_flagmap_by_tender_id(self, tender_id):
		query = "DELETE FROM tenderred_flagmap WHERE tender_id  =  '" + tender_id + "';"
		return query

	def delete_tenderred_flagmap_by_red_flag_id(self, red_flag_id):
		query = "DELETE FROM tenderred_flagmap WHERE red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_from_bidred_flagmap(self):
		query = "DELETE FROM bidred_flagmap;"
		return query

	def delete_bidred_flagmap(self, key_column, bid_id, red_flag_id):
		query = "DELETE FROM bidred_flagmap WHERE key_column  =  '" + key_column + "' AND bid_id  =  '" + bid_id + "' AND red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_bidred_flagmap_by_key_column(self, key_column):
		query = "DELETE FROM bidred_flagmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_bidred_flagmap_by_bid_id(self, bid_id):
		query = "DELETE FROM bidred_flagmap WHERE bid_id  =  '" + bid_id + "';"
		return query

	def delete_bidred_flagmap_by_red_flag_id(self, red_flag_id):
		query = "DELETE FROM bidred_flagmap WHERE red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_from_itemred_flagmap(self):
		query = "DELETE FROM itemred_flagmap;"
		return query

	def delete_itemred_flagmap(self, key_column, item_id, red_flag_id):
		query = "DELETE FROM itemred_flagmap WHERE key_column  =  '" + key_column + "' AND item_id  =  '" + item_id + "' AND red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_itemred_flagmap_by_key_column(self, key_column):
		query = "DELETE FROM itemred_flagmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_itemred_flagmap_by_item_id(self, item_id):
		query = "DELETE FROM itemred_flagmap WHERE item_id  =  '" + item_id + "';"
		return query

	def delete_itemred_flagmap_by_red_flag_id(self, red_flag_id):
		query = "DELETE FROM itemred_flagmap WHERE red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_from_contractred_flagmap(self):
		query = "DELETE FROM contractred_flagmap;"
		return query

	def delete_contractred_flagmap(self, key_column, contract_id, red_flag_id):
		query = "DELETE FROM contractred_flagmap WHERE key_column  =  '" + key_column + "' AND contract_id  =  '" + contract_id + "' AND red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_contractred_flagmap_by_key_column(self, key_column):
		query = "DELETE FROM contractred_flagmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_contractred_flagmap_by_contract_id(self, contract_id):
		query = "DELETE FROM contractred_flagmap WHERE contract_id  =  '" + contract_id + "';"
		return query

	def delete_contractred_flagmap_by_red_flag_id(self, red_flag_id):
		query = "DELETE FROM contractred_flagmap WHERE red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_from_illicit_schemered_flagmap(self):
		query = "DELETE FROM illicit_schemered_flagmap;"
		return query

	def delete_illicit_schemered_flagmap(self, key_column, illicit_scheme_id, red_flag_id):
		query = "DELETE FROM illicit_schemered_flagmap WHERE key_column  =  '" + key_column + "' AND illicit_scheme_id  =  '" + illicit_scheme_id + "' AND red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_illicit_schemered_flagmap_by_key_column(self, key_column):
		query = "DELETE FROM illicit_schemered_flagmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_illicit_schemered_flagmap_by_illicit_scheme_id(self, illicit_scheme_id):
		query = "DELETE FROM illicit_schemered_flagmap WHERE illicit_scheme_id  =  '" + illicit_scheme_id + "';"
		return query

	def delete_illicit_schemered_flagmap_by_red_flag_id(self, red_flag_id):
		query = "DELETE FROM illicit_schemered_flagmap WHERE red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_from_bidfeemap(self):
		query = "DELETE FROM bidfeemap;"
		return query

	def delete_bidfeemap(self, key_column, bid_id, fee_id):
		query = "DELETE FROM bidfeemap WHERE key_column  =  '" + key_column + "' AND bid_id  =  '" + bid_id + "' AND fee_id  =  '" + fee_id + "';"
		return query

	def delete_bidfeemap_by_key_column(self, key_column):
		query = "DELETE FROM bidfeemap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_bidfeemap_by_bid_id(self, bid_id):
		query = "DELETE FROM bidfeemap WHERE bid_id  =  '" + bid_id + "';"
		return query

	def delete_bidfeemap_by_fee_id(self, fee_id):
		query = "DELETE FROM bidfeemap WHERE fee_id  =  '" + fee_id + "';"
		return query

	def delete_from_bidpaymentmap(self):
		query = "DELETE FROM bidpaymentmap;"
		return query

	def delete_bidpaymentmap(self, key_column, bid_id, payment_id):
		query = "DELETE FROM bidpaymentmap WHERE key_column  =  '" + key_column + "' AND bid_id  =  '" + bid_id + "' AND payment_id  =  '" + payment_id + "';"
		return query

	def delete_bidpaymentmap_by_key_column(self, key_column):
		query = "DELETE FROM bidpaymentmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_bidpaymentmap_by_bid_id(self, bid_id):
		query = "DELETE FROM bidpaymentmap WHERE bid_id  =  '" + bid_id + "';"
		return query

	def delete_bidpaymentmap_by_payment_id(self, payment_id):
		query = "DELETE FROM bidpaymentmap WHERE payment_id  =  '" + payment_id + "';"
		return query

	def delete_from_bidawardmap(self):
		query = "DELETE FROM bidawardmap;"
		return query

	def delete_bidawardmap(self, key_column, bid_id, award_id):
		query = "DELETE FROM bidawardmap WHERE key_column  =  '" + key_column + "' AND bid_id  =  '" + bid_id + "' AND award_id  =  '" + award_id + "';"
		return query

	def delete_bidawardmap_by_key_column(self, key_column):
		query = "DELETE FROM bidawardmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_bidawardmap_by_bid_id(self, bid_id):
		query = "DELETE FROM bidawardmap WHERE bid_id  =  '" + bid_id + "';"
		return query

	def delete_bidawardmap_by_award_id(self, award_id):
		query = "DELETE FROM bidawardmap WHERE award_id  =  '" + award_id + "';"
		return query

	def delete_from_tenderbidmap(self):
		query = "DELETE FROM tenderbidmap;"
		return query

	def delete_tenderbidmap(self, key_column, tender_id, bid_id):
		query = "DELETE FROM tenderbidmap WHERE key_column  =  '" + key_column + "' AND tender_id  =  '" + tender_id + "' AND bid_id  =  '" + bid_id + "';"
		return query

	def delete_tenderbidmap_by_key_column(self, key_column):
		query = "DELETE FROM tenderbidmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_tenderbidmap_by_tender_id(self, tender_id):
		query = "DELETE FROM tenderbidmap WHERE tender_id  =  '" + tender_id + "';"
		return query

	def delete_tenderbidmap_by_bid_id(self, bid_id):
		query = "DELETE FROM tenderbidmap WHERE bid_id  =  '" + bid_id + "';"
		return query

	def delete_from_tenderfeemap(self):
		query = "DELETE FROM tenderfeemap;"
		return query

	def delete_tenderfeemap(self, key_column, tender_id, fee_id):
		query = "DELETE FROM tenderfeemap WHERE key_column  =  '" + key_column + "' AND tender_id  =  '" + tender_id + "' AND fee_id  =  '" + fee_id + "';"
		return query

	def delete_tenderfeemap_by_key_column(self, key_column):
		query = "DELETE FROM tenderfeemap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_tenderfeemap_by_tender_id(self, tender_id):
		query = "DELETE FROM tenderfeemap WHERE tender_id  =  '" + tender_id + "';"
		return query

	def delete_tenderfeemap_by_fee_id(self, fee_id):
		query = "DELETE FROM tenderfeemap WHERE fee_id  =  '" + fee_id + "';"
		return query

	def delete_from_tenderpaymentmap(self):
		query = "DELETE FROM tenderpaymentmap;"
		return query

	def delete_tenderpaymentmap(self, key_column, tender_id, payment_id):
		query = "DELETE FROM tenderpaymentmap WHERE key_column  =  '" + key_column + "' AND tender_id  =  '" + tender_id + "' AND payment_id  =  '" + payment_id + "';"
		return query

	def delete_tenderpaymentmap_by_key_column(self, key_column):
		query = "DELETE FROM tenderpaymentmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_tenderpaymentmap_by_tender_id(self, tender_id):
		query = "DELETE FROM tenderpaymentmap WHERE tender_id  =  '" + tender_id + "';"
		return query

	def delete_tenderpaymentmap_by_payment_id(self, payment_id):
		query = "DELETE FROM tenderpaymentmap WHERE payment_id  =  '" + payment_id + "';"
		return query

	def delete_from_awardappealmap(self):
		query = "DELETE FROM awardappealmap;"
		return query

	def delete_awardappealmap(self, key_column, award_id, appeal_id):
		query = "DELETE FROM awardappealmap WHERE key_column  =  '" + key_column + "' AND award_id  =  '" + award_id + "' AND appeal_id  =  '" + appeal_id + "';"
		return query

	def delete_awardappealmap_by_key_column(self, key_column):
		query = "DELETE FROM awardappealmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_awardappealmap_by_award_id(self, award_id):
		query = "DELETE FROM awardappealmap WHERE award_id  =  '" + award_id + "';"
		return query

	def delete_awardappealmap_by_appeal_id(self, appeal_id):
		query = "DELETE FROM awardappealmap WHERE appeal_id  =  '" + appeal_id + "';"
		return query

	def delete_from_procuring_entityprocurement_typemap(self):
		query = "DELETE FROM procuring_entityprocurement_typemap;"
		return query

	def delete_procuring_entityprocurement_typemap(self, key_column, procuring_entity_id, procurement_type_id):
		query = "DELETE FROM procuring_entityprocurement_typemap WHERE key_column  =  '" + key_column + "' AND procuring_entity_id  =  '" + procuring_entity_id + "' AND procurement_type_id  =  '" + procurement_type_id + "';"
		return query

	def delete_procuring_entityprocurement_typemap_by_key_column(self, key_column):
		query = "DELETE FROM procuring_entityprocurement_typemap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_procuring_entityprocurement_typemap_by_procuring_entity_id(self, procuring_entity_id):
		query = "DELETE FROM procuring_entityprocurement_typemap WHERE procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_procuring_entityprocurement_typemap_by_procurement_type_id(self, procurement_type_id):
		query = "DELETE FROM procuring_entityprocurement_typemap WHERE procurement_type_id  =  '" + procurement_type_id + "';"
		return query

	def delete_from_procuring_entityprocurement_methodmap(self):
		query = "DELETE FROM procuring_entityprocurement_methodmap;"
		return query

	def delete_procuring_entityprocurement_methodmap(self, key_column, procuring_entity_id, procurement_method_id):
		query = "DELETE FROM procuring_entityprocurement_methodmap WHERE key_column  =  '" + key_column + "' AND procuring_entity_id  =  '" + procuring_entity_id + "' AND procurement_method_id  =  '" + procurement_method_id + "';"
		return query

	def delete_procuring_entityprocurement_methodmap_by_key_column(self, key_column):
		query = "DELETE FROM procuring_entityprocurement_methodmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_procuring_entityprocurement_methodmap_by_procuring_entity_id(self, procuring_entity_id):
		query = "DELETE FROM procuring_entityprocurement_methodmap WHERE procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_procuring_entityprocurement_methodmap_by_procurement_method_id(self, procurement_method_id):
		query = "DELETE FROM procuring_entityprocurement_methodmap WHERE procurement_method_id  =  '" + procurement_method_id + "';"
		return query

	def delete_from_procuring_entityprocurement_stagemap(self):
		query = "DELETE FROM procuring_entityprocurement_stagemap;"
		return query

	def delete_procuring_entityprocurement_stagemap(self, key_column, procuring_entity_id, procurement_stage_id):
		query = "DELETE FROM procuring_entityprocurement_stagemap WHERE key_column  =  '" + key_column + "' AND procuring_entity_id  =  '" + procuring_entity_id + "' AND procurement_stage_id  =  '" + procurement_stage_id + "';"
		return query

	def delete_procuring_entityprocurement_stagemap_by_key_column(self, key_column):
		query = "DELETE FROM procuring_entityprocurement_stagemap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_procuring_entityprocurement_stagemap_by_procuring_entity_id(self, procuring_entity_id):
		query = "DELETE FROM procuring_entityprocurement_stagemap WHERE procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_procuring_entityprocurement_stagemap_by_procurement_stage_id(self, procurement_stage_id):
		query = "DELETE FROM procuring_entityprocurement_stagemap WHERE procurement_stage_id  =  '" + procurement_stage_id + "';"
		return query

	def delete_from_procuring_entitybidmap(self):
		query = "DELETE FROM procuring_entitybidmap;"
		return query

	def delete_procuring_entitybidmap(self, key_column, procuring_entity_id, bid_id):
		query = "DELETE FROM procuring_entitybidmap WHERE key_column  =  '" + key_column + "' AND procuring_entity_id  =  '" + procuring_entity_id + "' AND bid_id  =  '" + bid_id + "';"
		return query

	def delete_procuring_entitybidmap_by_key_column(self, key_column):
		query = "DELETE FROM procuring_entitybidmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_procuring_entitybidmap_by_procuring_entity_id(self, procuring_entity_id):
		query = "DELETE FROM procuring_entitybidmap WHERE procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_procuring_entitybidmap_by_bid_id(self, bid_id):
		query = "DELETE FROM procuring_entitybidmap WHERE bid_id  =  '" + bid_id + "';"
		return query

	def delete_from_procuring_entitytendermap(self):
		query = "DELETE FROM procuring_entitytendermap;"
		return query

	def delete_procuring_entitytendermap(self, key_column, procuring_entity_id, tender_id):
		query = "DELETE FROM procuring_entitytendermap WHERE key_column  =  '" + key_column + "' AND procuring_entity_id  =  '" + procuring_entity_id + "' AND tender_id  =  '" + tender_id + "';"
		return query

	def delete_procuring_entitytendermap_by_key_column(self, key_column):
		query = "DELETE FROM procuring_entitytendermap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_procuring_entitytendermap_by_procuring_entity_id(self, procuring_entity_id):
		query = "DELETE FROM procuring_entitytendermap WHERE procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_procuring_entitytendermap_by_tender_id(self, tender_id):
		query = "DELETE FROM procuring_entitytendermap WHERE tender_id  =  '" + tender_id + "';"
		return query

	def delete_from_procuring_entitycontractmap(self):
		query = "DELETE FROM procuring_entitycontractmap;"
		return query

	def delete_procuring_entitycontractmap(self, key_column, procuring_entity_id, contract_id):
		query = "DELETE FROM procuring_entitycontractmap WHERE key_column  =  '" + key_column + "' AND procuring_entity_id  =  '" + procuring_entity_id + "' AND contract_id  =  '" + contract_id + "';"
		return query

	def delete_procuring_entitycontractmap_by_key_column(self, key_column):
		query = "DELETE FROM procuring_entitycontractmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_procuring_entitycontractmap_by_procuring_entity_id(self, procuring_entity_id):
		query = "DELETE FROM procuring_entitycontractmap WHERE procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_procuring_entitycontractmap_by_contract_id(self, contract_id):
		query = "DELETE FROM procuring_entitycontractmap WHERE contract_id  =  '" + contract_id + "';"
		return query

	def delete_from_procuring_entityillicit_schememap(self):
		query = "DELETE FROM procuring_entityillicit_schememap;"
		return query

	def delete_procuring_entityillicit_schememap(self, key_column, procuring_entity_id, illicit_scheme_id):
		query = "DELETE FROM procuring_entityillicit_schememap WHERE key_column  =  '" + key_column + "' AND procuring_entity_id  =  '" + procuring_entity_id + "' AND illicit_scheme_id  =  '" + illicit_scheme_id + "';"
		return query

	def delete_procuring_entityillicit_schememap_by_key_column(self, key_column):
		query = "DELETE FROM procuring_entityillicit_schememap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_procuring_entityillicit_schememap_by_procuring_entity_id(self, procuring_entity_id):
		query = "DELETE FROM procuring_entityillicit_schememap WHERE procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_procuring_entityillicit_schememap_by_illicit_scheme_id(self, illicit_scheme_id):
		query = "DELETE FROM procuring_entityillicit_schememap WHERE illicit_scheme_id  =  '" + illicit_scheme_id + "';"
		return query

	def delete_from_procuring_entityaddressmap(self):
		query = "DELETE FROM procuring_entityaddressmap;"
		return query

	def delete_procuring_entityaddressmap(self, key_column, procuring_entity_id, address_id):
		query = "DELETE FROM procuring_entityaddressmap WHERE key_column  =  '" + key_column + "' AND procuring_entity_id  =  '" + procuring_entity_id + "' AND address_id  =  '" + address_id + "';"
		return query

	def delete_procuring_entityaddressmap_by_key_column(self, key_column):
		query = "DELETE FROM procuring_entityaddressmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_procuring_entityaddressmap_by_procuring_entity_id(self, procuring_entity_id):
		query = "DELETE FROM procuring_entityaddressmap WHERE procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_procuring_entityaddressmap_by_address_id(self, address_id):
		query = "DELETE FROM procuring_entityaddressmap WHERE address_id  =  '" + address_id + "';"
		return query

	def delete_from_procuring_entityattachmentmap(self):
		query = "DELETE FROM procuring_entityattachmentmap;"
		return query

	def delete_procuring_entityattachmentmap(self, key_column, procuring_entity_id, attachment_id):
		query = "DELETE FROM procuring_entityattachmentmap WHERE key_column  =  '" + key_column + "' AND procuring_entity_id  =  '" + procuring_entity_id + "' AND attachment_id  =  '" + attachment_id + "';"
		return query

	def delete_procuring_entityattachmentmap_by_key_column(self, key_column):
		query = "DELETE FROM procuring_entityattachmentmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_procuring_entityattachmentmap_by_procuring_entity_id(self, procuring_entity_id):
		query = "DELETE FROM procuring_entityattachmentmap WHERE procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_procuring_entityattachmentmap_by_attachment_id(self, attachment_id):
		query = "DELETE FROM procuring_entityattachmentmap WHERE attachment_id  =  '" + attachment_id + "';"
		return query

	def delete_from_procuring_entityplanmap(self):
		query = "DELETE FROM procuring_entityplanmap;"
		return query

	def delete_procuring_entityplanmap(self, key_column, procuring_entity_id, plan_id):
		query = "DELETE FROM procuring_entityplanmap WHERE key_column  =  '" + key_column + "' AND procuring_entity_id  =  '" + procuring_entity_id + "' AND plan_id  =  '" + plan_id + "';"
		return query

	def delete_procuring_entityplanmap_by_key_column(self, key_column):
		query = "DELETE FROM procuring_entityplanmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_procuring_entityplanmap_by_procuring_entity_id(self, procuring_entity_id):
		query = "DELETE FROM procuring_entityplanmap WHERE procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_procuring_entityplanmap_by_plan_id(self, plan_id):
		query = "DELETE FROM procuring_entityplanmap WHERE plan_id  =  '" + plan_id + "';"
		return query

	def delete_from_procuring_entityawardmap(self):
		query = "DELETE FROM procuring_entityawardmap;"
		return query

	def delete_procuring_entityawardmap(self, key_column, procuring_entity_id, award_id):
		query = "DELETE FROM procuring_entityawardmap WHERE key_column  =  '" + key_column + "' AND procuring_entity_id  =  '" + procuring_entity_id + "' AND award_id  =  '" + award_id + "';"
		return query

	def delete_procuring_entityawardmap_by_key_column(self, key_column):
		query = "DELETE FROM procuring_entityawardmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_procuring_entityawardmap_by_procuring_entity_id(self, procuring_entity_id):
		query = "DELETE FROM procuring_entityawardmap WHERE procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_procuring_entityawardmap_by_award_id(self, award_id):
		query = "DELETE FROM procuring_entityawardmap WHERE award_id  =  '" + award_id + "';"
		return query

	def delete_from_procuring_entitycontactmap(self):
		query = "DELETE FROM procuring_entitycontactmap;"
		return query

	def delete_procuring_entitycontactmap(self, key_column, procuring_entity_id, contact_id):
		query = "DELETE FROM procuring_entitycontactmap WHERE key_column  =  '" + key_column + "' AND procuring_entity_id  =  '" + procuring_entity_id + "' AND contact_id  =  '" + contact_id + "';"
		return query

	def delete_procuring_entitycontactmap_by_key_column(self, key_column):
		query = "DELETE FROM procuring_entitycontactmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_procuring_entitycontactmap_by_procuring_entity_id(self, procuring_entity_id):
		query = "DELETE FROM procuring_entitycontactmap WHERE procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_procuring_entitycontactmap_by_contact_id(self, contact_id):
		query = "DELETE FROM procuring_entitycontactmap WHERE contact_id  =  '" + contact_id + "';"
		return query

	def delete_from_procuring_entitypaymentmap(self):
		query = "DELETE FROM procuring_entitypaymentmap;"
		return query

	def delete_procuring_entitypaymentmap(self, key_column, procuring_entity_id, payment_id):
		query = "DELETE FROM procuring_entitypaymentmap WHERE key_column  =  '" + key_column + "' AND procuring_entity_id  =  '" + procuring_entity_id + "' AND payment_id  =  '" + payment_id + "';"
		return query

	def delete_procuring_entitypaymentmap_by_key_column(self, key_column):
		query = "DELETE FROM procuring_entitypaymentmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_procuring_entitypaymentmap_by_procuring_entity_id(self, procuring_entity_id):
		query = "DELETE FROM procuring_entitypaymentmap WHERE procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_procuring_entitypaymentmap_by_payment_id(self, payment_id):
		query = "DELETE FROM procuring_entitypaymentmap WHERE payment_id  =  '" + payment_id + "';"
		return query

	def delete_from_procuring_entityuser_accountmap(self):
		query = "DELETE FROM procuring_entityuser_accountmap;"
		return query

	def delete_procuring_entityuser_accountmap(self, key_column, procuring_entity_id, user_account_id):
		query = "DELETE FROM procuring_entityuser_accountmap WHERE key_column  =  '" + key_column + "' AND procuring_entity_id  =  '" + procuring_entity_id + "' AND user_account_id  =  '" + user_account_id + "';"
		return query

	def delete_procuring_entityuser_accountmap_by_key_column(self, key_column):
		query = "DELETE FROM procuring_entityuser_accountmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_procuring_entityuser_accountmap_by_procuring_entity_id(self, procuring_entity_id):
		query = "DELETE FROM procuring_entityuser_accountmap WHERE procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_procuring_entityuser_accountmap_by_user_account_id(self, user_account_id):
		query = "DELETE FROM procuring_entityuser_accountmap WHERE user_account_id  =  '" + user_account_id + "';"
		return query

	def delete_from_procuring_entitysupplying_entitymap(self):
		query = "DELETE FROM procuring_entitysupplying_entitymap;"
		return query

	def delete_procuring_entitysupplying_entitymap(self, key_column, procuring_entity_id, supplying_entity_id):
		query = "DELETE FROM procuring_entitysupplying_entitymap WHERE key_column  =  '" + key_column + "' AND procuring_entity_id  =  '" + procuring_entity_id + "' AND supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_procuring_entitysupplying_entitymap_by_key_column(self, key_column):
		query = "DELETE FROM procuring_entitysupplying_entitymap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_procuring_entitysupplying_entitymap_by_procuring_entity_id(self, procuring_entity_id):
		query = "DELETE FROM procuring_entitysupplying_entitymap WHERE procuring_entity_id  =  '" + procuring_entity_id + "';"
		return query

	def delete_procuring_entitysupplying_entitymap_by_supplying_entity_id(self, supplying_entity_id):
		query = "DELETE FROM procuring_entitysupplying_entitymap WHERE supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_from_supplying_entityprocurement_typemap(self):
		query = "DELETE FROM supplying_entityprocurement_typemap;"
		return query

	def delete_supplying_entityprocurement_typemap(self, key_column, supplying_entity_id, procurement_type_id):
		query = "DELETE FROM supplying_entityprocurement_typemap WHERE key_column  =  '" + key_column + "' AND supplying_entity_id  =  '" + supplying_entity_id + "' AND procurement_type_id  =  '" + procurement_type_id + "';"
		return query

	def delete_supplying_entityprocurement_typemap_by_key_column(self, key_column):
		query = "DELETE FROM supplying_entityprocurement_typemap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_supplying_entityprocurement_typemap_by_supplying_entity_id(self, supplying_entity_id):
		query = "DELETE FROM supplying_entityprocurement_typemap WHERE supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_supplying_entityprocurement_typemap_by_procurement_type_id(self, procurement_type_id):
		query = "DELETE FROM supplying_entityprocurement_typemap WHERE procurement_type_id  =  '" + procurement_type_id + "';"
		return query

	def delete_from_supplying_entityprocurement_methodmap(self):
		query = "DELETE FROM supplying_entityprocurement_methodmap;"
		return query

	def delete_supplying_entityprocurement_methodmap(self, key_column, supplying_entity_id, procurement_method_id):
		query = "DELETE FROM supplying_entityprocurement_methodmap WHERE key_column  =  '" + key_column + "' AND supplying_entity_id  =  '" + supplying_entity_id + "' AND procurement_method_id  =  '" + procurement_method_id + "';"
		return query

	def delete_supplying_entityprocurement_methodmap_by_key_column(self, key_column):
		query = "DELETE FROM supplying_entityprocurement_methodmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_supplying_entityprocurement_methodmap_by_supplying_entity_id(self, supplying_entity_id):
		query = "DELETE FROM supplying_entityprocurement_methodmap WHERE supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_supplying_entityprocurement_methodmap_by_procurement_method_id(self, procurement_method_id):
		query = "DELETE FROM supplying_entityprocurement_methodmap WHERE procurement_method_id  =  '" + procurement_method_id + "';"
		return query

	def delete_from_supplying_entityprocurement_stagemap(self):
		query = "DELETE FROM supplying_entityprocurement_stagemap;"
		return query

	def delete_supplying_entityprocurement_stagemap(self, key_column, supplying_entity_id, procurement_stage_id):
		query = "DELETE FROM supplying_entityprocurement_stagemap WHERE key_column  =  '" + key_column + "' AND supplying_entity_id  =  '" + supplying_entity_id + "' AND procurement_stage_id  =  '" + procurement_stage_id + "';"
		return query

	def delete_supplying_entityprocurement_stagemap_by_key_column(self, key_column):
		query = "DELETE FROM supplying_entityprocurement_stagemap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_supplying_entityprocurement_stagemap_by_supplying_entity_id(self, supplying_entity_id):
		query = "DELETE FROM supplying_entityprocurement_stagemap WHERE supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_supplying_entityprocurement_stagemap_by_procurement_stage_id(self, procurement_stage_id):
		query = "DELETE FROM supplying_entityprocurement_stagemap WHERE procurement_stage_id  =  '" + procurement_stage_id + "';"
		return query

	def delete_from_supplying_entitybidmap(self):
		query = "DELETE FROM supplying_entitybidmap;"
		return query

	def delete_supplying_entitybidmap(self, key_column, supplying_entity_id, bid_id):
		query = "DELETE FROM supplying_entitybidmap WHERE key_column  =  '" + key_column + "' AND supplying_entity_id  =  '" + supplying_entity_id + "' AND bid_id  =  '" + bid_id + "';"
		return query

	def delete_supplying_entitybidmap_by_key_column(self, key_column):
		query = "DELETE FROM supplying_entitybidmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_supplying_entitybidmap_by_supplying_entity_id(self, supplying_entity_id):
		query = "DELETE FROM supplying_entitybidmap WHERE supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_supplying_entitybidmap_by_bid_id(self, bid_id):
		query = "DELETE FROM supplying_entitybidmap WHERE bid_id  =  '" + bid_id + "';"
		return query

	def delete_from_supplying_entitytendermap(self):
		query = "DELETE FROM supplying_entitytendermap;"
		return query

	def delete_supplying_entitytendermap(self, key_column, supplying_entity_id, tender_id):
		query = "DELETE FROM supplying_entitytendermap WHERE key_column  =  '" + key_column + "' AND supplying_entity_id  =  '" + supplying_entity_id + "' AND tender_id  =  '" + tender_id + "';"
		return query

	def delete_supplying_entitytendermap_by_key_column(self, key_column):
		query = "DELETE FROM supplying_entitytendermap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_supplying_entitytendermap_by_supplying_entity_id(self, supplying_entity_id):
		query = "DELETE FROM supplying_entitytendermap WHERE supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_supplying_entitytendermap_by_tender_id(self, tender_id):
		query = "DELETE FROM supplying_entitytendermap WHERE tender_id  =  '" + tender_id + "';"
		return query

	def delete_from_supplying_entitycontractmap(self):
		query = "DELETE FROM supplying_entitycontractmap;"
		return query

	def delete_supplying_entitycontractmap(self, key_column, supplying_entity_id, contract_id):
		query = "DELETE FROM supplying_entitycontractmap WHERE key_column  =  '" + key_column + "' AND supplying_entity_id  =  '" + supplying_entity_id + "' AND contract_id  =  '" + contract_id + "';"
		return query

	def delete_supplying_entitycontractmap_by_key_column(self, key_column):
		query = "DELETE FROM supplying_entitycontractmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_supplying_entitycontractmap_by_supplying_entity_id(self, supplying_entity_id):
		query = "DELETE FROM supplying_entitycontractmap WHERE supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_supplying_entitycontractmap_by_contract_id(self, contract_id):
		query = "DELETE FROM supplying_entitycontractmap WHERE contract_id  =  '" + contract_id + "';"
		return query

	def delete_from_supplying_entityillicit_schememap(self):
		query = "DELETE FROM supplying_entityillicit_schememap;"
		return query

	def delete_supplying_entityillicit_schememap(self, key_column, supplying_entity_id, illicit_scheme_id):
		query = "DELETE FROM supplying_entityillicit_schememap WHERE key_column  =  '" + key_column + "' AND supplying_entity_id  =  '" + supplying_entity_id + "' AND illicit_scheme_id  =  '" + illicit_scheme_id + "';"
		return query

	def delete_supplying_entityillicit_schememap_by_key_column(self, key_column):
		query = "DELETE FROM supplying_entityillicit_schememap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_supplying_entityillicit_schememap_by_supplying_entity_id(self, supplying_entity_id):
		query = "DELETE FROM supplying_entityillicit_schememap WHERE supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_supplying_entityillicit_schememap_by_illicit_scheme_id(self, illicit_scheme_id):
		query = "DELETE FROM supplying_entityillicit_schememap WHERE illicit_scheme_id  =  '" + illicit_scheme_id + "';"
		return query

	def delete_from_supplying_entityaddressmap(self):
		query = "DELETE FROM supplying_entityaddressmap;"
		return query

	def delete_supplying_entityaddressmap(self, key_column, supplying_entity_id, address_id):
		query = "DELETE FROM supplying_entityaddressmap WHERE key_column  =  '" + key_column + "' AND supplying_entity_id  =  '" + supplying_entity_id + "' AND address_id  =  '" + address_id + "';"
		return query

	def delete_supplying_entityaddressmap_by_key_column(self, key_column):
		query = "DELETE FROM supplying_entityaddressmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_supplying_entityaddressmap_by_supplying_entity_id(self, supplying_entity_id):
		query = "DELETE FROM supplying_entityaddressmap WHERE supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_supplying_entityaddressmap_by_address_id(self, address_id):
		query = "DELETE FROM supplying_entityaddressmap WHERE address_id  =  '" + address_id + "';"
		return query

	def delete_from_supplying_entityattachmentmap(self):
		query = "DELETE FROM supplying_entityattachmentmap;"
		return query

	def delete_supplying_entityattachmentmap(self, key_column, supplying_entity_id, attachment_id):
		query = "DELETE FROM supplying_entityattachmentmap WHERE key_column  =  '" + key_column + "' AND supplying_entity_id  =  '" + supplying_entity_id + "' AND attachment_id  =  '" + attachment_id + "';"
		return query

	def delete_supplying_entityattachmentmap_by_key_column(self, key_column):
		query = "DELETE FROM supplying_entityattachmentmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_supplying_entityattachmentmap_by_supplying_entity_id(self, supplying_entity_id):
		query = "DELETE FROM supplying_entityattachmentmap WHERE supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_supplying_entityattachmentmap_by_attachment_id(self, attachment_id):
		query = "DELETE FROM supplying_entityattachmentmap WHERE attachment_id  =  '" + attachment_id + "';"
		return query

	def delete_from_supplying_entityawardmap(self):
		query = "DELETE FROM supplying_entityawardmap;"
		return query

	def delete_supplying_entityawardmap(self, key_column, supplying_entity_id, award_id):
		query = "DELETE FROM supplying_entityawardmap WHERE key_column  =  '" + key_column + "' AND supplying_entity_id  =  '" + supplying_entity_id + "' AND award_id  =  '" + award_id + "';"
		return query

	def delete_supplying_entityawardmap_by_key_column(self, key_column):
		query = "DELETE FROM supplying_entityawardmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_supplying_entityawardmap_by_supplying_entity_id(self, supplying_entity_id):
		query = "DELETE FROM supplying_entityawardmap WHERE supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_supplying_entityawardmap_by_award_id(self, award_id):
		query = "DELETE FROM supplying_entityawardmap WHERE award_id  =  '" + award_id + "';"
		return query

	def delete_from_supplying_entitycontactmap(self):
		query = "DELETE FROM supplying_entitycontactmap;"
		return query

	def delete_supplying_entitycontactmap(self, key_column, supplying_entity_id, contact_id):
		query = "DELETE FROM supplying_entitycontactmap WHERE key_column  =  '" + key_column + "' AND supplying_entity_id  =  '" + supplying_entity_id + "' AND contact_id  =  '" + contact_id + "';"
		return query

	def delete_supplying_entitycontactmap_by_key_column(self, key_column):
		query = "DELETE FROM supplying_entitycontactmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_supplying_entitycontactmap_by_supplying_entity_id(self, supplying_entity_id):
		query = "DELETE FROM supplying_entitycontactmap WHERE supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_supplying_entitycontactmap_by_contact_id(self, contact_id):
		query = "DELETE FROM supplying_entitycontactmap WHERE contact_id  =  '" + contact_id + "';"
		return query

	def delete_from_supplying_entitypaymentmap(self):
		query = "DELETE FROM supplying_entitypaymentmap;"
		return query

	def delete_supplying_entitypaymentmap(self, key_column, supplying_entity_id, payment_id):
		query = "DELETE FROM supplying_entitypaymentmap WHERE key_column  =  '" + key_column + "' AND supplying_entity_id  =  '" + supplying_entity_id + "' AND payment_id  =  '" + payment_id + "';"
		return query

	def delete_supplying_entitypaymentmap_by_key_column(self, key_column):
		query = "DELETE FROM supplying_entitypaymentmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_supplying_entitypaymentmap_by_supplying_entity_id(self, supplying_entity_id):
		query = "DELETE FROM supplying_entitypaymentmap WHERE supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_supplying_entitypaymentmap_by_payment_id(self, payment_id):
		query = "DELETE FROM supplying_entitypaymentmap WHERE payment_id  =  '" + payment_id + "';"
		return query

	def delete_from_supplying_entityuser_accountmap(self):
		query = "DELETE FROM supplying_entityuser_accountmap;"
		return query

	def delete_supplying_entityuser_accountmap(self, key_column, supplying_entity_id, user_account_id):
		query = "DELETE FROM supplying_entityuser_accountmap WHERE key_column  =  '" + key_column + "' AND supplying_entity_id  =  '" + supplying_entity_id + "' AND user_account_id  =  '" + user_account_id + "';"
		return query

	def delete_supplying_entityuser_accountmap_by_key_column(self, key_column):
		query = "DELETE FROM supplying_entityuser_accountmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_supplying_entityuser_accountmap_by_supplying_entity_id(self, supplying_entity_id):
		query = "DELETE FROM supplying_entityuser_accountmap WHERE supplying_entity_id  =  '" + supplying_entity_id + "';"
		return query

	def delete_supplying_entityuser_accountmap_by_user_account_id(self, user_account_id):
		query = "DELETE FROM supplying_entityuser_accountmap WHERE user_account_id  =  '" + user_account_id + "';"
		return query

	def delete_from_contractawardmap(self):
		query = "DELETE FROM contractawardmap;"
		return query

	def delete_contractawardmap(self, key_column, contract_id, award_id):
		query = "DELETE FROM contractawardmap WHERE key_column  =  '" + key_column + "' AND contract_id  =  '" + contract_id + "' AND award_id  =  '" + award_id + "';"
		return query

	def delete_contractawardmap_by_key_column(self, key_column):
		query = "DELETE FROM contractawardmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_contractawardmap_by_contract_id(self, contract_id):
		query = "DELETE FROM contractawardmap WHERE contract_id  =  '" + contract_id + "';"
		return query

	def delete_contractawardmap_by_award_id(self, award_id):
		query = "DELETE FROM contractawardmap WHERE award_id  =  '" + award_id + "';"
		return query

	def delete_from_paymentfeemap(self):
		query = "DELETE FROM paymentfeemap;"
		return query

	def delete_paymentfeemap(self, key_column, payment_id, fee_id):
		query = "DELETE FROM paymentfeemap WHERE key_column  =  '" + key_column + "' AND payment_id  =  '" + payment_id + "' AND fee_id  =  '" + fee_id + "';"
		return query

	def delete_paymentfeemap_by_key_column(self, key_column):
		query = "DELETE FROM paymentfeemap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_paymentfeemap_by_payment_id(self, payment_id):
		query = "DELETE FROM paymentfeemap WHERE payment_id  =  '" + payment_id + "';"
		return query

	def delete_paymentfeemap_by_fee_id(self, fee_id):
		query = "DELETE FROM paymentfeemap WHERE fee_id  =  '" + fee_id + "';"
		return query

	def delete_from_alert_authorityuser_accountmap(self):
		query = "DELETE FROM alert_authorityuser_accountmap;"
		return query

	def delete_alert_authorityuser_accountmap(self, key_column, alert_authority_id, user_account_id):
		query = "DELETE FROM alert_authorityuser_accountmap WHERE key_column  =  '" + key_column + "' AND alert_authority_id  =  '" + alert_authority_id + "' AND user_account_id  =  '" + user_account_id + "';"
		return query

	def delete_alert_authorityuser_accountmap_by_key_column(self, key_column):
		query = "DELETE FROM alert_authorityuser_accountmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_alert_authorityuser_accountmap_by_alert_authority_id(self, alert_authority_id):
		query = "DELETE FROM alert_authorityuser_accountmap WHERE alert_authority_id  =  '" + alert_authority_id + "';"
		return query

	def delete_alert_authorityuser_accountmap_by_user_account_id(self, user_account_id):
		query = "DELETE FROM alert_authorityuser_accountmap WHERE user_account_id  =  '" + user_account_id + "';"
		return query

	def delete_from_alert_authorityalert_levelmap(self):
		query = "DELETE FROM alert_authorityalert_levelmap;"
		return query

	def delete_alert_authorityalert_levelmap(self, key_column, alert_authority_id, alert_level_id):
		query = "DELETE FROM alert_authorityalert_levelmap WHERE key_column  =  '" + key_column + "' AND alert_authority_id  =  '" + alert_authority_id + "' AND alert_level_id  =  '" + alert_level_id + "';"
		return query

	def delete_alert_authorityalert_levelmap_by_key_column(self, key_column):
		query = "DELETE FROM alert_authorityalert_levelmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_alert_authorityalert_levelmap_by_alert_authority_id(self, alert_authority_id):
		query = "DELETE FROM alert_authorityalert_levelmap WHERE alert_authority_id  =  '" + alert_authority_id + "';"
		return query

	def delete_alert_authorityalert_levelmap_by_alert_level_id(self, alert_level_id):
		query = "DELETE FROM alert_authorityalert_levelmap WHERE alert_level_id  =  '" + alert_level_id + "';"
		return query

	def delete_from_alert_authorityalertmap(self):
		query = "DELETE FROM alert_authorityalertmap;"
		return query

	def delete_alert_authorityalertmap(self, key_column, alert_authority_id, alert_id):
		query = "DELETE FROM alert_authorityalertmap WHERE key_column  =  '" + key_column + "' AND alert_authority_id  =  '" + alert_authority_id + "' AND alert_id  =  '" + alert_id + "';"
		return query

	def delete_alert_authorityalertmap_by_key_column(self, key_column):
		query = "DELETE FROM alert_authorityalertmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_alert_authorityalertmap_by_alert_authority_id(self, alert_authority_id):
		query = "DELETE FROM alert_authorityalertmap WHERE alert_authority_id  =  '" + alert_authority_id + "';"
		return query

	def delete_alert_authorityalertmap_by_alert_id(self, alert_id):
		query = "DELETE FROM alert_authorityalertmap WHERE alert_id  =  '" + alert_id + "';"
		return query

	def delete_from_alert_authorityaddressmap(self):
		query = "DELETE FROM alert_authorityaddressmap;"
		return query

	def delete_alert_authorityaddressmap(self, key_column, alert_authority_id, address_id):
		query = "DELETE FROM alert_authorityaddressmap WHERE key_column  =  '" + key_column + "' AND alert_authority_id  =  '" + alert_authority_id + "' AND address_id  =  '" + address_id + "';"
		return query

	def delete_alert_authorityaddressmap_by_key_column(self, key_column):
		query = "DELETE FROM alert_authorityaddressmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_alert_authorityaddressmap_by_alert_authority_id(self, alert_authority_id):
		query = "DELETE FROM alert_authorityaddressmap WHERE alert_authority_id  =  '" + alert_authority_id + "';"
		return query

	def delete_alert_authorityaddressmap_by_address_id(self, address_id):
		query = "DELETE FROM alert_authorityaddressmap WHERE address_id  =  '" + address_id + "';"
		return query

	def delete_from_alert_leveluser_accountmap(self):
		query = "DELETE FROM alert_leveluser_accountmap;"
		return query

	def delete_alert_leveluser_accountmap(self, key_column, alert_level_id, user_account_id):
		query = "DELETE FROM alert_leveluser_accountmap WHERE key_column  =  '" + key_column + "' AND alert_level_id  =  '" + alert_level_id + "' AND user_account_id  =  '" + user_account_id + "';"
		return query

	def delete_alert_leveluser_accountmap_by_key_column(self, key_column):
		query = "DELETE FROM alert_leveluser_accountmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_alert_leveluser_accountmap_by_alert_level_id(self, alert_level_id):
		query = "DELETE FROM alert_leveluser_accountmap WHERE alert_level_id  =  '" + alert_level_id + "';"
		return query

	def delete_alert_leveluser_accountmap_by_user_account_id(self, user_account_id):
		query = "DELETE FROM alert_leveluser_accountmap WHERE user_account_id  =  '" + user_account_id + "';"
		return query

	def delete_from_alert_levelred_flagmap(self):
		query = "DELETE FROM alert_levelred_flagmap;"
		return query

	def delete_alert_levelred_flagmap(self, key_column, alert_level_id, red_flag_id):
		query = "DELETE FROM alert_levelred_flagmap WHERE key_column  =  '" + key_column + "' AND alert_level_id  =  '" + alert_level_id + "' AND red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_alert_levelred_flagmap_by_key_column(self, key_column):
		query = "DELETE FROM alert_levelred_flagmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_alert_levelred_flagmap_by_alert_level_id(self, alert_level_id):
		query = "DELETE FROM alert_levelred_flagmap WHERE alert_level_id  =  '" + alert_level_id + "';"
		return query

	def delete_alert_levelred_flagmap_by_red_flag_id(self, red_flag_id):
		query = "DELETE FROM alert_levelred_flagmap WHERE red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_from_alert_leveladdressmap(self):
		query = "DELETE FROM alert_leveladdressmap;"
		return query

	def delete_alert_leveladdressmap(self, key_column, alert_level_id, address_id):
		query = "DELETE FROM alert_leveladdressmap WHERE key_column  =  '" + key_column + "' AND alert_level_id  =  '" + alert_level_id + "' AND address_id  =  '" + address_id + "';"
		return query

	def delete_alert_leveladdressmap_by_key_column(self, key_column):
		query = "DELETE FROM alert_leveladdressmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_alert_leveladdressmap_by_alert_level_id(self, alert_level_id):
		query = "DELETE FROM alert_leveladdressmap WHERE alert_level_id  =  '" + alert_level_id + "';"
		return query

	def delete_alert_leveladdressmap_by_address_id(self, address_id):
		query = "DELETE FROM alert_leveladdressmap WHERE address_id  =  '" + address_id + "';"
		return query

	def delete_from_alertred_flagmap(self):
		query = "DELETE FROM alertred_flagmap;"
		return query

	def delete_alertred_flagmap(self, key_column, alert_id, red_flag_id):
		query = "DELETE FROM alertred_flagmap WHERE key_column  =  '" + key_column + "' AND alert_id  =  '" + alert_id + "' AND red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_alertred_flagmap_by_key_column(self, key_column):
		query = "DELETE FROM alertred_flagmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_alertred_flagmap_by_alert_id(self, alert_id):
		query = "DELETE FROM alertred_flagmap WHERE alert_id  =  '" + alert_id + "';"
		return query

	def delete_alertred_flagmap_by_red_flag_id(self, red_flag_id):
		query = "DELETE FROM alertred_flagmap WHERE red_flag_id  =  '" + red_flag_id + "';"
		return query

	def delete_from_alertattachmentmap(self):
		query = "DELETE FROM alertattachmentmap;"
		return query

	def delete_alertattachmentmap(self, key_column, alert_id, attachment_id):
		query = "DELETE FROM alertattachmentmap WHERE key_column  =  '" + key_column + "' AND alert_id  =  '" + alert_id + "' AND attachment_id  =  '" + attachment_id + "';"
		return query

	def delete_alertattachmentmap_by_key_column(self, key_column):
		query = "DELETE FROM alertattachmentmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_alertattachmentmap_by_alert_id(self, alert_id):
		query = "DELETE FROM alertattachmentmap WHERE alert_id  =  '" + alert_id + "';"
		return query

	def delete_alertattachmentmap_by_attachment_id(self, attachment_id):
		query = "DELETE FROM alertattachmentmap WHERE attachment_id  =  '" + attachment_id + "';"
		return query

	def delete_from_alert_authoritycontactmap(self):
		query = "DELETE FROM alert_authoritycontactmap;"
		return query

	def delete_alert_authoritycontactmap(self, key_column, alert_authority_id, contact_id):
		query = "DELETE FROM alert_authoritycontactmap WHERE key_column  =  '" + key_column + "' AND alert_authority_id  =  '" + alert_authority_id + "' AND contact_id  =  '" + contact_id + "';"
		return query

	def delete_alert_authoritycontactmap_by_key_column(self, key_column):
		query = "DELETE FROM alert_authoritycontactmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_alert_authoritycontactmap_by_alert_authority_id(self, alert_authority_id):
		query = "DELETE FROM alert_authoritycontactmap WHERE alert_authority_id  =  '" + alert_authority_id + "';"
		return query

	def delete_alert_authoritycontactmap_by_contact_id(self, contact_id):
		query = "DELETE FROM alert_authoritycontactmap WHERE contact_id  =  '" + contact_id + "';"
		return query

	def delete_from_alert_levelcontactmap(self):
		query = "DELETE FROM alert_levelcontactmap;"
		return query

	def delete_alert_levelcontactmap(self, key_column, alert_level_id, contact_id):
		query = "DELETE FROM alert_levelcontactmap WHERE key_column  =  '" + key_column + "' AND alert_level_id  =  '" + alert_level_id + "' AND contact_id  =  '" + contact_id + "';"
		return query

	def delete_alert_levelcontactmap_by_key_column(self, key_column):
		query = "DELETE FROM alert_levelcontactmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_alert_levelcontactmap_by_alert_level_id(self, alert_level_id):
		query = "DELETE FROM alert_levelcontactmap WHERE alert_level_id  =  '" + alert_level_id + "';"
		return query

	def delete_alert_levelcontactmap_by_contact_id(self, contact_id):
		query = "DELETE FROM alert_levelcontactmap WHERE contact_id  =  '" + contact_id + "';"
		return query

	def delete_from_user_accountcontactmap(self):
		query = "DELETE FROM user_accountcontactmap;"
		return query

	def delete_user_accountcontactmap(self, key_column, user_account_id, contact_id):
		query = "DELETE FROM user_accountcontactmap WHERE key_column  =  '" + key_column + "' AND user_account_id  =  '" + user_account_id + "' AND contact_id  =  '" + contact_id + "';"
		return query

	def delete_user_accountcontactmap_by_key_column(self, key_column):
		query = "DELETE FROM user_accountcontactmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_user_accountcontactmap_by_user_account_id(self, user_account_id):
		query = "DELETE FROM user_accountcontactmap WHERE user_account_id  =  '" + user_account_id + "';"
		return query

	def delete_user_accountcontactmap_by_contact_id(self, contact_id):
		query = "DELETE FROM user_accountcontactmap WHERE contact_id  =  '" + contact_id + "';"
		return query

	def delete_from_user_accountaddressmap(self):
		query = "DELETE FROM user_accountaddressmap;"
		return query

	def delete_user_accountaddressmap(self, key_column, user_account_id, address_id):
		query = "DELETE FROM user_accountaddressmap WHERE key_column  =  '" + key_column + "' AND user_account_id  =  '" + user_account_id + "' AND address_id  =  '" + address_id + "';"
		return query

	def delete_user_accountaddressmap_by_key_column(self, key_column):
		query = "DELETE FROM user_accountaddressmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_user_accountaddressmap_by_user_account_id(self, user_account_id):
		query = "DELETE FROM user_accountaddressmap WHERE user_account_id  =  '" + user_account_id + "';"
		return query

	def delete_user_accountaddressmap_by_address_id(self, address_id):
		query = "DELETE FROM user_accountaddressmap WHERE address_id  =  '" + address_id + "';"
		return query

	def delete_from_user_accountsubmissionmap(self):
		query = "DELETE FROM user_accountsubmissionmap;"
		return query

	def delete_user_accountsubmissionmap(self, key_column, user_account_id, submission_id):
		query = "DELETE FROM user_accountsubmissionmap WHERE key_column  =  '" + key_column + "' AND user_account_id  =  '" + user_account_id + "' AND submission_id  =  '" + submission_id + "';"
		return query

	def delete_user_accountsubmissionmap_by_key_column(self, key_column):
		query = "DELETE FROM user_accountsubmissionmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_user_accountsubmissionmap_by_user_account_id(self, user_account_id):
		query = "DELETE FROM user_accountsubmissionmap WHERE user_account_id  =  '" + user_account_id + "';"
		return query

	def delete_user_accountsubmissionmap_by_submission_id(self, submission_id):
		query = "DELETE FROM user_accountsubmissionmap WHERE submission_id  =  '" + submission_id + "';"
		return query

	def delete_from_procurement_stagesubmissionmap(self):
		query = "DELETE FROM procurement_stagesubmissionmap;"
		return query

	def delete_procurement_stagesubmissionmap(self, key_column, procurement_stage_id, submission_id):
		query = "DELETE FROM procurement_stagesubmissionmap WHERE key_column  =  '" + key_column + "' AND procurement_stage_id  =  '" + procurement_stage_id + "' AND submission_id  =  '" + submission_id + "';"
		return query

	def delete_procurement_stagesubmissionmap_by_key_column(self, key_column):
		query = "DELETE FROM procurement_stagesubmissionmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_procurement_stagesubmissionmap_by_procurement_stage_id(self, procurement_stage_id):
		query = "DELETE FROM procurement_stagesubmissionmap WHERE procurement_stage_id  =  '" + procurement_stage_id + "';"
		return query

	def delete_procurement_stagesubmissionmap_by_submission_id(self, submission_id):
		query = "DELETE FROM procurement_stagesubmissionmap WHERE submission_id  =  '" + submission_id + "';"
		return query

	def delete_from_plansubmissionmap(self):
		query = "DELETE FROM plansubmissionmap;"
		return query

	def delete_plansubmissionmap(self, key_column, plan_id, submission_id):
		query = "DELETE FROM plansubmissionmap WHERE key_column  =  '" + key_column + "' AND plan_id  =  '" + plan_id + "' AND submission_id  =  '" + submission_id + "';"
		return query

	def delete_plansubmissionmap_by_key_column(self, key_column):
		query = "DELETE FROM plansubmissionmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_plansubmissionmap_by_plan_id(self, plan_id):
		query = "DELETE FROM plansubmissionmap WHERE plan_id  =  '" + plan_id + "';"
		return query

	def delete_plansubmissionmap_by_submission_id(self, submission_id):
		query = "DELETE FROM plansubmissionmap WHERE submission_id  =  '" + submission_id + "';"
		return query

	def delete_from_submissionattachmentmap(self):
		query = "DELETE FROM submissionattachmentmap;"
		return query

	def delete_submissionattachmentmap(self, key_column, submission_id, attachment_id):
		query = "DELETE FROM submissionattachmentmap WHERE key_column  =  '" + key_column + "' AND submission_id  =  '" + submission_id + "' AND attachment_id  =  '" + attachment_id + "';"
		return query

	def delete_submissionattachmentmap_by_key_column(self, key_column):
		query = "DELETE FROM submissionattachmentmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_submissionattachmentmap_by_submission_id(self, submission_id):
		query = "DELETE FROM submissionattachmentmap WHERE submission_id  =  '" + submission_id + "';"
		return query

	def delete_submissionattachmentmap_by_attachment_id(self, attachment_id):
		query = "DELETE FROM submissionattachmentmap WHERE attachment_id  =  '" + attachment_id + "';"
		return query

	def delete_from_appealattachmentmap(self):
		query = "DELETE FROM appealattachmentmap;"
		return query

	def delete_appealattachmentmap(self, key_column, appeal_id, attachment_id):
		query = "DELETE FROM appealattachmentmap WHERE key_column  =  '" + key_column + "' AND appeal_id  =  '" + appeal_id + "' AND attachment_id  =  '" + attachment_id + "';"
		return query

	def delete_appealattachmentmap_by_key_column(self, key_column):
		query = "DELETE FROM appealattachmentmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_appealattachmentmap_by_appeal_id(self, appeal_id):
		query = "DELETE FROM appealattachmentmap WHERE appeal_id  =  '" + appeal_id + "';"
		return query

	def delete_appealattachmentmap_by_attachment_id(self, attachment_id):
		query = "DELETE FROM appealattachmentmap WHERE attachment_id  =  '" + attachment_id + "';"
		return query

	def delete_from_user_accountattachmentmap(self):
		query = "DELETE FROM user_accountattachmentmap;"
		return query

	def delete_user_accountattachmentmap(self, key_column, user_account_id, attachment_id):
		query = "DELETE FROM user_accountattachmentmap WHERE key_column  =  '" + key_column + "' AND user_account_id  =  '" + user_account_id + "' AND attachment_id  =  '" + attachment_id + "';"
		return query

	def delete_user_accountattachmentmap_by_key_column(self, key_column):
		query = "DELETE FROM user_accountattachmentmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_user_accountattachmentmap_by_user_account_id(self, user_account_id):
		query = "DELETE FROM user_accountattachmentmap WHERE user_account_id  =  '" + user_account_id + "';"
		return query

	def delete_user_accountattachmentmap_by_attachment_id(self, attachment_id):
		query = "DELETE FROM user_accountattachmentmap WHERE attachment_id  =  '" + attachment_id + "';"
		return query

	def delete_from_awardsubmissionmap(self):
		query = "DELETE FROM awardsubmissionmap;"
		return query

	def delete_awardsubmissionmap(self, key_column, award_id, submission_id):
		query = "DELETE FROM awardsubmissionmap WHERE key_column  =  '" + key_column + "' AND award_id  =  '" + award_id + "' AND submission_id  =  '" + submission_id + "';"
		return query

	def delete_awardsubmissionmap_by_key_column(self, key_column):
		query = "DELETE FROM awardsubmissionmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_awardsubmissionmap_by_award_id(self, award_id):
		query = "DELETE FROM awardsubmissionmap WHERE award_id  =  '" + award_id + "';"
		return query

	def delete_awardsubmissionmap_by_submission_id(self, submission_id):
		query = "DELETE FROM awardsubmissionmap WHERE submission_id  =  '" + submission_id + "';"
		return query

	def delete_from_user_accountplanmap(self):
		query = "DELETE FROM user_accountplanmap;"
		return query

	def delete_user_accountplanmap(self, key_column, user_account_id, plan_id):
		query = "DELETE FROM user_accountplanmap WHERE key_column  =  '" + key_column + "' AND user_account_id  =  '" + user_account_id + "' AND plan_id  =  '" + plan_id + "';"
		return query

	def delete_user_accountplanmap_by_key_column(self, key_column):
		query = "DELETE FROM user_accountplanmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_user_accountplanmap_by_user_account_id(self, user_account_id):
		query = "DELETE FROM user_accountplanmap WHERE user_account_id  =  '" + user_account_id + "';"
		return query

	def delete_user_accountplanmap_by_plan_id(self, plan_id):
		query = "DELETE FROM user_accountplanmap WHERE plan_id  =  '" + plan_id + "';"
		return query

	def delete_from_awardtendermap(self):
		query = "DELETE FROM awardtendermap;"
		return query

	def delete_awardtendermap(self, key_column, award_id, tender_id):
		query = "DELETE FROM awardtendermap WHERE key_column  =  '" + key_column + "' AND award_id  =  '" + award_id + "' AND tender_id  =  '" + tender_id + "';"
		return query

	def delete_awardtendermap_by_key_column(self, key_column):
		query = "DELETE FROM awardtendermap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_awardtendermap_by_award_id(self, award_id):
		query = "DELETE FROM awardtendermap WHERE award_id  =  '" + award_id + "';"
		return query

	def delete_awardtendermap_by_tender_id(self, tender_id):
		query = "DELETE FROM awardtendermap WHERE tender_id  =  '" + tender_id + "';"
		return query

	def delete_from_bidsubmissionmap(self):
		query = "DELETE FROM bidsubmissionmap;"
		return query

	def delete_bidsubmissionmap(self, key_column, bid_id, submission_id):
		query = "DELETE FROM bidsubmissionmap WHERE key_column  =  '" + key_column + "' AND bid_id  =  '" + bid_id + "' AND submission_id  =  '" + submission_id + "';"
		return query

	def delete_bidsubmissionmap_by_key_column(self, key_column):
		query = "DELETE FROM bidsubmissionmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_bidsubmissionmap_by_bid_id(self, bid_id):
		query = "DELETE FROM bidsubmissionmap WHERE bid_id  =  '" + bid_id + "';"
		return query

	def delete_bidsubmissionmap_by_submission_id(self, submission_id):
		query = "DELETE FROM bidsubmissionmap WHERE submission_id  =  '" + submission_id + "';"
		return query

	def delete_from_tenderappealmap(self):
		query = "DELETE FROM tenderappealmap;"
		return query

	def delete_tenderappealmap(self, key_column, tender_id, appeal_id):
		query = "DELETE FROM tenderappealmap WHERE key_column  =  '" + key_column + "' AND tender_id  =  '" + tender_id + "' AND appeal_id  =  '" + appeal_id + "';"
		return query

	def delete_tenderappealmap_by_key_column(self, key_column):
		query = "DELETE FROM tenderappealmap WHERE key_column  =  '" + key_column + "';"
		return query

	def delete_tenderappealmap_by_tender_id(self, tender_id):
		query = "DELETE FROM tenderappealmap WHERE tender_id  =  '" + tender_id + "';"
		return query

	def delete_tenderappealmap_by_appeal_id(self, appeal_id):
		query = "DELETE FROM tenderappealmap WHERE appeal_id  =  '" + appeal_id + "';"
		return query




