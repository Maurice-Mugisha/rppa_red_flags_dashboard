
def insert_red_flagconfigurationmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, red_flag_id, configuration_id):

	query_executor.execute(selection_object.select_red_flagconfigurationmap(key_column, red_flag_id, configuration_id))
	red_flagconfigurationmap_check_query_result = query_executor.fetchall()
	result_list_length = len(red_flagconfigurationmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_red_flagconfigurationmap(key_column, red_flag_id, configuration_id))
		database_connection_object.commit()