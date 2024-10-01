
def insert_user_accountsubmissionmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, user_account_id, submission_id):

	query_executor.execute(selection_object.select_user_accountsubmissionmap(key_column, user_account_id, submission_id))
	user_accountsubmissionmap_check_query_result = query_executor.fetchall()
	result_list_length = len(user_accountsubmissionmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_accountsubmissionmap(key_column, user_account_id, submission_id))
		database_connection_object.commit()