
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
