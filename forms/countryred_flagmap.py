
def insert_countryred_flagmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, country_id, red_flag_id):

	query_executor.execute(selection_object.select_countryred_flagmap(key_column, country_id, red_flag_id))
	countryred_flagmap_check_query_result = query_executor.fetchall()
	result_list_length = len(countryred_flagmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_countryred_flagmap(key_column, country_id, red_flag_id))
		database_connection_object.commit()