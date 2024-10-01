
def insert_alert(database_connection_object, query_executor, selection_object, insertion_object, alert_id, subject, description):

	query_executor.execute(selection_object.select_alert(alert_id))
	alert_check_query_result = query_executor.fetchall()
	result_list_length = len(alert_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert(alert_id))
		database_connection_object.commit()

	if len(str(subject).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_subject(alert_id, subject))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_description(alert_id, description))
		database_connection_object.commit()
