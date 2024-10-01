
def insert_alert_leveluser_accountmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, alert_level_id, user_account_id):

	query_executor.execute(selection_object.select_alert_leveluser_accountmap(key_column, alert_level_id, user_account_id))
	alert_leveluser_accountmap_check_query_result = query_executor.fetchall()
	result_list_length = len(alert_leveluser_accountmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_alert_leveluser_accountmap(key_column, alert_level_id, user_account_id))
		database_connection_object.commit()