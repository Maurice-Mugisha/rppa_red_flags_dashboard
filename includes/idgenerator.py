import datetime
import pytz
import random



class IDGenerator:


	def __init__(self, continent, city):
		self.continent = continent
		self.city = city

	def get_generic_id(self):
		datetime_object = datetime.datetime.now()
		relative_time_zone_string = self.continent + "/" + self.city
		relative_time_zone = pytz.timezone(relative_time_zone_string)
		datetime_object = relative_time_zone.localize(datetime_object)
		return datetime_object.strftime("%Y-%m-%d") + " " + datetime_object.strftime("%T:%M:%p")
	

	def set_time_zone_continent(self, continent):
		self.continent = continent


	def set_time_zone_city(self, city):
		self.city = city


	# Set the domain to minimize stochastic induction for small domains (probability theory of random numbers)
	# Failure to do this may lead to key generation failures under large events that can be greater than or equal to the sample space (actually, even less)
	# The sample space in this case has been appropriately set)
	def get_random_number(self):
		start = 0
		end = 70000
		random_number = random.randint(start, end)
		return str(random_number)

	def generate_random_id(self):
		key_column = self.get_generic_id() + " " + self.get_random_number()
		return key_column



	def generate_country_id(self):
		entity_name = "COUNTRY"
		country_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return country_id


	def generate_fiscal_year_id(self):
		entity_name = "FISCAL_YEAR"
		fiscal_year_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return fiscal_year_id


	def generate_configuration_id(self):
		entity_name = "CONFIGURATION"
		configuration_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return configuration_id


	def generate_red_flag_id(self):
		entity_name = "RED_FLAG"
		red_flag_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return red_flag_id


	def generate_illicit_scheme_id(self):
		entity_name = "ILLICIT_SCHEME"
		illicit_scheme_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return illicit_scheme_id


	def generate_procurement_stage_id(self):
		entity_name = "PROCUREMENT_STAGE"
		procurement_stage_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return procurement_stage_id


	def generate_submission_id(self):
		entity_name = "SUBMISSION"
		submission_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return submission_id


	def generate_procurement_type_id(self):
		entity_name = "PROCUREMENT_TYPE"
		procurement_type_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return procurement_type_id


	def generate_procurement_method_id(self):
		entity_name = "PROCUREMENT_METHOD"
		procurement_method_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return procurement_method_id


	def generate_bid_id(self):
		entity_name = "BID"
		bid_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return bid_id


	def generate_item_id(self):
		entity_name = "ITEM"
		item_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return item_id


	def generate_procuring_entity_id(self):
		entity_name = "PROCURING_ENTITY"
		procuring_entity_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return procuring_entity_id


	def generate_supplying_entity_id(self):
		entity_name = "SUPPLYING_ENTITY"
		supplying_entity_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return supplying_entity_id


	def generate_address_id(self):
		entity_name = "ADDRESS"
		address_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return address_id


	def generate_tender_id(self):
		entity_name = "TENDER"
		tender_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return tender_id


	def generate_attachment_id(self):
		entity_name = "ATTACHMENT"
		attachment_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return attachment_id


	def generate_award_id(self):
		entity_name = "AWARD"
		award_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return award_id


	def generate_contact_id(self):
		entity_name = "CONTACT"
		contact_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return contact_id


	def generate_contract_id(self):
		entity_name = "CONTRACT"
		contract_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return contract_id


	def generate_fee_id(self):
		entity_name = "FEE"
		fee_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return fee_id


	def generate_payment_id(self):
		entity_name = "PAYMENT"
		payment_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return payment_id


	def generate_plan_id(self):
		entity_name = "PLAN"
		plan_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return plan_id


	def generate_alert_id(self):
		entity_name = "ALERT"
		alert_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return alert_id


	def generate_alert_authority_id(self):
		entity_name = "ALERT_AUTHORITY"
		alert_authority_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return alert_authority_id


	def generate_alert_level_id(self):
		entity_name = "ALERT_LEVEL"
		alert_level_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return alert_level_id


	def generate_user_account_id(self):
		entity_name = "USER_ACCOUNT"
		user_account_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return user_account_id


	def generate_appeal_id(self):
		entity_name = "APPEAL"
		appeal_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return appeal_id





# End of class file