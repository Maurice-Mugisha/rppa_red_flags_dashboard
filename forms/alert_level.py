
def insert_alert_level(database_connection_object, query_executor, selection_object, insertion_object, alert_level_id, name, description):

	query_executor.execute(selection_object.select_alert_level(alert_level_id))
	alert_level_check_query_result = query_executor.fetchall()
	result_list_length = len(alert_level_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_level(alert_level_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_level_name(alert_level_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_level_description(alert_level_id, description))
		database_connection_object.commit()
