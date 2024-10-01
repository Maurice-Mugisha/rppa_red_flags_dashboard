


class Update:

	def  __init__(self, instance_name):
		self.instance_name = instance_name

	def  __str__(self):
		return self.instance_name


	def update_country(self, new_country_id, old_country_id):
		query = "UPDATE country SET country_id = '" + new_country_id + "' WHERE country_id = '" + old_country_id + "'";
		return query

	def update_country_code(self, code, country_id):
		query = "UPDATE country_code SET code = '" + code + "' WHERE country_id = '" + country_id + "'";
		return query

	def country_code_by_a_new_key(self, new_country_id, old_country_id):
		query = "UPDATE country_code SET country_id = '" + new_country_id + "' WHERE country_id = '" + old_country_id + "'";
		return query

	def update_country_name(self, name, country_id):
		query = "UPDATE country_name SET name = '" + name + "' WHERE country_id = '" + country_id + "'";
		return query

	def country_name_by_a_new_key(self, new_country_id, old_country_id):
		query = "UPDATE country_name SET country_id = '" + new_country_id + "' WHERE country_id = '" + old_country_id + "'";
		return query

	def update_country_currency(self, currency, country_id):
		query = "UPDATE country_currency SET currency = '" + currency + "' WHERE country_id = '" + country_id + "'";
		return query

	def country_currency_by_a_new_key(self, new_country_id, old_country_id):
		query = "UPDATE country_currency SET country_id = '" + new_country_id + "' WHERE country_id = '" + old_country_id + "'";
		return query

	def update_country_flag(self, flag, country_id):
		query = "UPDATE country_flag SET flag = '" + flag + "' WHERE country_id = '" + country_id + "'";
		return query

	def country_flag_by_a_new_key(self, new_country_id, old_country_id):
		query = "UPDATE country_flag SET country_id = '" + new_country_id + "' WHERE country_id = '" + old_country_id + "'";
		return query

	def update_country_coat_of_arms(self, coat_of_arms, country_id):
		query = "UPDATE country_coat_of_arms SET coat_of_arms = '" + coat_of_arms + "' WHERE country_id = '" + country_id + "'";
		return query

	def country_coat_of_arms_by_a_new_key(self, new_country_id, old_country_id):
		query = "UPDATE country_coat_of_arms SET country_id = '" + new_country_id + "' WHERE country_id = '" + old_country_id + "'";
		return query

	def update_fiscal_year(self, new_fiscal_year_id, old_fiscal_year_id):
		query = "UPDATE fiscal_year SET fiscal_year_id = '" + new_fiscal_year_id + "' WHERE fiscal_year_id = '" + old_fiscal_year_id + "'";
		return query

	def update_fiscal_year_start_date(self, start_date, fiscal_year_id):
		query = "UPDATE fiscal_year_start_date SET start_date = '" + start_date + "' WHERE fiscal_year_id = '" + fiscal_year_id + "'";
		return query

	def fiscal_year_start_date_by_a_new_key(self, new_fiscal_year_id, old_fiscal_year_id):
		query = "UPDATE fiscal_year_start_date SET fiscal_year_id = '" + new_fiscal_year_id + "' WHERE fiscal_year_id = '" + old_fiscal_year_id + "'";
		return query

	def update_fiscal_year_end_date(self, end_date, fiscal_year_id):
		query = "UPDATE fiscal_year_end_date SET end_date = '" + end_date + "' WHERE fiscal_year_id = '" + fiscal_year_id + "'";
		return query

	def fiscal_year_end_date_by_a_new_key(self, new_fiscal_year_id, old_fiscal_year_id):
		query = "UPDATE fiscal_year_end_date SET fiscal_year_id = '" + new_fiscal_year_id + "' WHERE fiscal_year_id = '" + old_fiscal_year_id + "'";
		return query

	def update_configuration(self, new_configuration_id, old_configuration_id):
		query = "UPDATE configuration SET configuration_id = '" + new_configuration_id + "' WHERE configuration_id = '" + old_configuration_id + "'";
		return query

	def update_configuration_name(self, name, configuration_id):
		query = "UPDATE configuration_name SET name = '" + name + "' WHERE configuration_id = '" + configuration_id + "'";
		return query

	def configuration_name_by_a_new_key(self, new_configuration_id, old_configuration_id):
		query = "UPDATE configuration_name SET configuration_id = '" + new_configuration_id + "' WHERE configuration_id = '" + old_configuration_id + "'";
		return query

	def update_configuration_description(self, description, configuration_id):
		query = "UPDATE configuration_description SET description = '" + description + "' WHERE configuration_id = '" + configuration_id + "'";
		return query

	def configuration_description_by_a_new_key(self, new_configuration_id, old_configuration_id):
		query = "UPDATE configuration_description SET configuration_id = '" + new_configuration_id + "' WHERE configuration_id = '" + old_configuration_id + "'";
		return query

	def update_configuration_value(self, value, configuration_id):
		query = "UPDATE configuration_value SET value = '" + value + "' WHERE configuration_id = '" + configuration_id + "'";
		return query

	def configuration_value_by_a_new_key(self, new_configuration_id, old_configuration_id):
		query = "UPDATE configuration_value SET configuration_id = '" + new_configuration_id + "' WHERE configuration_id = '" + old_configuration_id + "'";
		return query

	def update_configuration_status(self, status, configuration_id):
		query = "UPDATE configuration_status SET status = '" + status + "' WHERE configuration_id = '" + configuration_id + "'";
		return query

	def configuration_status_by_a_new_key(self, new_configuration_id, old_configuration_id):
		query = "UPDATE configuration_status SET configuration_id = '" + new_configuration_id + "' WHERE configuration_id = '" + old_configuration_id + "'";
		return query

	def update_red_flag(self, new_red_flag_id, old_red_flag_id):
		query = "UPDATE red_flag SET red_flag_id = '" + new_red_flag_id + "' WHERE red_flag_id = '" + old_red_flag_id + "'";
		return query

	def update_red_flag_name(self, name, red_flag_id):
		query = "UPDATE red_flag_name SET name = '" + name + "' WHERE red_flag_id = '" + red_flag_id + "'";
		return query

	def red_flag_name_by_a_new_key(self, new_red_flag_id, old_red_flag_id):
		query = "UPDATE red_flag_name SET red_flag_id = '" + new_red_flag_id + "' WHERE red_flag_id = '" + old_red_flag_id + "'";
		return query

	def update_red_flag_description(self, description, red_flag_id):
		query = "UPDATE red_flag_description SET description = '" + description + "' WHERE red_flag_id = '" + red_flag_id + "'";
		return query

	def red_flag_description_by_a_new_key(self, new_red_flag_id, old_red_flag_id):
		query = "UPDATE red_flag_description SET red_flag_id = '" + new_red_flag_id + "' WHERE red_flag_id = '" + old_red_flag_id + "'";
		return query

	def update_red_flag_status(self, status, red_flag_id):
		query = "UPDATE red_flag_status SET status = '" + status + "' WHERE red_flag_id = '" + red_flag_id + "'";
		return query

	def red_flag_status_by_a_new_key(self, new_red_flag_id, old_red_flag_id):
		query = "UPDATE red_flag_status SET red_flag_id = '" + new_red_flag_id + "' WHERE red_flag_id = '" + old_red_flag_id + "'";
		return query

	def update_illicit_scheme(self, new_illicit_scheme_id, old_illicit_scheme_id):
		query = "UPDATE illicit_scheme SET illicit_scheme_id = '" + new_illicit_scheme_id + "' WHERE illicit_scheme_id = '" + old_illicit_scheme_id + "'";
		return query

	def update_illicit_scheme_name(self, name, illicit_scheme_id):
		query = "UPDATE illicit_scheme_name SET name = '" + name + "' WHERE illicit_scheme_id = '" + illicit_scheme_id + "'";
		return query

	def illicit_scheme_name_by_a_new_key(self, new_illicit_scheme_id, old_illicit_scheme_id):
		query = "UPDATE illicit_scheme_name SET illicit_scheme_id = '" + new_illicit_scheme_id + "' WHERE illicit_scheme_id = '" + old_illicit_scheme_id + "'";
		return query

	def update_illicit_scheme_description(self, description, illicit_scheme_id):
		query = "UPDATE illicit_scheme_description SET description = '" + description + "' WHERE illicit_scheme_id = '" + illicit_scheme_id + "'";
		return query

	def illicit_scheme_description_by_a_new_key(self, new_illicit_scheme_id, old_illicit_scheme_id):
		query = "UPDATE illicit_scheme_description SET illicit_scheme_id = '" + new_illicit_scheme_id + "' WHERE illicit_scheme_id = '" + old_illicit_scheme_id + "'";
		return query

	def update_procurement_stage(self, new_procurement_stage_id, old_procurement_stage_id):
		query = "UPDATE procurement_stage SET procurement_stage_id = '" + new_procurement_stage_id + "' WHERE procurement_stage_id = '" + old_procurement_stage_id + "'";
		return query

	def update_procurement_stage_name(self, name, procurement_stage_id):
		query = "UPDATE procurement_stage_name SET name = '" + name + "' WHERE procurement_stage_id = '" + procurement_stage_id + "'";
		return query

	def procurement_stage_name_by_a_new_key(self, new_procurement_stage_id, old_procurement_stage_id):
		query = "UPDATE procurement_stage_name SET procurement_stage_id = '" + new_procurement_stage_id + "' WHERE procurement_stage_id = '" + old_procurement_stage_id + "'";
		return query

	def update_procurement_stage_description(self, description, procurement_stage_id):
		query = "UPDATE procurement_stage_description SET description = '" + description + "' WHERE procurement_stage_id = '" + procurement_stage_id + "'";
		return query

	def procurement_stage_description_by_a_new_key(self, new_procurement_stage_id, old_procurement_stage_id):
		query = "UPDATE procurement_stage_description SET procurement_stage_id = '" + new_procurement_stage_id + "' WHERE procurement_stage_id = '" + old_procurement_stage_id + "'";
		return query

	def update_submission(self, new_submission_id, old_submission_id):
		query = "UPDATE submission SET submission_id = '" + new_submission_id + "' WHERE submission_id = '" + old_submission_id + "'";
		return query

	def update_submission_name(self, name, submission_id):
		query = "UPDATE submission_name SET name = '" + name + "' WHERE submission_id = '" + submission_id + "'";
		return query

	def submission_name_by_a_new_key(self, new_submission_id, old_submission_id):
		query = "UPDATE submission_name SET submission_id = '" + new_submission_id + "' WHERE submission_id = '" + old_submission_id + "'";
		return query

	def update_submission_description(self, description, submission_id):
		query = "UPDATE submission_description SET description = '" + description + "' WHERE submission_id = '" + submission_id + "'";
		return query

	def submission_description_by_a_new_key(self, new_submission_id, old_submission_id):
		query = "UPDATE submission_description SET submission_id = '" + new_submission_id + "' WHERE submission_id = '" + old_submission_id + "'";
		return query

	def update_submission_reception_date_and_time(self, reception_date_and_time, submission_id):
		query = "UPDATE submission_reception_date_and_time SET reception_date_and_time = '" + reception_date_and_time + "' WHERE submission_id = '" + submission_id + "'";
		return query

	def submission_reception_date_and_time_by_a_new_key(self, new_submission_id, old_submission_id):
		query = "UPDATE submission_reception_date_and_time SET submission_id = '" + new_submission_id + "' WHERE submission_id = '" + old_submission_id + "'";
		return query

	def update_submission_cut_off_date_and_time(self, cut_off_date_and_time, submission_id):
		query = "UPDATE submission_cut_off_date_and_time SET cut_off_date_and_time = '" + cut_off_date_and_time + "' WHERE submission_id = '" + submission_id + "'";
		return query

	def submission_cut_off_date_and_time_by_a_new_key(self, new_submission_id, old_submission_id):
		query = "UPDATE submission_cut_off_date_and_time SET submission_id = '" + new_submission_id + "' WHERE submission_id = '" + old_submission_id + "'";
		return query

	def update_procurement_type(self, new_procurement_type_id, old_procurement_type_id):
		query = "UPDATE procurement_type SET procurement_type_id = '" + new_procurement_type_id + "' WHERE procurement_type_id = '" + old_procurement_type_id + "'";
		return query

	def update_procurement_type_code(self, code, procurement_type_id):
		query = "UPDATE procurement_type_code SET code = '" + code + "' WHERE procurement_type_id = '" + procurement_type_id + "'";
		return query

	def procurement_type_code_by_a_new_key(self, new_procurement_type_id, old_procurement_type_id):
		query = "UPDATE procurement_type_code SET procurement_type_id = '" + new_procurement_type_id + "' WHERE procurement_type_id = '" + old_procurement_type_id + "'";
		return query

	def update_procurement_type_name(self, name, procurement_type_id):
		query = "UPDATE procurement_type_name SET name = '" + name + "' WHERE procurement_type_id = '" + procurement_type_id + "'";
		return query

	def procurement_type_name_by_a_new_key(self, new_procurement_type_id, old_procurement_type_id):
		query = "UPDATE procurement_type_name SET procurement_type_id = '" + new_procurement_type_id + "' WHERE procurement_type_id = '" + old_procurement_type_id + "'";
		return query

	def update_procurement_type_description(self, description, procurement_type_id):
		query = "UPDATE procurement_type_description SET description = '" + description + "' WHERE procurement_type_id = '" + procurement_type_id + "'";
		return query

	def procurement_type_description_by_a_new_key(self, new_procurement_type_id, old_procurement_type_id):
		query = "UPDATE procurement_type_description SET procurement_type_id = '" + new_procurement_type_id + "' WHERE procurement_type_id = '" + old_procurement_type_id + "'";
		return query

	def update_procurement_method(self, new_procurement_method_id, old_procurement_method_id):
		query = "UPDATE procurement_method SET procurement_method_id = '" + new_procurement_method_id + "' WHERE procurement_method_id = '" + old_procurement_method_id + "'";
		return query

	def update_procurement_method_code(self, code, procurement_method_id):
		query = "UPDATE procurement_method_code SET code = '" + code + "' WHERE procurement_method_id = '" + procurement_method_id + "'";
		return query

	def procurement_method_code_by_a_new_key(self, new_procurement_method_id, old_procurement_method_id):
		query = "UPDATE procurement_method_code SET procurement_method_id = '" + new_procurement_method_id + "' WHERE procurement_method_id = '" + old_procurement_method_id + "'";
		return query

	def update_procurement_method_name(self, name, procurement_method_id):
		query = "UPDATE procurement_method_name SET name = '" + name + "' WHERE procurement_method_id = '" + procurement_method_id + "'";
		return query

	def procurement_method_name_by_a_new_key(self, new_procurement_method_id, old_procurement_method_id):
		query = "UPDATE procurement_method_name SET procurement_method_id = '" + new_procurement_method_id + "' WHERE procurement_method_id = '" + old_procurement_method_id + "'";
		return query

	def update_procurement_method_description(self, description, procurement_method_id):
		query = "UPDATE procurement_method_description SET description = '" + description + "' WHERE procurement_method_id = '" + procurement_method_id + "'";
		return query

	def procurement_method_description_by_a_new_key(self, new_procurement_method_id, old_procurement_method_id):
		query = "UPDATE procurement_method_description SET procurement_method_id = '" + new_procurement_method_id + "' WHERE procurement_method_id = '" + old_procurement_method_id + "'";
		return query

	def update_bid(self, new_bid_id, old_bid_id):
		query = "UPDATE bid SET bid_id = '" + new_bid_id + "' WHERE bid_id = '" + old_bid_id + "'";
		return query

	def update_bid_submission_date(self, submission_date, bid_id):
		query = "UPDATE bid_submission_date SET submission_date = '" + submission_date + "' WHERE bid_id = '" + bid_id + "'";
		return query

	def bid_submission_date_by_a_new_key(self, new_bid_id, old_bid_id):
		query = "UPDATE bid_submission_date SET bid_id = '" + new_bid_id + "' WHERE bid_id = '" + old_bid_id + "'";
		return query

	def update_bid_amount(self, amount, bid_id):
		query = "UPDATE bid_amount SET amount = amount WHERE bid_id = '" + bid_id + "'";
		return query

	def bid_amount_by_a_new_key(self, new_bid_id, old_bid_id):
		query = "UPDATE bid_amount SET bid_id = '" + new_bid_id + "' WHERE bid_id = '" + old_bid_id + "'";
		return query

	def update_bid_extra_information(self, extra_information, bid_id):
		query = "UPDATE bid_extra_information SET extra_information = '" + extra_information + "' WHERE bid_id = '" + bid_id + "'";
		return query

	def bid_extra_information_by_a_new_key(self, new_bid_id, old_bid_id):
		query = "UPDATE bid_extra_information SET bid_id = '" + new_bid_id + "' WHERE bid_id = '" + old_bid_id + "'";
		return query

	def update_item(self, new_item_id, old_item_id):
		query = "UPDATE item SET item_id = '" + new_item_id + "' WHERE item_id = '" + old_item_id + "'";
		return query

	def update_item_code(self, code, item_id):
		query = "UPDATE item_code SET code = '" + code + "' WHERE item_id = '" + item_id + "'";
		return query

	def item_code_by_a_new_key(self, new_item_id, old_item_id):
		query = "UPDATE item_code SET item_id = '" + new_item_id + "' WHERE item_id = '" + old_item_id + "'";
		return query

	def update_item_name(self, name, item_id):
		query = "UPDATE item_name SET name = '" + name + "' WHERE item_id = '" + item_id + "'";
		return query

	def item_name_by_a_new_key(self, new_item_id, old_item_id):
		query = "UPDATE item_name SET item_id = '" + new_item_id + "' WHERE item_id = '" + old_item_id + "'";
		return query

	def update_item_unit_cost(self, unit_cost, item_id):
		query = "UPDATE item_unit_cost SET unit_cost = unit_cost WHERE item_id = '" + item_id + "'";
		return query

	def item_unit_cost_by_a_new_key(self, new_item_id, old_item_id):
		query = "UPDATE item_unit_cost SET item_id = '" + new_item_id + "' WHERE item_id = '" + old_item_id + "'";
		return query

	def update_item_description(self, description, item_id):
		query = "UPDATE item_description SET description = '" + description + "' WHERE item_id = '" + item_id + "'";
		return query

	def item_description_by_a_new_key(self, new_item_id, old_item_id):
		query = "UPDATE item_description SET item_id = '" + new_item_id + "' WHERE item_id = '" + old_item_id + "'";
		return query

	def update_procuring_entity(self, new_procuring_entity_id, old_procuring_entity_id):
		query = "UPDATE procuring_entity SET procuring_entity_id = '" + new_procuring_entity_id + "' WHERE procuring_entity_id = '" + old_procuring_entity_id + "'";
		return query

	def update_procuring_entity_name(self, name, procuring_entity_id):
		query = "UPDATE procuring_entity_name SET name = '" + name + "' WHERE procuring_entity_id = '" + procuring_entity_id + "'";
		return query

	def procuring_entity_name_by_a_new_key(self, new_procuring_entity_id, old_procuring_entity_id):
		query = "UPDATE procuring_entity_name SET procuring_entity_id = '" + new_procuring_entity_id + "' WHERE procuring_entity_id = '" + old_procuring_entity_id + "'";
		return query

	def update_procuring_entity_tax_identifier(self, tax_identifier, procuring_entity_id):
		query = "UPDATE procuring_entity_tax_identifier SET tax_identifier = '" + tax_identifier + "' WHERE procuring_entity_id = '" + procuring_entity_id + "'";
		return query

	def procuring_entity_tax_identifier_by_a_new_key(self, new_procuring_entity_id, old_procuring_entity_id):
		query = "UPDATE procuring_entity_tax_identifier SET procuring_entity_id = '" + new_procuring_entity_id + "' WHERE procuring_entity_id = '" + old_procuring_entity_id + "'";
		return query

	def update_procuring_entity_tax_identifier_value(self, tax_identifier_value, procuring_entity_id):
		query = "UPDATE procuring_entity_tax_identifier_value SET tax_identifier_value = '" + tax_identifier_value + "' WHERE procuring_entity_id = '" + procuring_entity_id + "'";
		return query

	def procuring_entity_tax_identifier_value_by_a_new_key(self, new_procuring_entity_id, old_procuring_entity_id):
		query = "UPDATE procuring_entity_tax_identifier_value SET procuring_entity_id = '" + new_procuring_entity_id + "' WHERE procuring_entity_id = '" + old_procuring_entity_id + "'";
		return query

	def update_procuring_entity_registration_number(self, registration_number, procuring_entity_id):
		query = "UPDATE procuring_entity_registration_number SET registration_number = '" + registration_number + "' WHERE procuring_entity_id = '" + procuring_entity_id + "'";
		return query

	def procuring_entity_registration_number_by_a_new_key(self, new_procuring_entity_id, old_procuring_entity_id):
		query = "UPDATE procuring_entity_registration_number SET procuring_entity_id = '" + new_procuring_entity_id + "' WHERE procuring_entity_id = '" + old_procuring_entity_id + "'";
		return query

	def update_procuring_entity_registration_date(self, registration_date, procuring_entity_id):
		query = "UPDATE procuring_entity_registration_date SET registration_date = '" + registration_date + "' WHERE procuring_entity_id = '" + procuring_entity_id + "'";
		return query

	def procuring_entity_registration_date_by_a_new_key(self, new_procuring_entity_id, old_procuring_entity_id):
		query = "UPDATE procuring_entity_registration_date SET procuring_entity_id = '" + new_procuring_entity_id + "' WHERE procuring_entity_id = '" + old_procuring_entity_id + "'";
		return query

	def update_procuring_entity_status(self, status, procuring_entity_id):
		query = "UPDATE procuring_entity_status SET status = '" + status + "' WHERE procuring_entity_id = '" + procuring_entity_id + "'";
		return query

	def procuring_entity_status_by_a_new_key(self, new_procuring_entity_id, old_procuring_entity_id):
		query = "UPDATE procuring_entity_status SET procuring_entity_id = '" + new_procuring_entity_id + "' WHERE procuring_entity_id = '" + old_procuring_entity_id + "'";
		return query

	def update_supplying_entity(self, new_supplying_entity_id, old_supplying_entity_id):
		query = "UPDATE supplying_entity SET supplying_entity_id = '" + new_supplying_entity_id + "' WHERE supplying_entity_id = '" + old_supplying_entity_id + "'";
		return query

	def update_supplying_entity_name(self, name, supplying_entity_id):
		query = "UPDATE supplying_entity_name SET name = '" + name + "' WHERE supplying_entity_id = '" + supplying_entity_id + "'";
		return query

	def supplying_entity_name_by_a_new_key(self, new_supplying_entity_id, old_supplying_entity_id):
		query = "UPDATE supplying_entity_name SET supplying_entity_id = '" + new_supplying_entity_id + "' WHERE supplying_entity_id = '" + old_supplying_entity_id + "'";
		return query

	def update_supplying_entity_tax_identifier(self, tax_identifier, supplying_entity_id):
		query = "UPDATE supplying_entity_tax_identifier SET tax_identifier = '" + tax_identifier + "' WHERE supplying_entity_id = '" + supplying_entity_id + "'";
		return query

	def supplying_entity_tax_identifier_by_a_new_key(self, new_supplying_entity_id, old_supplying_entity_id):
		query = "UPDATE supplying_entity_tax_identifier SET supplying_entity_id = '" + new_supplying_entity_id + "' WHERE supplying_entity_id = '" + old_supplying_entity_id + "'";
		return query

	def update_supplying_entity_tax_identifier_value(self, tax_identifier_value, supplying_entity_id):
		query = "UPDATE supplying_entity_tax_identifier_value SET tax_identifier_value = '" + tax_identifier_value + "' WHERE supplying_entity_id = '" + supplying_entity_id + "'";
		return query

	def supplying_entity_tax_identifier_value_by_a_new_key(self, new_supplying_entity_id, old_supplying_entity_id):
		query = "UPDATE supplying_entity_tax_identifier_value SET supplying_entity_id = '" + new_supplying_entity_id + "' WHERE supplying_entity_id = '" + old_supplying_entity_id + "'";
		return query

	def update_supplying_entity_registration_number(self, registration_number, supplying_entity_id):
		query = "UPDATE supplying_entity_registration_number SET registration_number = '" + registration_number + "' WHERE supplying_entity_id = '" + supplying_entity_id + "'";
		return query

	def supplying_entity_registration_number_by_a_new_key(self, new_supplying_entity_id, old_supplying_entity_id):
		query = "UPDATE supplying_entity_registration_number SET supplying_entity_id = '" + new_supplying_entity_id + "' WHERE supplying_entity_id = '" + old_supplying_entity_id + "'";
		return query

	def update_supplying_entity_registration_date(self, registration_date, supplying_entity_id):
		query = "UPDATE supplying_entity_registration_date SET registration_date = '" + registration_date + "' WHERE supplying_entity_id = '" + supplying_entity_id + "'";
		return query

	def supplying_entity_registration_date_by_a_new_key(self, new_supplying_entity_id, old_supplying_entity_id):
		query = "UPDATE supplying_entity_registration_date SET supplying_entity_id = '" + new_supplying_entity_id + "' WHERE supplying_entity_id = '" + old_supplying_entity_id + "'";
		return query

	def update_supplying_entity_status(self, status, supplying_entity_id):
		query = "UPDATE supplying_entity_status SET status = '" + status + "' WHERE supplying_entity_id = '" + supplying_entity_id + "'";
		return query

	def supplying_entity_status_by_a_new_key(self, new_supplying_entity_id, old_supplying_entity_id):
		query = "UPDATE supplying_entity_status SET supplying_entity_id = '" + new_supplying_entity_id + "' WHERE supplying_entity_id = '" + old_supplying_entity_id + "'";
		return query

	def update_address(self, new_address_id, old_address_id):
		query = "UPDATE address SET address_id = '" + new_address_id + "' WHERE address_id = '" + old_address_id + "'";
		return query

	def update_address_country(self, country, address_id):
		query = "UPDATE address_country SET country = '" + country + "' WHERE address_id = '" + address_id + "'";
		return query

	def address_country_by_a_new_key(self, new_address_id, old_address_id):
		query = "UPDATE address_country SET address_id = '" + new_address_id + "' WHERE address_id = '" + old_address_id + "'";
		return query

	def update_address_address_line_1(self, address_line_1, address_id):
		query = "UPDATE address_address_line_1 SET address_line_1 = '" + address_line_1 + "' WHERE address_id = '" + address_id + "'";
		return query

	def address_address_line_1_by_a_new_key(self, new_address_id, old_address_id):
		query = "UPDATE address_address_line_1 SET address_id = '" + new_address_id + "' WHERE address_id = '" + old_address_id + "'";
		return query

	def update_address_address_line_2(self, address_line_2, address_id):
		query = "UPDATE address_address_line_2 SET address_line_2 = '" + address_line_2 + "' WHERE address_id = '" + address_id + "'";
		return query

	def address_address_line_2_by_a_new_key(self, new_address_id, old_address_id):
		query = "UPDATE address_address_line_2 SET address_id = '" + new_address_id + "' WHERE address_id = '" + old_address_id + "'";
		return query

	def update_address_address_line_3(self, address_line_3, address_id):
		query = "UPDATE address_address_line_3 SET address_line_3 = '" + address_line_3 + "' WHERE address_id = '" + address_id + "'";
		return query

	def address_address_line_3_by_a_new_key(self, new_address_id, old_address_id):
		query = "UPDATE address_address_line_3 SET address_id = '" + new_address_id + "' WHERE address_id = '" + old_address_id + "'";
		return query

	def update_address_address_line_4(self, address_line_4, address_id):
		query = "UPDATE address_address_line_4 SET address_line_4 = '" + address_line_4 + "' WHERE address_id = '" + address_id + "'";
		return query

	def address_address_line_4_by_a_new_key(self, new_address_id, old_address_id):
		query = "UPDATE address_address_line_4 SET address_id = '" + new_address_id + "' WHERE address_id = '" + old_address_id + "'";
		return query

	def update_address_address_line_5(self, address_line_5, address_id):
		query = "UPDATE address_address_line_5 SET address_line_5 = '" + address_line_5 + "' WHERE address_id = '" + address_id + "'";
		return query

	def address_address_line_5_by_a_new_key(self, new_address_id, old_address_id):
		query = "UPDATE address_address_line_5 SET address_id = '" + new_address_id + "' WHERE address_id = '" + old_address_id + "'";
		return query

	def update_address_address_line_6(self, address_line_6, address_id):
		query = "UPDATE address_address_line_6 SET address_line_6 = '" + address_line_6 + "' WHERE address_id = '" + address_id + "'";
		return query

	def address_address_line_6_by_a_new_key(self, new_address_id, old_address_id):
		query = "UPDATE address_address_line_6 SET address_id = '" + new_address_id + "' WHERE address_id = '" + old_address_id + "'";
		return query

	def update_address_address_line_7(self, address_line_7, address_id):
		query = "UPDATE address_address_line_7 SET address_line_7 = '" + address_line_7 + "' WHERE address_id = '" + address_id + "'";
		return query

	def address_address_line_7_by_a_new_key(self, new_address_id, old_address_id):
		query = "UPDATE address_address_line_7 SET address_id = '" + new_address_id + "' WHERE address_id = '" + old_address_id + "'";
		return query

	def update_address_address_line_8(self, address_line_8, address_id):
		query = "UPDATE address_address_line_8 SET address_line_8 = '" + address_line_8 + "' WHERE address_id = '" + address_id + "'";
		return query

	def address_address_line_8_by_a_new_key(self, new_address_id, old_address_id):
		query = "UPDATE address_address_line_8 SET address_id = '" + new_address_id + "' WHERE address_id = '" + old_address_id + "'";
		return query

	def update_address_address_line_9(self, address_line_9, address_id):
		query = "UPDATE address_address_line_9 SET address_line_9 = '" + address_line_9 + "' WHERE address_id = '" + address_id + "'";
		return query

	def address_address_line_9_by_a_new_key(self, new_address_id, old_address_id):
		query = "UPDATE address_address_line_9 SET address_id = '" + new_address_id + "' WHERE address_id = '" + old_address_id + "'";
		return query

	def update_address_x_coord(self, x_coord, address_id):
		query = "UPDATE address_x_coord SET x_coord = x_coord WHERE address_id = '" + address_id + "'";
		return query

	def address_x_coord_by_a_new_key(self, new_address_id, old_address_id):
		query = "UPDATE address_x_coord SET address_id = '" + new_address_id + "' WHERE address_id = '" + old_address_id + "'";
		return query

	def update_address_y_coord(self, y_coord, address_id):
		query = "UPDATE address_y_coord SET y_coord = y_coord WHERE address_id = '" + address_id + "'";
		return query

	def address_y_coord_by_a_new_key(self, new_address_id, old_address_id):
		query = "UPDATE address_y_coord SET address_id = '" + new_address_id + "' WHERE address_id = '" + old_address_id + "'";
		return query

	def update_address_status(self, status, address_id):
		query = "UPDATE address_status SET status = '" + status + "' WHERE address_id = '" + address_id + "'";
		return query

	def address_status_by_a_new_key(self, new_address_id, old_address_id):
		query = "UPDATE address_status SET address_id = '" + new_address_id + "' WHERE address_id = '" + old_address_id + "'";
		return query

	def update_address_description(self, description, address_id):
		query = "UPDATE address_description SET description = '" + description + "' WHERE address_id = '" + address_id + "'";
		return query

	def address_description_by_a_new_key(self, new_address_id, old_address_id):
		query = "UPDATE address_description SET address_id = '" + new_address_id + "' WHERE address_id = '" + old_address_id + "'";
		return query

	def update_address_short_form(self, short_form, address_id):
		query = "UPDATE address_short_form SET short_form = '" + short_form + "' WHERE address_id = '" + address_id + "'";
		return query

	def address_short_form_by_a_new_key(self, new_address_id, old_address_id):
		query = "UPDATE address_short_form SET address_id = '" + new_address_id + "' WHERE address_id = '" + old_address_id + "'";
		return query

	def update_tender(self, new_tender_id, old_tender_id):
		query = "UPDATE tender SET tender_id = '" + new_tender_id + "' WHERE tender_id = '" + old_tender_id + "'";
		return query

	def update_tender_title(self, title, tender_id):
		query = "UPDATE tender_title SET title = '" + title + "' WHERE tender_id = '" + tender_id + "'";
		return query

	def tender_title_by_a_new_key(self, new_tender_id, old_tender_id):
		query = "UPDATE tender_title SET tender_id = '" + new_tender_id + "' WHERE tender_id = '" + old_tender_id + "'";
		return query

	def update_tender_description(self, description, tender_id):
		query = "UPDATE tender_description SET description = '" + description + "' WHERE tender_id = '" + tender_id + "'";
		return query

	def tender_description_by_a_new_key(self, new_tender_id, old_tender_id):
		query = "UPDATE tender_description SET tender_id = '" + new_tender_id + "' WHERE tender_id = '" + old_tender_id + "'";
		return query

	def update_tender_budget(self, budget, tender_id):
		query = "UPDATE tender_budget SET budget = budget WHERE tender_id = '" + tender_id + "'";
		return query

	def tender_budget_by_a_new_key(self, new_tender_id, old_tender_id):
		query = "UPDATE tender_budget SET tender_id = '" + new_tender_id + "' WHERE tender_id = '" + old_tender_id + "'";
		return query

	def update_tender_status(self, status, tender_id):
		query = "UPDATE tender_status SET status = '" + status + "' WHERE tender_id = '" + tender_id + "'";
		return query

	def tender_status_by_a_new_key(self, new_tender_id, old_tender_id):
		query = "UPDATE tender_status SET tender_id = '" + new_tender_id + "' WHERE tender_id = '" + old_tender_id + "'";
		return query

	def update_tender_evaluate_mechanism(self, evaluate_mechanism, tender_id):
		query = "UPDATE tender_evaluate_mechanism SET evaluate_mechanism = '" + evaluate_mechanism + "' WHERE tender_id = '" + tender_id + "'";
		return query

	def tender_evaluate_mechanism_by_a_new_key(self, new_tender_id, old_tender_id):
		query = "UPDATE tender_evaluate_mechanism SET tender_id = '" + new_tender_id + "' WHERE tender_id = '" + old_tender_id + "'";
		return query

	def update_tender_publication_date_and_time(self, publication_date_and_time, tender_id):
		query = "UPDATE tender_publication_date_and_time SET publication_date_and_time = '" + publication_date_and_time + "' WHERE tender_id = '" + tender_id + "'";
		return query

	def tender_publication_date_and_time_by_a_new_key(self, new_tender_id, old_tender_id):
		query = "UPDATE tender_publication_date_and_time SET tender_id = '" + new_tender_id + "' WHERE tender_id = '" + old_tender_id + "'";
		return query

	def update_tender_submission_cut_off_date_and_time(self, submission_cut_off_date_and_time, tender_id):
		query = "UPDATE tender_submission_cut_off_date_and_time SET submission_cut_off_date_and_time = '" + submission_cut_off_date_and_time + "' WHERE tender_id = '" + tender_id + "'";
		return query

	def tender_submission_cut_off_date_and_time_by_a_new_key(self, new_tender_id, old_tender_id):
		query = "UPDATE tender_submission_cut_off_date_and_time SET tender_id = '" + new_tender_id + "' WHERE tender_id = '" + old_tender_id + "'";
		return query

	def update_tender_award_notice_date(self, award_notice_date, tender_id):
		query = "UPDATE tender_award_notice_date SET award_notice_date = '" + award_notice_date + "' WHERE tender_id = '" + tender_id + "'";
		return query

	def tender_award_notice_date_by_a_new_key(self, new_tender_id, old_tender_id):
		query = "UPDATE tender_award_notice_date SET tender_id = '" + new_tender_id + "' WHERE tender_id = '" + old_tender_id + "'";
		return query

	def update_tender_contract_notice_date(self, contract_notice_date, tender_id):
		query = "UPDATE tender_contract_notice_date SET contract_notice_date = '" + contract_notice_date + "' WHERE tender_id = '" + tender_id + "'";
		return query

	def tender_contract_notice_date_by_a_new_key(self, new_tender_id, old_tender_id):
		query = "UPDATE tender_contract_notice_date SET tender_id = '" + new_tender_id + "' WHERE tender_id = '" + old_tender_id + "'";
		return query

	def update_attachment(self, new_attachment_id, old_attachment_id):
		query = "UPDATE attachment SET attachment_id = '" + new_attachment_id + "' WHERE attachment_id = '" + old_attachment_id + "'";
		return query

	def update_attachment_type(self, type, attachment_id):
		query = "UPDATE attachment_type SET type = '" + type + "' WHERE attachment_id = '" + attachment_id + "'";
		return query

	def attachment_type_by_a_new_key(self, new_attachment_id, old_attachment_id):
		query = "UPDATE attachment_type SET attachment_id = '" + new_attachment_id + "' WHERE attachment_id = '" + old_attachment_id + "'";
		return query

	def update_attachment_name(self, name, attachment_id):
		query = "UPDATE attachment_name SET name = '" + name + "' WHERE attachment_id = '" + attachment_id + "'";
		return query

	def attachment_name_by_a_new_key(self, new_attachment_id, old_attachment_id):
		query = "UPDATE attachment_name SET attachment_id = '" + new_attachment_id + "' WHERE attachment_id = '" + old_attachment_id + "'";
		return query

	def update_attachment_description(self, description, attachment_id):
		query = "UPDATE attachment_description SET description = '" + description + "' WHERE attachment_id = '" + attachment_id + "'";
		return query

	def attachment_description_by_a_new_key(self, new_attachment_id, old_attachment_id):
		query = "UPDATE attachment_description SET attachment_id = '" + new_attachment_id + "' WHERE attachment_id = '" + old_attachment_id + "'";
		return query

	def update_attachment_link(self, link, attachment_id):
		query = "UPDATE attachment_link SET link = '" + link + "' WHERE attachment_id = '" + attachment_id + "'";
		return query

	def attachment_link_by_a_new_key(self, new_attachment_id, old_attachment_id):
		query = "UPDATE attachment_link SET attachment_id = '" + new_attachment_id + "' WHERE attachment_id = '" + old_attachment_id + "'";
		return query

	def update_award(self, new_award_id, old_award_id):
		query = "UPDATE award SET award_id = '" + new_award_id + "' WHERE award_id = '" + old_award_id + "'";
		return query

	def update_award_is_accepted(self, is_accepted, award_id):
		query = "UPDATE award_is_accepted SET is_accepted = is_accepted WHERE award_id = '" + award_id + "'";
		return query

	def award_is_accepted_by_a_new_key(self, new_award_id, old_award_id):
		query = "UPDATE award_is_accepted SET award_id = '" + new_award_id + "' WHERE award_id = '" + old_award_id + "'";
		return query

	def update_award_date_replied(self, date_replied, award_id):
		query = "UPDATE award_date_replied SET date_replied = '" + date_replied + "' WHERE award_id = '" + award_id + "'";
		return query

	def award_date_replied_by_a_new_key(self, new_award_id, old_award_id):
		query = "UPDATE award_date_replied SET award_id = '" + new_award_id + "' WHERE award_id = '" + old_award_id + "'";
		return query

	def update_award_reply_reason(self, reply_reason, award_id):
		query = "UPDATE award_reply_reason SET reply_reason = '" + reply_reason + "' WHERE award_id = '" + award_id + "'";
		return query

	def award_reply_reason_by_a_new_key(self, new_award_id, old_award_id):
		query = "UPDATE award_reply_reason SET award_id = '" + new_award_id + "' WHERE award_id = '" + old_award_id + "'";
		return query

	def update_award_award_amount(self, award_amount, award_id):
		query = "UPDATE award_award_amount SET award_amount = award_amount WHERE award_id = '" + award_id + "'";
		return query

	def award_award_amount_by_a_new_key(self, new_award_id, old_award_id):
		query = "UPDATE award_award_amount SET award_id = '" + new_award_id + "' WHERE award_id = '" + old_award_id + "'";
		return query

	def update_contact(self, new_contact_id, old_contact_id):
		query = "UPDATE contact SET contact_id = '" + new_contact_id + "' WHERE contact_id = '" + old_contact_id + "'";
		return query

	def update_contact_name(self, name, contact_id):
		query = "UPDATE contact_name SET name = '" + name + "' WHERE contact_id = '" + contact_id + "'";
		return query

	def contact_name_by_a_new_key(self, new_contact_id, old_contact_id):
		query = "UPDATE contact_name SET contact_id = '" + new_contact_id + "' WHERE contact_id = '" + old_contact_id + "'";
		return query

	def update_contact_value(self, value, contact_id):
		query = "UPDATE contact_value SET value = '" + value + "' WHERE contact_id = '" + contact_id + "'";
		return query

	def contact_value_by_a_new_key(self, new_contact_id, old_contact_id):
		query = "UPDATE contact_value SET contact_id = '" + new_contact_id + "' WHERE contact_id = '" + old_contact_id + "'";
		return query

	def update_contact_status(self, status, contact_id):
		query = "UPDATE contact_status SET status = '" + status + "' WHERE contact_id = '" + contact_id + "'";
		return query

	def contact_status_by_a_new_key(self, new_contact_id, old_contact_id):
		query = "UPDATE contact_status SET contact_id = '" + new_contact_id + "' WHERE contact_id = '" + old_contact_id + "'";
		return query

	def update_contract(self, new_contract_id, old_contract_id):
		query = "UPDATE contract SET contract_id = '" + new_contract_id + "' WHERE contract_id = '" + old_contract_id + "'";
		return query

	def update_contract_title(self, title, contract_id):
		query = "UPDATE contract_title SET title = '" + title + "' WHERE contract_id = '" + contract_id + "'";
		return query

	def contract_title_by_a_new_key(self, new_contract_id, old_contract_id):
		query = "UPDATE contract_title SET contract_id = '" + new_contract_id + "' WHERE contract_id = '" + old_contract_id + "'";
		return query

	def update_contract_amount(self, amount, contract_id):
		query = "UPDATE contract_amount SET amount = amount WHERE contract_id = '" + contract_id + "'";
		return query

	def contract_amount_by_a_new_key(self, new_contract_id, old_contract_id):
		query = "UPDATE contract_amount SET contract_id = '" + new_contract_id + "' WHERE contract_id = '" + old_contract_id + "'";
		return query

	def update_contract_status(self, status, contract_id):
		query = "UPDATE contract_status SET status = '" + status + "' WHERE contract_id = '" + contract_id + "'";
		return query

	def contract_status_by_a_new_key(self, new_contract_id, old_contract_id):
		query = "UPDATE contract_status SET contract_id = '" + new_contract_id + "' WHERE contract_id = '" + old_contract_id + "'";
		return query

	def update_contract_description(self, description, contract_id):
		query = "UPDATE contract_description SET description = '" + description + "' WHERE contract_id = '" + contract_id + "'";
		return query

	def contract_description_by_a_new_key(self, new_contract_id, old_contract_id):
		query = "UPDATE contract_description SET contract_id = '" + new_contract_id + "' WHERE contract_id = '" + old_contract_id + "'";
		return query

	def update_fee(self, new_fee_id, old_fee_id):
		query = "UPDATE fee SET fee_id = '" + new_fee_id + "' WHERE fee_id = '" + old_fee_id + "'";
		return query

	def update_fee_name(self, name, fee_id):
		query = "UPDATE fee_name SET name = '" + name + "' WHERE fee_id = '" + fee_id + "'";
		return query

	def fee_name_by_a_new_key(self, new_fee_id, old_fee_id):
		query = "UPDATE fee_name SET fee_id = '" + new_fee_id + "' WHERE fee_id = '" + old_fee_id + "'";
		return query

	def update_fee_amount(self, amount, fee_id):
		query = "UPDATE fee_amount SET amount = amount WHERE fee_id = '" + fee_id + "'";
		return query

	def fee_amount_by_a_new_key(self, new_fee_id, old_fee_id):
		query = "UPDATE fee_amount SET fee_id = '" + new_fee_id + "' WHERE fee_id = '" + old_fee_id + "'";
		return query

	def update_fee_type(self, type, fee_id):
		query = "UPDATE fee_type SET type = '" + type + "' WHERE fee_id = '" + fee_id + "'";
		return query

	def fee_type_by_a_new_key(self, new_fee_id, old_fee_id):
		query = "UPDATE fee_type SET fee_id = '" + new_fee_id + "' WHERE fee_id = '" + old_fee_id + "'";
		return query

	def update_payment(self, new_payment_id, old_payment_id):
		query = "UPDATE payment SET payment_id = '" + new_payment_id + "' WHERE payment_id = '" + old_payment_id + "'";
		return query

	def update_payment_transaction_id(self, transaction_id, payment_id):
		query = "UPDATE payment_transaction_id SET transaction_id = '" + transaction_id + "' WHERE payment_id = '" + payment_id + "'";
		return query

	def payment_transaction_id_by_a_new_key(self, new_payment_id, old_payment_id):
		query = "UPDATE payment_transaction_id SET payment_id = '" + new_payment_id + "' WHERE payment_id = '" + old_payment_id + "'";
		return query

	def update_payment_date_received(self, date_received, payment_id):
		query = "UPDATE payment_date_received SET date_received = '" + date_received + "' WHERE payment_id = '" + payment_id + "'";
		return query

	def payment_date_received_by_a_new_key(self, new_payment_id, old_payment_id):
		query = "UPDATE payment_date_received SET payment_id = '" + new_payment_id + "' WHERE payment_id = '" + old_payment_id + "'";
		return query

	def update_payment_amount(self, amount, payment_id):
		query = "UPDATE payment_amount SET amount = amount WHERE payment_id = '" + payment_id + "'";
		return query

	def payment_amount_by_a_new_key(self, new_payment_id, old_payment_id):
		query = "UPDATE payment_amount SET payment_id = '" + new_payment_id + "' WHERE payment_id = '" + old_payment_id + "'";
		return query

	def update_payment_currency(self, currency, payment_id):
		query = "UPDATE payment_currency SET currency = '" + currency + "' WHERE payment_id = '" + payment_id + "'";
		return query

	def payment_currency_by_a_new_key(self, new_payment_id, old_payment_id):
		query = "UPDATE payment_currency SET payment_id = '" + new_payment_id + "' WHERE payment_id = '" + old_payment_id + "'";
		return query

	def update_payment_status(self, status, payment_id):
		query = "UPDATE payment_status SET status = '" + status + "' WHERE payment_id = '" + payment_id + "'";
		return query

	def payment_status_by_a_new_key(self, new_payment_id, old_payment_id):
		query = "UPDATE payment_status SET payment_id = '" + new_payment_id + "' WHERE payment_id = '" + old_payment_id + "'";
		return query

	def update_payment_extra_information(self, extra_information, payment_id):
		query = "UPDATE payment_extra_information SET extra_information = '" + extra_information + "' WHERE payment_id = '" + payment_id + "'";
		return query

	def payment_extra_information_by_a_new_key(self, new_payment_id, old_payment_id):
		query = "UPDATE payment_extra_information SET payment_id = '" + new_payment_id + "' WHERE payment_id = '" + old_payment_id + "'";
		return query

	def update_plan(self, new_plan_id, old_plan_id):
		query = "UPDATE plan SET plan_id = '" + new_plan_id + "' WHERE plan_id = '" + old_plan_id + "'";
		return query

	def update_plan_budget(self, budget, plan_id):
		query = "UPDATE plan_budget SET budget = budget WHERE plan_id = '" + plan_id + "'";
		return query

	def plan_budget_by_a_new_key(self, new_plan_id, old_plan_id):
		query = "UPDATE plan_budget SET plan_id = '" + new_plan_id + "' WHERE plan_id = '" + old_plan_id + "'";
		return query

	def update_plan_submission_date_and_time(self, submission_date_and_time, plan_id):
		query = "UPDATE plan_submission_date_and_time SET submission_date_and_time = '" + submission_date_and_time + "' WHERE plan_id = '" + plan_id + "'";
		return query

	def plan_submission_date_and_time_by_a_new_key(self, new_plan_id, old_plan_id):
		query = "UPDATE plan_submission_date_and_time SET plan_id = '" + new_plan_id + "' WHERE plan_id = '" + old_plan_id + "'";
		return query

	def update_plan_description(self, description, plan_id):
		query = "UPDATE plan_description SET description = '" + description + "' WHERE plan_id = '" + plan_id + "'";
		return query

	def plan_description_by_a_new_key(self, new_plan_id, old_plan_id):
		query = "UPDATE plan_description SET plan_id = '" + new_plan_id + "' WHERE plan_id = '" + old_plan_id + "'";
		return query

	def update_alert(self, new_alert_id, old_alert_id):
		query = "UPDATE alert SET alert_id = '" + new_alert_id + "' WHERE alert_id = '" + old_alert_id + "'";
		return query

	def update_alert_subject(self, subject, alert_id):
		query = "UPDATE alert_subject SET subject = '" + subject + "' WHERE alert_id = '" + alert_id + "'";
		return query

	def alert_subject_by_a_new_key(self, new_alert_id, old_alert_id):
		query = "UPDATE alert_subject SET alert_id = '" + new_alert_id + "' WHERE alert_id = '" + old_alert_id + "'";
		return query

	def update_alert_description(self, description, alert_id):
		query = "UPDATE alert_description SET description = '" + description + "' WHERE alert_id = '" + alert_id + "'";
		return query

	def alert_description_by_a_new_key(self, new_alert_id, old_alert_id):
		query = "UPDATE alert_description SET alert_id = '" + new_alert_id + "' WHERE alert_id = '" + old_alert_id + "'";
		return query

	def update_alert_authority(self, new_alert_authority_id, old_alert_authority_id):
		query = "UPDATE alert_authority SET alert_authority_id = '" + new_alert_authority_id + "' WHERE alert_authority_id = '" + old_alert_authority_id + "'";
		return query

	def update_alert_authority_name(self, name, alert_authority_id):
		query = "UPDATE alert_authority_name SET name = '" + name + "' WHERE alert_authority_id = '" + alert_authority_id + "'";
		return query

	def alert_authority_name_by_a_new_key(self, new_alert_authority_id, old_alert_authority_id):
		query = "UPDATE alert_authority_name SET alert_authority_id = '" + new_alert_authority_id + "' WHERE alert_authority_id = '" + old_alert_authority_id + "'";
		return query

	def update_alert_authority_description(self, description, alert_authority_id):
		query = "UPDATE alert_authority_description SET description = '" + description + "' WHERE alert_authority_id = '" + alert_authority_id + "'";
		return query

	def alert_authority_description_by_a_new_key(self, new_alert_authority_id, old_alert_authority_id):
		query = "UPDATE alert_authority_description SET alert_authority_id = '" + new_alert_authority_id + "' WHERE alert_authority_id = '" + old_alert_authority_id + "'";
		return query

	def update_alert_level(self, new_alert_level_id, old_alert_level_id):
		query = "UPDATE alert_level SET alert_level_id = '" + new_alert_level_id + "' WHERE alert_level_id = '" + old_alert_level_id + "'";
		return query

	def update_alert_level_name(self, name, alert_level_id):
		query = "UPDATE alert_level_name SET name = '" + name + "' WHERE alert_level_id = '" + alert_level_id + "'";
		return query

	def alert_level_name_by_a_new_key(self, new_alert_level_id, old_alert_level_id):
		query = "UPDATE alert_level_name SET alert_level_id = '" + new_alert_level_id + "' WHERE alert_level_id = '" + old_alert_level_id + "'";
		return query

	def update_alert_level_description(self, description, alert_level_id):
		query = "UPDATE alert_level_description SET description = '" + description + "' WHERE alert_level_id = '" + alert_level_id + "'";
		return query

	def alert_level_description_by_a_new_key(self, new_alert_level_id, old_alert_level_id):
		query = "UPDATE alert_level_description SET alert_level_id = '" + new_alert_level_id + "' WHERE alert_level_id = '" + old_alert_level_id + "'";
		return query

	def update_user_account(self, new_user_account_id, old_user_account_id):
		query = "UPDATE user_account SET user_account_id = '" + new_user_account_id + "' WHERE user_account_id = '" + old_user_account_id + "'";
		return query

	def update_user_account_national_id_number(self, national_id_number, user_account_id):
		query = "UPDATE user_account_national_id_number SET national_id_number = '" + national_id_number + "' WHERE user_account_id = '" + user_account_id + "'";
		return query

	def user_account_national_id_number_by_a_new_key(self, new_user_account_id, old_user_account_id):
		query = "UPDATE user_account_national_id_number SET user_account_id = '" + new_user_account_id + "' WHERE user_account_id = '" + old_user_account_id + "'";
		return query

	def update_user_account_category(self, category, user_account_id):
		query = "UPDATE user_account_category SET category = '" + category + "' WHERE user_account_id = '" + user_account_id + "'";
		return query

	def user_account_category_by_a_new_key(self, new_user_account_id, old_user_account_id):
		query = "UPDATE user_account_category SET user_account_id = '" + new_user_account_id + "' WHERE user_account_id = '" + old_user_account_id + "'";
		return query

	def update_user_account_first_name(self, first_name, user_account_id):
		query = "UPDATE user_account_first_name SET first_name = '" + first_name + "' WHERE user_account_id = '" + user_account_id + "'";
		return query

	def user_account_first_name_by_a_new_key(self, new_user_account_id, old_user_account_id):
		query = "UPDATE user_account_first_name SET user_account_id = '" + new_user_account_id + "' WHERE user_account_id = '" + old_user_account_id + "'";
		return query

	def update_user_account_last_name(self, last_name, user_account_id):
		query = "UPDATE user_account_last_name SET last_name = '" + last_name + "' WHERE user_account_id = '" + user_account_id + "'";
		return query

	def user_account_last_name_by_a_new_key(self, new_user_account_id, old_user_account_id):
		query = "UPDATE user_account_last_name SET user_account_id = '" + new_user_account_id + "' WHERE user_account_id = '" + old_user_account_id + "'";
		return query

	def update_user_account_other_names(self, other_names, user_account_id):
		query = "UPDATE user_account_other_names SET other_names = '" + other_names + "' WHERE user_account_id = '" + user_account_id + "'";
		return query

	def user_account_other_names_by_a_new_key(self, new_user_account_id, old_user_account_id):
		query = "UPDATE user_account_other_names SET user_account_id = '" + new_user_account_id + "' WHERE user_account_id = '" + old_user_account_id + "'";
		return query

	def update_user_account_date_of_birth(self, date_of_birth, user_account_id):
		query = "UPDATE user_account_date_of_birth SET date_of_birth = '" + date_of_birth + "' WHERE user_account_id = '" + user_account_id + "'";
		return query

	def user_account_date_of_birth_by_a_new_key(self, new_user_account_id, old_user_account_id):
		query = "UPDATE user_account_date_of_birth SET user_account_id = '" + new_user_account_id + "' WHERE user_account_id = '" + old_user_account_id + "'";
		return query

	def update_user_account_gender(self, gender, user_account_id):
		query = "UPDATE user_account_gender SET gender = '" + gender + "' WHERE user_account_id = '" + user_account_id + "'";
		return query

	def user_account_gender_by_a_new_key(self, new_user_account_id, old_user_account_id):
		query = "UPDATE user_account_gender SET user_account_id = '" + new_user_account_id + "' WHERE user_account_id = '" + old_user_account_id + "'";
		return query

	def update_user_account_status(self, status, user_account_id):
		query = "UPDATE user_account_status SET status = '" + status + "' WHERE user_account_id = '" + user_account_id + "'";
		return query

	def user_account_status_by_a_new_key(self, new_user_account_id, old_user_account_id):
		query = "UPDATE user_account_status SET user_account_id = '" + new_user_account_id + "' WHERE user_account_id = '" + old_user_account_id + "'";
		return query

	def update_user_account_email(self, email, user_account_id):
		query = "UPDATE user_account_email SET email = '" + email + "' WHERE user_account_id = '" + user_account_id + "'";
		return query

	def user_account_email_by_a_new_key(self, new_user_account_id, old_user_account_id):
		query = "UPDATE user_account_email SET user_account_id = '" + new_user_account_id + "' WHERE user_account_id = '" + old_user_account_id + "'";
		return query

	def update_user_account_password(self, password, user_account_id):
		query = "UPDATE user_account_password SET password = '" + password + "' WHERE user_account_id = '" + user_account_id + "'";
		return query

	def user_account_password_by_a_new_key(self, new_user_account_id, old_user_account_id):
		query = "UPDATE user_account_password SET user_account_id = '" + new_user_account_id + "' WHERE user_account_id = '" + old_user_account_id + "'";
		return query

	def update_user_account_photo(self, photo, user_account_id):
		query = "UPDATE user_account_photo SET photo = '" + photo + "' WHERE user_account_id = '" + user_account_id + "'";
		return query

	def user_account_photo_by_a_new_key(self, new_user_account_id, old_user_account_id):
		query = "UPDATE user_account_photo SET user_account_id = '" + new_user_account_id + "' WHERE user_account_id = '" + old_user_account_id + "'";
		return query

	def update_appeal(self, new_appeal_id, old_appeal_id):
		query = "UPDATE appeal SET appeal_id = '" + new_appeal_id + "' WHERE appeal_id = '" + old_appeal_id + "'";
		return query

	def update_appeal_subject(self, subject, appeal_id):
		query = "UPDATE appeal_subject SET subject = '" + subject + "' WHERE appeal_id = '" + appeal_id + "'";
		return query

	def appeal_subject_by_a_new_key(self, new_appeal_id, old_appeal_id):
		query = "UPDATE appeal_subject SET appeal_id = '" + new_appeal_id + "' WHERE appeal_id = '" + old_appeal_id + "'";
		return query

	def update_appeal_description(self, description, appeal_id):
		query = "UPDATE appeal_description SET description = '" + description + "' WHERE appeal_id = '" + appeal_id + "'";
		return query

	def appeal_description_by_a_new_key(self, new_appeal_id, old_appeal_id):
		query = "UPDATE appeal_description SET appeal_id = '" + new_appeal_id + "' WHERE appeal_id = '" + old_appeal_id + "'";
		return query

	def update_countryfiscal_yearmap(self, new_key_column, new_country_id, new_fiscal_year_id, old_key_column, old_country_id, old_fiscal_year_id):
		query = "UPDATE countryfiscal_yearmap SET key_column = '" + new_key_column + "',  country_id = '" + new_country_id + "',  fiscal_year_id = '" + new_fiscal_year_id + "' WHERE key_column = '" + old_key_column + "' AND country_id = '" + old_country_id + "' AND fiscal_year_id = '" + old_fiscal_year_id + "'";
		return query

	def update_countryprocurement_stagemap(self, new_key_column, new_country_id, new_procurement_stage_id, old_key_column, old_country_id, old_procurement_stage_id):
		query = "UPDATE countryprocurement_stagemap SET key_column = '" + new_key_column + "',  country_id = '" + new_country_id + "',  procurement_stage_id = '" + new_procurement_stage_id + "' WHERE key_column = '" + old_key_column + "' AND country_id = '" + old_country_id + "' AND procurement_stage_id = '" + old_procurement_stage_id + "'";
		return query

	def update_countryprocurement_typemap(self, new_key_column, new_country_id, new_procurement_type_id, old_key_column, old_country_id, old_procurement_type_id):
		query = "UPDATE countryprocurement_typemap SET key_column = '" + new_key_column + "',  country_id = '" + new_country_id + "',  procurement_type_id = '" + new_procurement_type_id + "' WHERE key_column = '" + old_key_column + "' AND country_id = '" + old_country_id + "' AND procurement_type_id = '" + old_procurement_type_id + "'";
		return query

	def update_countryprocurement_methodmap(self, new_key_column, new_country_id, new_procurement_method_id, old_key_column, old_country_id, old_procurement_method_id):
		query = "UPDATE countryprocurement_methodmap SET key_column = '" + new_key_column + "',  country_id = '" + new_country_id + "',  procurement_method_id = '" + new_procurement_method_id + "' WHERE key_column = '" + old_key_column + "' AND country_id = '" + old_country_id + "' AND procurement_method_id = '" + old_procurement_method_id + "'";
		return query

	def update_countryprocuring_entitymap(self, new_key_column, new_country_id, new_procuring_entity_id, old_key_column, old_country_id, old_procuring_entity_id):
		query = "UPDATE countryprocuring_entitymap SET key_column = '" + new_key_column + "',  country_id = '" + new_country_id + "',  procuring_entity_id = '" + new_procuring_entity_id + "' WHERE key_column = '" + old_key_column + "' AND country_id = '" + old_country_id + "' AND procuring_entity_id = '" + old_procuring_entity_id + "'";
		return query

	def update_countrysupplying_entitymap(self, new_key_column, new_country_id, new_supplying_entity_id, old_key_column, old_country_id, old_supplying_entity_id):
		query = "UPDATE countrysupplying_entitymap SET key_column = '" + new_key_column + "',  country_id = '" + new_country_id + "',  supplying_entity_id = '" + new_supplying_entity_id + "' WHERE key_column = '" + old_key_column + "' AND country_id = '" + old_country_id + "' AND supplying_entity_id = '" + old_supplying_entity_id + "'";
		return query

	def update_countryred_flagmap(self, new_key_column, new_country_id, new_red_flag_id, old_key_column, old_country_id, old_red_flag_id):
		query = "UPDATE countryred_flagmap SET key_column = '" + new_key_column + "',  country_id = '" + new_country_id + "',  red_flag_id = '" + new_red_flag_id + "' WHERE key_column = '" + old_key_column + "' AND country_id = '" + old_country_id + "' AND red_flag_id = '" + old_red_flag_id + "'";
		return query

	def update_countryillicit_schememap(self, new_key_column, new_country_id, new_illicit_scheme_id, old_key_column, old_country_id, old_illicit_scheme_id):
		query = "UPDATE countryillicit_schememap SET key_column = '" + new_key_column + "',  country_id = '" + new_country_id + "',  illicit_scheme_id = '" + new_illicit_scheme_id + "' WHERE key_column = '" + old_key_column + "' AND country_id = '" + old_country_id + "' AND illicit_scheme_id = '" + old_illicit_scheme_id + "'";
		return query

	def update_fiscal_yeartendermap(self, new_key_column, new_fiscal_year_id, new_tender_id, old_key_column, old_fiscal_year_id, old_tender_id):
		query = "UPDATE fiscal_yeartendermap SET key_column = '" + new_key_column + "',  fiscal_year_id = '" + new_fiscal_year_id + "',  tender_id = '" + new_tender_id + "' WHERE key_column = '" + old_key_column + "' AND fiscal_year_id = '" + old_fiscal_year_id + "' AND tender_id = '" + old_tender_id + "'";
		return query

	def update_fiscal_yearillicit_schememap(self, new_key_column, new_fiscal_year_id, new_illicit_scheme_id, old_key_column, old_fiscal_year_id, old_illicit_scheme_id):
		query = "UPDATE fiscal_yearillicit_schememap SET key_column = '" + new_key_column + "',  fiscal_year_id = '" + new_fiscal_year_id + "',  illicit_scheme_id = '" + new_illicit_scheme_id + "' WHERE key_column = '" + old_key_column + "' AND fiscal_year_id = '" + old_fiscal_year_id + "' AND illicit_scheme_id = '" + old_illicit_scheme_id + "'";
		return query

	def update_fiscal_yearred_flagmap(self, new_key_column, new_fiscal_year_id, new_red_flag_id, old_key_column, old_fiscal_year_id, old_red_flag_id):
		query = "UPDATE fiscal_yearred_flagmap SET key_column = '" + new_key_column + "',  fiscal_year_id = '" + new_fiscal_year_id + "',  red_flag_id = '" + new_red_flag_id + "' WHERE key_column = '" + old_key_column + "' AND fiscal_year_id = '" + old_fiscal_year_id + "' AND red_flag_id = '" + old_red_flag_id + "'";
		return query

	def update_fiscal_yearprocurement_stagemap(self, new_key_column, new_fiscal_year_id, new_procurement_stage_id, old_key_column, old_fiscal_year_id, old_procurement_stage_id):
		query = "UPDATE fiscal_yearprocurement_stagemap SET key_column = '" + new_key_column + "',  fiscal_year_id = '" + new_fiscal_year_id + "',  procurement_stage_id = '" + new_procurement_stage_id + "' WHERE key_column = '" + old_key_column + "' AND fiscal_year_id = '" + old_fiscal_year_id + "' AND procurement_stage_id = '" + old_procurement_stage_id + "'";
		return query

	def update_fiscal_yearprocurement_typemap(self, new_key_column, new_fiscal_year_id, new_procurement_type_id, old_key_column, old_fiscal_year_id, old_procurement_type_id):
		query = "UPDATE fiscal_yearprocurement_typemap SET key_column = '" + new_key_column + "',  fiscal_year_id = '" + new_fiscal_year_id + "',  procurement_type_id = '" + new_procurement_type_id + "' WHERE key_column = '" + old_key_column + "' AND fiscal_year_id = '" + old_fiscal_year_id + "' AND procurement_type_id = '" + old_procurement_type_id + "'";
		return query

	def update_fiscal_yearprocurement_methodmap(self, new_key_column, new_fiscal_year_id, new_procurement_method_id, old_key_column, old_fiscal_year_id, old_procurement_method_id):
		query = "UPDATE fiscal_yearprocurement_methodmap SET key_column = '" + new_key_column + "',  fiscal_year_id = '" + new_fiscal_year_id + "',  procurement_method_id = '" + new_procurement_method_id + "' WHERE key_column = '" + old_key_column + "' AND fiscal_year_id = '" + old_fiscal_year_id + "' AND procurement_method_id = '" + old_procurement_method_id + "'";
		return query

	def update_fiscal_yearbidmap(self, new_key_column, new_fiscal_year_id, new_bid_id, old_key_column, old_fiscal_year_id, old_bid_id):
		query = "UPDATE fiscal_yearbidmap SET key_column = '" + new_key_column + "',  fiscal_year_id = '" + new_fiscal_year_id + "',  bid_id = '" + new_bid_id + "' WHERE key_column = '" + old_key_column + "' AND fiscal_year_id = '" + old_fiscal_year_id + "' AND bid_id = '" + old_bid_id + "'";
		return query

	def update_fiscal_yearitemmap(self, new_key_column, new_fiscal_year_id, new_item_id, old_key_column, old_fiscal_year_id, old_item_id):
		query = "UPDATE fiscal_yearitemmap SET key_column = '" + new_key_column + "',  fiscal_year_id = '" + new_fiscal_year_id + "',  item_id = '" + new_item_id + "' WHERE key_column = '" + old_key_column + "' AND fiscal_year_id = '" + old_fiscal_year_id + "' AND item_id = '" + old_item_id + "'";
		return query

	def update_fiscal_yearcontractmap(self, new_key_column, new_fiscal_year_id, new_contract_id, old_key_column, old_fiscal_year_id, old_contract_id):
		query = "UPDATE fiscal_yearcontractmap SET key_column = '" + new_key_column + "',  fiscal_year_id = '" + new_fiscal_year_id + "',  contract_id = '" + new_contract_id + "' WHERE key_column = '" + old_key_column + "' AND fiscal_year_id = '" + old_fiscal_year_id + "' AND contract_id = '" + old_contract_id + "'";
		return query

	def update_fiscal_yearconfigurationmap(self, new_key_column, new_fiscal_year_id, new_configuration_id, old_key_column, old_fiscal_year_id, old_configuration_id):
		query = "UPDATE fiscal_yearconfigurationmap SET key_column = '" + new_key_column + "',  fiscal_year_id = '" + new_fiscal_year_id + "',  configuration_id = '" + new_configuration_id + "' WHERE key_column = '" + old_key_column + "' AND fiscal_year_id = '" + old_fiscal_year_id + "' AND configuration_id = '" + old_configuration_id + "'";
		return query

	def update_fiscal_yearfeemap(self, new_key_column, new_fiscal_year_id, new_fee_id, old_key_column, old_fiscal_year_id, old_fee_id):
		query = "UPDATE fiscal_yearfeemap SET key_column = '" + new_key_column + "',  fiscal_year_id = '" + new_fiscal_year_id + "',  fee_id = '" + new_fee_id + "' WHERE key_column = '" + old_key_column + "' AND fiscal_year_id = '" + old_fiscal_year_id + "' AND fee_id = '" + old_fee_id + "'";
		return query

	def update_fiscal_yearprocuring_entitymap(self, new_key_column, new_fiscal_year_id, new_procuring_entity_id, old_key_column, old_fiscal_year_id, old_procuring_entity_id):
		query = "UPDATE fiscal_yearprocuring_entitymap SET key_column = '" + new_key_column + "',  fiscal_year_id = '" + new_fiscal_year_id + "',  procuring_entity_id = '" + new_procuring_entity_id + "' WHERE key_column = '" + old_key_column + "' AND fiscal_year_id = '" + old_fiscal_year_id + "' AND procuring_entity_id = '" + old_procuring_entity_id + "'";
		return query

	def update_fiscal_yearsupplying_entitymap(self, new_key_column, new_fiscal_year_id, new_supplying_entity_id, old_key_column, old_fiscal_year_id, old_supplying_entity_id):
		query = "UPDATE fiscal_yearsupplying_entitymap SET key_column = '" + new_key_column + "',  fiscal_year_id = '" + new_fiscal_year_id + "',  supplying_entity_id = '" + new_supplying_entity_id + "' WHERE key_column = '" + old_key_column + "' AND fiscal_year_id = '" + old_fiscal_year_id + "' AND supplying_entity_id = '" + old_supplying_entity_id + "'";
		return query

	def update_fiscal_yearawardmap(self, new_key_column, new_fiscal_year_id, new_award_id, old_key_column, old_fiscal_year_id, old_award_id):
		query = "UPDATE fiscal_yearawardmap SET key_column = '" + new_key_column + "',  fiscal_year_id = '" + new_fiscal_year_id + "',  award_id = '" + new_award_id + "' WHERE key_column = '" + old_key_column + "' AND fiscal_year_id = '" + old_fiscal_year_id + "' AND award_id = '" + old_award_id + "'";
		return query

	def update_fiscal_yearplanmap(self, new_key_column, new_fiscal_year_id, new_plan_id, old_key_column, old_fiscal_year_id, old_plan_id):
		query = "UPDATE fiscal_yearplanmap SET key_column = '" + new_key_column + "',  fiscal_year_id = '" + new_fiscal_year_id + "',  plan_id = '" + new_plan_id + "' WHERE key_column = '" + old_key_column + "' AND fiscal_year_id = '" + old_fiscal_year_id + "' AND plan_id = '" + old_plan_id + "'";
		return query

	def update_red_flagconfigurationmap(self, new_key_column, new_red_flag_id, new_configuration_id, old_key_column, old_red_flag_id, old_configuration_id):
		query = "UPDATE red_flagconfigurationmap SET key_column = '" + new_key_column + "',  red_flag_id = '" + new_red_flag_id + "',  configuration_id = '" + new_configuration_id + "' WHERE key_column = '" + old_key_column + "' AND red_flag_id = '" + old_red_flag_id + "' AND configuration_id = '" + old_configuration_id + "'";
		return query

	def update_procurement_stagered_flagmap(self, new_key_column, new_procurement_stage_id, new_red_flag_id, old_key_column, old_procurement_stage_id, old_red_flag_id):
		query = "UPDATE procurement_stagered_flagmap SET key_column = '" + new_key_column + "',  procurement_stage_id = '" + new_procurement_stage_id + "',  red_flag_id = '" + new_red_flag_id + "' WHERE key_column = '" + old_key_column + "' AND procurement_stage_id = '" + old_procurement_stage_id + "' AND red_flag_id = '" + old_red_flag_id + "'";
		return query

	def update_procuring_entityred_flagmap(self, new_key_column, new_procuring_entity_id, new_red_flag_id, old_key_column, old_procuring_entity_id, old_red_flag_id):
		query = "UPDATE procuring_entityred_flagmap SET key_column = '" + new_key_column + "',  procuring_entity_id = '" + new_procuring_entity_id + "',  red_flag_id = '" + new_red_flag_id + "' WHERE key_column = '" + old_key_column + "' AND procuring_entity_id = '" + old_procuring_entity_id + "' AND red_flag_id = '" + old_red_flag_id + "'";
		return query

	def update_supplying_entityred_flagmap(self, new_key_column, new_supplying_entity_id, new_red_flag_id, old_key_column, old_supplying_entity_id, old_red_flag_id):
		query = "UPDATE supplying_entityred_flagmap SET key_column = '" + new_key_column + "',  supplying_entity_id = '" + new_supplying_entity_id + "',  red_flag_id = '" + new_red_flag_id + "' WHERE key_column = '" + old_key_column + "' AND supplying_entity_id = '" + old_supplying_entity_id + "' AND red_flag_id = '" + old_red_flag_id + "'";
		return query

	def update_procurement_typered_flagmap(self, new_key_column, new_procurement_type_id, new_red_flag_id, old_key_column, old_procurement_type_id, old_red_flag_id):
		query = "UPDATE procurement_typered_flagmap SET key_column = '" + new_key_column + "',  procurement_type_id = '" + new_procurement_type_id + "',  red_flag_id = '" + new_red_flag_id + "' WHERE key_column = '" + old_key_column + "' AND procurement_type_id = '" + old_procurement_type_id + "' AND red_flag_id = '" + old_red_flag_id + "'";
		return query

	def update_procurement_methodred_flagmap(self, new_key_column, new_procurement_method_id, new_red_flag_id, old_key_column, old_procurement_method_id, old_red_flag_id):
		query = "UPDATE procurement_methodred_flagmap SET key_column = '" + new_key_column + "',  procurement_method_id = '" + new_procurement_method_id + "',  red_flag_id = '" + new_red_flag_id + "' WHERE key_column = '" + old_key_column + "' AND procurement_method_id = '" + old_procurement_method_id + "' AND red_flag_id = '" + old_red_flag_id + "'";
		return query

	def update_tenderred_flagmap(self, new_key_column, new_tender_id, new_red_flag_id, old_key_column, old_tender_id, old_red_flag_id):
		query = "UPDATE tenderred_flagmap SET key_column = '" + new_key_column + "',  tender_id = '" + new_tender_id + "',  red_flag_id = '" + new_red_flag_id + "' WHERE key_column = '" + old_key_column + "' AND tender_id = '" + old_tender_id + "' AND red_flag_id = '" + old_red_flag_id + "'";
		return query

	def update_bidred_flagmap(self, new_key_column, new_bid_id, new_red_flag_id, old_key_column, old_bid_id, old_red_flag_id):
		query = "UPDATE bidred_flagmap SET key_column = '" + new_key_column + "',  bid_id = '" + new_bid_id + "',  red_flag_id = '" + new_red_flag_id + "' WHERE key_column = '" + old_key_column + "' AND bid_id = '" + old_bid_id + "' AND red_flag_id = '" + old_red_flag_id + "'";
		return query

	def update_itemred_flagmap(self, new_key_column, new_item_id, new_red_flag_id, old_key_column, old_item_id, old_red_flag_id):
		query = "UPDATE itemred_flagmap SET key_column = '" + new_key_column + "',  item_id = '" + new_item_id + "',  red_flag_id = '" + new_red_flag_id + "' WHERE key_column = '" + old_key_column + "' AND item_id = '" + old_item_id + "' AND red_flag_id = '" + old_red_flag_id + "'";
		return query

	def update_contractred_flagmap(self, new_key_column, new_contract_id, new_red_flag_id, old_key_column, old_contract_id, old_red_flag_id):
		query = "UPDATE contractred_flagmap SET key_column = '" + new_key_column + "',  contract_id = '" + new_contract_id + "',  red_flag_id = '" + new_red_flag_id + "' WHERE key_column = '" + old_key_column + "' AND contract_id = '" + old_contract_id + "' AND red_flag_id = '" + old_red_flag_id + "'";
		return query

	def update_illicit_schemered_flagmap(self, new_key_column, new_illicit_scheme_id, new_red_flag_id, old_key_column, old_illicit_scheme_id, old_red_flag_id):
		query = "UPDATE illicit_schemered_flagmap SET key_column = '" + new_key_column + "',  illicit_scheme_id = '" + new_illicit_scheme_id + "',  red_flag_id = '" + new_red_flag_id + "' WHERE key_column = '" + old_key_column + "' AND illicit_scheme_id = '" + old_illicit_scheme_id + "' AND red_flag_id = '" + old_red_flag_id + "'";
		return query

	def update_bidfeemap(self, new_key_column, new_bid_id, new_fee_id, old_key_column, old_bid_id, old_fee_id):
		query = "UPDATE bidfeemap SET key_column = '" + new_key_column + "',  bid_id = '" + new_bid_id + "',  fee_id = '" + new_fee_id + "' WHERE key_column = '" + old_key_column + "' AND bid_id = '" + old_bid_id + "' AND fee_id = '" + old_fee_id + "'";
		return query

	def update_bidpaymentmap(self, new_key_column, new_bid_id, new_payment_id, old_key_column, old_bid_id, old_payment_id):
		query = "UPDATE bidpaymentmap SET key_column = '" + new_key_column + "',  bid_id = '" + new_bid_id + "',  payment_id = '" + new_payment_id + "' WHERE key_column = '" + old_key_column + "' AND bid_id = '" + old_bid_id + "' AND payment_id = '" + old_payment_id + "'";
		return query

	def update_bidawardmap(self, new_key_column, new_bid_id, new_award_id, old_key_column, old_bid_id, old_award_id):
		query = "UPDATE bidawardmap SET key_column = '" + new_key_column + "',  bid_id = '" + new_bid_id + "',  award_id = '" + new_award_id + "' WHERE key_column = '" + old_key_column + "' AND bid_id = '" + old_bid_id + "' AND award_id = '" + old_award_id + "'";
		return query

	def update_tenderbidmap(self, new_key_column, new_tender_id, new_bid_id, old_key_column, old_tender_id, old_bid_id):
		query = "UPDATE tenderbidmap SET key_column = '" + new_key_column + "',  tender_id = '" + new_tender_id + "',  bid_id = '" + new_bid_id + "' WHERE key_column = '" + old_key_column + "' AND tender_id = '" + old_tender_id + "' AND bid_id = '" + old_bid_id + "'";
		return query

	def update_tenderfeemap(self, new_key_column, new_tender_id, new_fee_id, old_key_column, old_tender_id, old_fee_id):
		query = "UPDATE tenderfeemap SET key_column = '" + new_key_column + "',  tender_id = '" + new_tender_id + "',  fee_id = '" + new_fee_id + "' WHERE key_column = '" + old_key_column + "' AND tender_id = '" + old_tender_id + "' AND fee_id = '" + old_fee_id + "'";
		return query

	def update_tenderpaymentmap(self, new_key_column, new_tender_id, new_payment_id, old_key_column, old_tender_id, old_payment_id):
		query = "UPDATE tenderpaymentmap SET key_column = '" + new_key_column + "',  tender_id = '" + new_tender_id + "',  payment_id = '" + new_payment_id + "' WHERE key_column = '" + old_key_column + "' AND tender_id = '" + old_tender_id + "' AND payment_id = '" + old_payment_id + "'";
		return query

	def update_awardappealmap(self, new_key_column, new_award_id, new_appeal_id, old_key_column, old_award_id, old_appeal_id):
		query = "UPDATE awardappealmap SET key_column = '" + new_key_column + "',  award_id = '" + new_award_id + "',  appeal_id = '" + new_appeal_id + "' WHERE key_column = '" + old_key_column + "' AND award_id = '" + old_award_id + "' AND appeal_id = '" + old_appeal_id + "'";
		return query

	def update_procuring_entityprocurement_typemap(self, new_key_column, new_procuring_entity_id, new_procurement_type_id, old_key_column, old_procuring_entity_id, old_procurement_type_id):
		query = "UPDATE procuring_entityprocurement_typemap SET key_column = '" + new_key_column + "',  procuring_entity_id = '" + new_procuring_entity_id + "',  procurement_type_id = '" + new_procurement_type_id + "' WHERE key_column = '" + old_key_column + "' AND procuring_entity_id = '" + old_procuring_entity_id + "' AND procurement_type_id = '" + old_procurement_type_id + "'";
		return query

	def update_procuring_entityprocurement_methodmap(self, new_key_column, new_procuring_entity_id, new_procurement_method_id, old_key_column, old_procuring_entity_id, old_procurement_method_id):
		query = "UPDATE procuring_entityprocurement_methodmap SET key_column = '" + new_key_column + "',  procuring_entity_id = '" + new_procuring_entity_id + "',  procurement_method_id = '" + new_procurement_method_id + "' WHERE key_column = '" + old_key_column + "' AND procuring_entity_id = '" + old_procuring_entity_id + "' AND procurement_method_id = '" + old_procurement_method_id + "'";
		return query

	def update_procuring_entityprocurement_stagemap(self, new_key_column, new_procuring_entity_id, new_procurement_stage_id, old_key_column, old_procuring_entity_id, old_procurement_stage_id):
		query = "UPDATE procuring_entityprocurement_stagemap SET key_column = '" + new_key_column + "',  procuring_entity_id = '" + new_procuring_entity_id + "',  procurement_stage_id = '" + new_procurement_stage_id + "' WHERE key_column = '" + old_key_column + "' AND procuring_entity_id = '" + old_procuring_entity_id + "' AND procurement_stage_id = '" + old_procurement_stage_id + "'";
		return query

	def update_procuring_entitybidmap(self, new_key_column, new_procuring_entity_id, new_bid_id, old_key_column, old_procuring_entity_id, old_bid_id):
		query = "UPDATE procuring_entitybidmap SET key_column = '" + new_key_column + "',  procuring_entity_id = '" + new_procuring_entity_id + "',  bid_id = '" + new_bid_id + "' WHERE key_column = '" + old_key_column + "' AND procuring_entity_id = '" + old_procuring_entity_id + "' AND bid_id = '" + old_bid_id + "'";
		return query

	def update_procuring_entitytendermap(self, new_key_column, new_procuring_entity_id, new_tender_id, old_key_column, old_procuring_entity_id, old_tender_id):
		query = "UPDATE procuring_entitytendermap SET key_column = '" + new_key_column + "',  procuring_entity_id = '" + new_procuring_entity_id + "',  tender_id = '" + new_tender_id + "' WHERE key_column = '" + old_key_column + "' AND procuring_entity_id = '" + old_procuring_entity_id + "' AND tender_id = '" + old_tender_id + "'";
		return query

	def update_procuring_entitycontractmap(self, new_key_column, new_procuring_entity_id, new_contract_id, old_key_column, old_procuring_entity_id, old_contract_id):
		query = "UPDATE procuring_entitycontractmap SET key_column = '" + new_key_column + "',  procuring_entity_id = '" + new_procuring_entity_id + "',  contract_id = '" + new_contract_id + "' WHERE key_column = '" + old_key_column + "' AND procuring_entity_id = '" + old_procuring_entity_id + "' AND contract_id = '" + old_contract_id + "'";
		return query

	def update_procuring_entityillicit_schememap(self, new_key_column, new_procuring_entity_id, new_illicit_scheme_id, old_key_column, old_procuring_entity_id, old_illicit_scheme_id):
		query = "UPDATE procuring_entityillicit_schememap SET key_column = '" + new_key_column + "',  procuring_entity_id = '" + new_procuring_entity_id + "',  illicit_scheme_id = '" + new_illicit_scheme_id + "' WHERE key_column = '" + old_key_column + "' AND procuring_entity_id = '" + old_procuring_entity_id + "' AND illicit_scheme_id = '" + old_illicit_scheme_id + "'";
		return query

	def update_procuring_entityaddressmap(self, new_key_column, new_procuring_entity_id, new_address_id, old_key_column, old_procuring_entity_id, old_address_id):
		query = "UPDATE procuring_entityaddressmap SET key_column = '" + new_key_column + "',  procuring_entity_id = '" + new_procuring_entity_id + "',  address_id = '" + new_address_id + "' WHERE key_column = '" + old_key_column + "' AND procuring_entity_id = '" + old_procuring_entity_id + "' AND address_id = '" + old_address_id + "'";
		return query

	def update_procuring_entityattachmentmap(self, new_key_column, new_procuring_entity_id, new_attachment_id, old_key_column, old_procuring_entity_id, old_attachment_id):
		query = "UPDATE procuring_entityattachmentmap SET key_column = '" + new_key_column + "',  procuring_entity_id = '" + new_procuring_entity_id + "',  attachment_id = '" + new_attachment_id + "' WHERE key_column = '" + old_key_column + "' AND procuring_entity_id = '" + old_procuring_entity_id + "' AND attachment_id = '" + old_attachment_id + "'";
		return query

	def update_procuring_entityplanmap(self, new_key_column, new_procuring_entity_id, new_plan_id, old_key_column, old_procuring_entity_id, old_plan_id):
		query = "UPDATE procuring_entityplanmap SET key_column = '" + new_key_column + "',  procuring_entity_id = '" + new_procuring_entity_id + "',  plan_id = '" + new_plan_id + "' WHERE key_column = '" + old_key_column + "' AND procuring_entity_id = '" + old_procuring_entity_id + "' AND plan_id = '" + old_plan_id + "'";
		return query

	def update_procuring_entityawardmap(self, new_key_column, new_procuring_entity_id, new_award_id, old_key_column, old_procuring_entity_id, old_award_id):
		query = "UPDATE procuring_entityawardmap SET key_column = '" + new_key_column + "',  procuring_entity_id = '" + new_procuring_entity_id + "',  award_id = '" + new_award_id + "' WHERE key_column = '" + old_key_column + "' AND procuring_entity_id = '" + old_procuring_entity_id + "' AND award_id = '" + old_award_id + "'";
		return query

	def update_procuring_entitycontactmap(self, new_key_column, new_procuring_entity_id, new_contact_id, old_key_column, old_procuring_entity_id, old_contact_id):
		query = "UPDATE procuring_entitycontactmap SET key_column = '" + new_key_column + "',  procuring_entity_id = '" + new_procuring_entity_id + "',  contact_id = '" + new_contact_id + "' WHERE key_column = '" + old_key_column + "' AND procuring_entity_id = '" + old_procuring_entity_id + "' AND contact_id = '" + old_contact_id + "'";
		return query

	def update_procuring_entitypaymentmap(self, new_key_column, new_procuring_entity_id, new_payment_id, old_key_column, old_procuring_entity_id, old_payment_id):
		query = "UPDATE procuring_entitypaymentmap SET key_column = '" + new_key_column + "',  procuring_entity_id = '" + new_procuring_entity_id + "',  payment_id = '" + new_payment_id + "' WHERE key_column = '" + old_key_column + "' AND procuring_entity_id = '" + old_procuring_entity_id + "' AND payment_id = '" + old_payment_id + "'";
		return query

	def update_procuring_entityuser_accountmap(self, new_key_column, new_procuring_entity_id, new_user_account_id, old_key_column, old_procuring_entity_id, old_user_account_id):
		query = "UPDATE procuring_entityuser_accountmap SET key_column = '" + new_key_column + "',  procuring_entity_id = '" + new_procuring_entity_id + "',  user_account_id = '" + new_user_account_id + "' WHERE key_column = '" + old_key_column + "' AND procuring_entity_id = '" + old_procuring_entity_id + "' AND user_account_id = '" + old_user_account_id + "'";
		return query

	def update_procuring_entitysupplying_entitymap(self, new_key_column, new_procuring_entity_id, new_supplying_entity_id, old_key_column, old_procuring_entity_id, old_supplying_entity_id):
		query = "UPDATE procuring_entitysupplying_entitymap SET key_column = '" + new_key_column + "',  procuring_entity_id = '" + new_procuring_entity_id + "',  supplying_entity_id = '" + new_supplying_entity_id + "' WHERE key_column = '" + old_key_column + "' AND procuring_entity_id = '" + old_procuring_entity_id + "' AND supplying_entity_id = '" + old_supplying_entity_id + "'";
		return query

	def update_supplying_entityprocurement_typemap(self, new_key_column, new_supplying_entity_id, new_procurement_type_id, old_key_column, old_supplying_entity_id, old_procurement_type_id):
		query = "UPDATE supplying_entityprocurement_typemap SET key_column = '" + new_key_column + "',  supplying_entity_id = '" + new_supplying_entity_id + "',  procurement_type_id = '" + new_procurement_type_id + "' WHERE key_column = '" + old_key_column + "' AND supplying_entity_id = '" + old_supplying_entity_id + "' AND procurement_type_id = '" + old_procurement_type_id + "'";
		return query

	def update_supplying_entityprocurement_methodmap(self, new_key_column, new_supplying_entity_id, new_procurement_method_id, old_key_column, old_supplying_entity_id, old_procurement_method_id):
		query = "UPDATE supplying_entityprocurement_methodmap SET key_column = '" + new_key_column + "',  supplying_entity_id = '" + new_supplying_entity_id + "',  procurement_method_id = '" + new_procurement_method_id + "' WHERE key_column = '" + old_key_column + "' AND supplying_entity_id = '" + old_supplying_entity_id + "' AND procurement_method_id = '" + old_procurement_method_id + "'";
		return query

	def update_supplying_entityprocurement_stagemap(self, new_key_column, new_supplying_entity_id, new_procurement_stage_id, old_key_column, old_supplying_entity_id, old_procurement_stage_id):
		query = "UPDATE supplying_entityprocurement_stagemap SET key_column = '" + new_key_column + "',  supplying_entity_id = '" + new_supplying_entity_id + "',  procurement_stage_id = '" + new_procurement_stage_id + "' WHERE key_column = '" + old_key_column + "' AND supplying_entity_id = '" + old_supplying_entity_id + "' AND procurement_stage_id = '" + old_procurement_stage_id + "'";
		return query

	def update_supplying_entitybidmap(self, new_key_column, new_supplying_entity_id, new_bid_id, old_key_column, old_supplying_entity_id, old_bid_id):
		query = "UPDATE supplying_entitybidmap SET key_column = '" + new_key_column + "',  supplying_entity_id = '" + new_supplying_entity_id + "',  bid_id = '" + new_bid_id + "' WHERE key_column = '" + old_key_column + "' AND supplying_entity_id = '" + old_supplying_entity_id + "' AND bid_id = '" + old_bid_id + "'";
		return query

	def update_supplying_entitytendermap(self, new_key_column, new_supplying_entity_id, new_tender_id, old_key_column, old_supplying_entity_id, old_tender_id):
		query = "UPDATE supplying_entitytendermap SET key_column = '" + new_key_column + "',  supplying_entity_id = '" + new_supplying_entity_id + "',  tender_id = '" + new_tender_id + "' WHERE key_column = '" + old_key_column + "' AND supplying_entity_id = '" + old_supplying_entity_id + "' AND tender_id = '" + old_tender_id + "'";
		return query

	def update_supplying_entitycontractmap(self, new_key_column, new_supplying_entity_id, new_contract_id, old_key_column, old_supplying_entity_id, old_contract_id):
		query = "UPDATE supplying_entitycontractmap SET key_column = '" + new_key_column + "',  supplying_entity_id = '" + new_supplying_entity_id + "',  contract_id = '" + new_contract_id + "' WHERE key_column = '" + old_key_column + "' AND supplying_entity_id = '" + old_supplying_entity_id + "' AND contract_id = '" + old_contract_id + "'";
		return query

	def update_supplying_entityillicit_schememap(self, new_key_column, new_supplying_entity_id, new_illicit_scheme_id, old_key_column, old_supplying_entity_id, old_illicit_scheme_id):
		query = "UPDATE supplying_entityillicit_schememap SET key_column = '" + new_key_column + "',  supplying_entity_id = '" + new_supplying_entity_id + "',  illicit_scheme_id = '" + new_illicit_scheme_id + "' WHERE key_column = '" + old_key_column + "' AND supplying_entity_id = '" + old_supplying_entity_id + "' AND illicit_scheme_id = '" + old_illicit_scheme_id + "'";
		return query

	def update_supplying_entityaddressmap(self, new_key_column, new_supplying_entity_id, new_address_id, old_key_column, old_supplying_entity_id, old_address_id):
		query = "UPDATE supplying_entityaddressmap SET key_column = '" + new_key_column + "',  supplying_entity_id = '" + new_supplying_entity_id + "',  address_id = '" + new_address_id + "' WHERE key_column = '" + old_key_column + "' AND supplying_entity_id = '" + old_supplying_entity_id + "' AND address_id = '" + old_address_id + "'";
		return query

	def update_supplying_entityattachmentmap(self, new_key_column, new_supplying_entity_id, new_attachment_id, old_key_column, old_supplying_entity_id, old_attachment_id):
		query = "UPDATE supplying_entityattachmentmap SET key_column = '" + new_key_column + "',  supplying_entity_id = '" + new_supplying_entity_id + "',  attachment_id = '" + new_attachment_id + "' WHERE key_column = '" + old_key_column + "' AND supplying_entity_id = '" + old_supplying_entity_id + "' AND attachment_id = '" + old_attachment_id + "'";
		return query

	def update_supplying_entityawardmap(self, new_key_column, new_supplying_entity_id, new_award_id, old_key_column, old_supplying_entity_id, old_award_id):
		query = "UPDATE supplying_entityawardmap SET key_column = '" + new_key_column + "',  supplying_entity_id = '" + new_supplying_entity_id + "',  award_id = '" + new_award_id + "' WHERE key_column = '" + old_key_column + "' AND supplying_entity_id = '" + old_supplying_entity_id + "' AND award_id = '" + old_award_id + "'";
		return query

	def update_supplying_entitycontactmap(self, new_key_column, new_supplying_entity_id, new_contact_id, old_key_column, old_supplying_entity_id, old_contact_id):
		query = "UPDATE supplying_entitycontactmap SET key_column = '" + new_key_column + "',  supplying_entity_id = '" + new_supplying_entity_id + "',  contact_id = '" + new_contact_id + "' WHERE key_column = '" + old_key_column + "' AND supplying_entity_id = '" + old_supplying_entity_id + "' AND contact_id = '" + old_contact_id + "'";
		return query

	def update_supplying_entitypaymentmap(self, new_key_column, new_supplying_entity_id, new_payment_id, old_key_column, old_supplying_entity_id, old_payment_id):
		query = "UPDATE supplying_entitypaymentmap SET key_column = '" + new_key_column + "',  supplying_entity_id = '" + new_supplying_entity_id + "',  payment_id = '" + new_payment_id + "' WHERE key_column = '" + old_key_column + "' AND supplying_entity_id = '" + old_supplying_entity_id + "' AND payment_id = '" + old_payment_id + "'";
		return query

	def update_supplying_entityuser_accountmap(self, new_key_column, new_supplying_entity_id, new_user_account_id, old_key_column, old_supplying_entity_id, old_user_account_id):
		query = "UPDATE supplying_entityuser_accountmap SET key_column = '" + new_key_column + "',  supplying_entity_id = '" + new_supplying_entity_id + "',  user_account_id = '" + new_user_account_id + "' WHERE key_column = '" + old_key_column + "' AND supplying_entity_id = '" + old_supplying_entity_id + "' AND user_account_id = '" + old_user_account_id + "'";
		return query

	def update_contractawardmap(self, new_key_column, new_contract_id, new_award_id, old_key_column, old_contract_id, old_award_id):
		query = "UPDATE contractawardmap SET key_column = '" + new_key_column + "',  contract_id = '" + new_contract_id + "',  award_id = '" + new_award_id + "' WHERE key_column = '" + old_key_column + "' AND contract_id = '" + old_contract_id + "' AND award_id = '" + old_award_id + "'";
		return query

	def update_paymentfeemap(self, new_key_column, new_payment_id, new_fee_id, old_key_column, old_payment_id, old_fee_id):
		query = "UPDATE paymentfeemap SET key_column = '" + new_key_column + "',  payment_id = '" + new_payment_id + "',  fee_id = '" + new_fee_id + "' WHERE key_column = '" + old_key_column + "' AND payment_id = '" + old_payment_id + "' AND fee_id = '" + old_fee_id + "'";
		return query

	def update_alert_authorityuser_accountmap(self, new_key_column, new_alert_authority_id, new_user_account_id, old_key_column, old_alert_authority_id, old_user_account_id):
		query = "UPDATE alert_authorityuser_accountmap SET key_column = '" + new_key_column + "',  alert_authority_id = '" + new_alert_authority_id + "',  user_account_id = '" + new_user_account_id + "' WHERE key_column = '" + old_key_column + "' AND alert_authority_id = '" + old_alert_authority_id + "' AND user_account_id = '" + old_user_account_id + "'";
		return query

	def update_alert_authorityalert_levelmap(self, new_key_column, new_alert_authority_id, new_alert_level_id, old_key_column, old_alert_authority_id, old_alert_level_id):
		query = "UPDATE alert_authorityalert_levelmap SET key_column = '" + new_key_column + "',  alert_authority_id = '" + new_alert_authority_id + "',  alert_level_id = '" + new_alert_level_id + "' WHERE key_column = '" + old_key_column + "' AND alert_authority_id = '" + old_alert_authority_id + "' AND alert_level_id = '" + old_alert_level_id + "'";
		return query

	def update_alert_authorityalertmap(self, new_key_column, new_alert_authority_id, new_alert_id, old_key_column, old_alert_authority_id, old_alert_id):
		query = "UPDATE alert_authorityalertmap SET key_column = '" + new_key_column + "',  alert_authority_id = '" + new_alert_authority_id + "',  alert_id = '" + new_alert_id + "' WHERE key_column = '" + old_key_column + "' AND alert_authority_id = '" + old_alert_authority_id + "' AND alert_id = '" + old_alert_id + "'";
		return query

	def update_alert_authorityaddressmap(self, new_key_column, new_alert_authority_id, new_address_id, old_key_column, old_alert_authority_id, old_address_id):
		query = "UPDATE alert_authorityaddressmap SET key_column = '" + new_key_column + "',  alert_authority_id = '" + new_alert_authority_id + "',  address_id = '" + new_address_id + "' WHERE key_column = '" + old_key_column + "' AND alert_authority_id = '" + old_alert_authority_id + "' AND address_id = '" + old_address_id + "'";
		return query

	def update_alert_leveluser_accountmap(self, new_key_column, new_alert_level_id, new_user_account_id, old_key_column, old_alert_level_id, old_user_account_id):
		query = "UPDATE alert_leveluser_accountmap SET key_column = '" + new_key_column + "',  alert_level_id = '" + new_alert_level_id + "',  user_account_id = '" + new_user_account_id + "' WHERE key_column = '" + old_key_column + "' AND alert_level_id = '" + old_alert_level_id + "' AND user_account_id = '" + old_user_account_id + "'";
		return query

	def update_alert_levelred_flagmap(self, new_key_column, new_alert_level_id, new_red_flag_id, old_key_column, old_alert_level_id, old_red_flag_id):
		query = "UPDATE alert_levelred_flagmap SET key_column = '" + new_key_column + "',  alert_level_id = '" + new_alert_level_id + "',  red_flag_id = '" + new_red_flag_id + "' WHERE key_column = '" + old_key_column + "' AND alert_level_id = '" + old_alert_level_id + "' AND red_flag_id = '" + old_red_flag_id + "'";
		return query

	def update_alert_leveladdressmap(self, new_key_column, new_alert_level_id, new_address_id, old_key_column, old_alert_level_id, old_address_id):
		query = "UPDATE alert_leveladdressmap SET key_column = '" + new_key_column + "',  alert_level_id = '" + new_alert_level_id + "',  address_id = '" + new_address_id + "' WHERE key_column = '" + old_key_column + "' AND alert_level_id = '" + old_alert_level_id + "' AND address_id = '" + old_address_id + "'";
		return query

	def update_alertred_flagmap(self, new_key_column, new_alert_id, new_red_flag_id, old_key_column, old_alert_id, old_red_flag_id):
		query = "UPDATE alertred_flagmap SET key_column = '" + new_key_column + "',  alert_id = '" + new_alert_id + "',  red_flag_id = '" + new_red_flag_id + "' WHERE key_column = '" + old_key_column + "' AND alert_id = '" + old_alert_id + "' AND red_flag_id = '" + old_red_flag_id + "'";
		return query

	def update_alertattachmentmap(self, new_key_column, new_alert_id, new_attachment_id, old_key_column, old_alert_id, old_attachment_id):
		query = "UPDATE alertattachmentmap SET key_column = '" + new_key_column + "',  alert_id = '" + new_alert_id + "',  attachment_id = '" + new_attachment_id + "' WHERE key_column = '" + old_key_column + "' AND alert_id = '" + old_alert_id + "' AND attachment_id = '" + old_attachment_id + "'";
		return query

	def update_alert_authoritycontactmap(self, new_key_column, new_alert_authority_id, new_contact_id, old_key_column, old_alert_authority_id, old_contact_id):
		query = "UPDATE alert_authoritycontactmap SET key_column = '" + new_key_column + "',  alert_authority_id = '" + new_alert_authority_id + "',  contact_id = '" + new_contact_id + "' WHERE key_column = '" + old_key_column + "' AND alert_authority_id = '" + old_alert_authority_id + "' AND contact_id = '" + old_contact_id + "'";
		return query

	def update_alert_levelcontactmap(self, new_key_column, new_alert_level_id, new_contact_id, old_key_column, old_alert_level_id, old_contact_id):
		query = "UPDATE alert_levelcontactmap SET key_column = '" + new_key_column + "',  alert_level_id = '" + new_alert_level_id + "',  contact_id = '" + new_contact_id + "' WHERE key_column = '" + old_key_column + "' AND alert_level_id = '" + old_alert_level_id + "' AND contact_id = '" + old_contact_id + "'";
		return query

	def update_user_accountcontactmap(self, new_key_column, new_user_account_id, new_contact_id, old_key_column, old_user_account_id, old_contact_id):
		query = "UPDATE user_accountcontactmap SET key_column = '" + new_key_column + "',  user_account_id = '" + new_user_account_id + "',  contact_id = '" + new_contact_id + "' WHERE key_column = '" + old_key_column + "' AND user_account_id = '" + old_user_account_id + "' AND contact_id = '" + old_contact_id + "'";
		return query

	def update_user_accountaddressmap(self, new_key_column, new_user_account_id, new_address_id, old_key_column, old_user_account_id, old_address_id):
		query = "UPDATE user_accountaddressmap SET key_column = '" + new_key_column + "',  user_account_id = '" + new_user_account_id + "',  address_id = '" + new_address_id + "' WHERE key_column = '" + old_key_column + "' AND user_account_id = '" + old_user_account_id + "' AND address_id = '" + old_address_id + "'";
		return query

	def update_user_accountsubmissionmap(self, new_key_column, new_user_account_id, new_submission_id, old_key_column, old_user_account_id, old_submission_id):
		query = "UPDATE user_accountsubmissionmap SET key_column = '" + new_key_column + "',  user_account_id = '" + new_user_account_id + "',  submission_id = '" + new_submission_id + "' WHERE key_column = '" + old_key_column + "' AND user_account_id = '" + old_user_account_id + "' AND submission_id = '" + old_submission_id + "'";
		return query

	def update_procurement_stagesubmissionmap(self, new_key_column, new_procurement_stage_id, new_submission_id, old_key_column, old_procurement_stage_id, old_submission_id):
		query = "UPDATE procurement_stagesubmissionmap SET key_column = '" + new_key_column + "',  procurement_stage_id = '" + new_procurement_stage_id + "',  submission_id = '" + new_submission_id + "' WHERE key_column = '" + old_key_column + "' AND procurement_stage_id = '" + old_procurement_stage_id + "' AND submission_id = '" + old_submission_id + "'";
		return query

	def update_plansubmissionmap(self, new_key_column, new_plan_id, new_submission_id, old_key_column, old_plan_id, old_submission_id):
		query = "UPDATE plansubmissionmap SET key_column = '" + new_key_column + "',  plan_id = '" + new_plan_id + "',  submission_id = '" + new_submission_id + "' WHERE key_column = '" + old_key_column + "' AND plan_id = '" + old_plan_id + "' AND submission_id = '" + old_submission_id + "'";
		return query

	def update_submissionattachmentmap(self, new_key_column, new_submission_id, new_attachment_id, old_key_column, old_submission_id, old_attachment_id):
		query = "UPDATE submissionattachmentmap SET key_column = '" + new_key_column + "',  submission_id = '" + new_submission_id + "',  attachment_id = '" + new_attachment_id + "' WHERE key_column = '" + old_key_column + "' AND submission_id = '" + old_submission_id + "' AND attachment_id = '" + old_attachment_id + "'";
		return query

	def update_appealattachmentmap(self, new_key_column, new_appeal_id, new_attachment_id, old_key_column, old_appeal_id, old_attachment_id):
		query = "UPDATE appealattachmentmap SET key_column = '" + new_key_column + "',  appeal_id = '" + new_appeal_id + "',  attachment_id = '" + new_attachment_id + "' WHERE key_column = '" + old_key_column + "' AND appeal_id = '" + old_appeal_id + "' AND attachment_id = '" + old_attachment_id + "'";
		return query

	def update_user_accountattachmentmap(self, new_key_column, new_user_account_id, new_attachment_id, old_key_column, old_user_account_id, old_attachment_id):
		query = "UPDATE user_accountattachmentmap SET key_column = '" + new_key_column + "',  user_account_id = '" + new_user_account_id + "',  attachment_id = '" + new_attachment_id + "' WHERE key_column = '" + old_key_column + "' AND user_account_id = '" + old_user_account_id + "' AND attachment_id = '" + old_attachment_id + "'";
		return query

	def update_awardsubmissionmap(self, new_key_column, new_award_id, new_submission_id, old_key_column, old_award_id, old_submission_id):
		query = "UPDATE awardsubmissionmap SET key_column = '" + new_key_column + "',  award_id = '" + new_award_id + "',  submission_id = '" + new_submission_id + "' WHERE key_column = '" + old_key_column + "' AND award_id = '" + old_award_id + "' AND submission_id = '" + old_submission_id + "'";
		return query

	def update_user_accountplanmap(self, new_key_column, new_user_account_id, new_plan_id, old_key_column, old_user_account_id, old_plan_id):
		query = "UPDATE user_accountplanmap SET key_column = '" + new_key_column + "',  user_account_id = '" + new_user_account_id + "',  plan_id = '" + new_plan_id + "' WHERE key_column = '" + old_key_column + "' AND user_account_id = '" + old_user_account_id + "' AND plan_id = '" + old_plan_id + "'";
		return query

	def update_awardtendermap(self, new_key_column, new_award_id, new_tender_id, old_key_column, old_award_id, old_tender_id):
		query = "UPDATE awardtendermap SET key_column = '" + new_key_column + "',  award_id = '" + new_award_id + "',  tender_id = '" + new_tender_id + "' WHERE key_column = '" + old_key_column + "' AND award_id = '" + old_award_id + "' AND tender_id = '" + old_tender_id + "'";
		return query

	def update_bidsubmissionmap(self, new_key_column, new_bid_id, new_submission_id, old_key_column, old_bid_id, old_submission_id):
		query = "UPDATE bidsubmissionmap SET key_column = '" + new_key_column + "',  bid_id = '" + new_bid_id + "',  submission_id = '" + new_submission_id + "' WHERE key_column = '" + old_key_column + "' AND bid_id = '" + old_bid_id + "' AND submission_id = '" + old_submission_id + "'";
		return query

	def update_tenderappealmap(self, new_key_column, new_tender_id, new_appeal_id, old_key_column, old_tender_id, old_appeal_id):
		query = "UPDATE tenderappealmap SET key_column = '" + new_key_column + "',  tender_id = '" + new_tender_id + "',  appeal_id = '" + new_appeal_id + "' WHERE key_column = '" + old_key_column + "' AND tender_id = '" + old_tender_id + "' AND appeal_id = '" + old_appeal_id + "'";
		return query




