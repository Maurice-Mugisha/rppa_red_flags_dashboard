
def insert_alert_authoritycontactmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, alert_authority_id, contact_id):

	query_executor.execute(selection_object.select_alert_authoritycontactmap(key_column, alert_authority_id, contact_id))
	alert_authoritycontactmap_check_query_result = query_executor.fetchall()
	result_list_length = len(alert_authoritycontactmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_authoritycontactmap(key_column, alert_authority_id, contact_id))
		database_connection_object.commit()