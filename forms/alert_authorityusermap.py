
def insert_alert_authorityusermap(query_executor, selection_object, insertion_object, key_column, alert_authority_id, user_id):

	query_executor.execute(selection_object.select_alert_authorityusermap(key_column, alert_authority_id, user_id))
	alert_authorityusermap_check_query_result = query_executor.fetchall()
	result_list_length = len(alert_authorityusermap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_authorityusermap(key_column, alert_authority_id, user_id))
		database_connection_object.commit()