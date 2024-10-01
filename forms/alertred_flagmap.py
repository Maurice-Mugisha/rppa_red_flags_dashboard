
def insert_alertred_flagmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, alert_id, red_flag_id):

	query_executor.execute(selection_object.select_alertred_flagmap(key_column, alert_id, red_flag_id))
	alertred_flagmap_check_query_result = query_executor.fetchall()
	result_list_length = len(alertred_flagmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_alertred_flagmap(key_column, alert_id, red_flag_id))
		database_connection_object.commit()