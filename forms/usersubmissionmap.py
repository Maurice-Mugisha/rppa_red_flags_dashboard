
def insert_usersubmissionmap(query_executor, selection_object, insertion_object, key_column, user_id, submission_id):

	query_executor.execute(selection_object.select_usersubmissionmap(key_column, user_id, submission_id))
	usersubmissionmap_check_query_result = query_executor.fetchall()
	result_list_length = len(usersubmissionmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_usersubmissionmap(key_column, user_id, submission_id))
		database_connection_object.commit()