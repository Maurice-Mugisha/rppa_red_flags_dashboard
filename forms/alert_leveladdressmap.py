
def insert_alert_leveladdressmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, alert_level_id, address_id):

	query_executor.execute(selection_object.select_alert_leveladdressmap(key_column, alert_level_id, address_id))
	alert_leveladdressmap_check_query_result = query_executor.fetchall()
	result_list_length = len(alert_leveladdressmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_leveladdressmap(key_column, alert_level_id, address_id))
		database_connection_object.commit()