
def insert_alert_levelred_flagmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, alert_level_id, red_flag_id):

	query_executor.execute(selection_object.select_alert_levelred_flagmap(key_column, alert_level_id, red_flag_id))
	alert_levelred_flagmap_check_query_result = query_executor.fetchall()
	result_list_length = len(alert_levelred_flagmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_levelred_flagmap(key_column, alert_level_id, red_flag_id))
		database_connection_object.commit()