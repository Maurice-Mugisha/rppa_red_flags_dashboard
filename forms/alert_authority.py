
def insert_alert_authority(database_connection_object, query_executor, selection_object, insertion_object, alert_authority_id, name, description):

	query_executor.execute(selection_object.select_alert_authority(alert_authority_id))
	alert_authority_check_query_result = query_executor.fetchall()
	result_list_length = len(alert_authority_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_authority(alert_authority_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_authority_name(alert_authority_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_authority_description(alert_authority_id, description))
		database_connection_object.commit()
