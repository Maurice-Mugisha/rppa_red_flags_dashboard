
def insert_alert_authorityalert_levelmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, alert_authority_id, alert_level_id):

	query_executor.execute(selection_object.select_alert_authorityalert_levelmap(key_column, alert_authority_id, alert_level_id))
	alert_authorityalert_levelmap_check_query_result = query_executor.fetchall()
	result_list_length = len(alert_authorityalert_levelmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_authorityalert_levelmap(key_column, alert_authority_id, alert_level_id))
		database_connection_object.commit()