
def insert_illicit_schemered_flagmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, illicit_scheme_id, red_flag_id):

	query_executor.execute(selection_object.select_illicit_schemered_flagmap(key_column, illicit_scheme_id, red_flag_id))
	illicit_schemered_flagmap_check_query_result = query_executor.fetchall()
	result_list_length = len(illicit_schemered_flagmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_illicit_schemered_flagmap(key_column, illicit_scheme_id, red_flag_id))
		database_connection_object.commit()