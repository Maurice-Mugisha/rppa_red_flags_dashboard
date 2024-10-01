
def insert_submissionattachmentmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, submission_id, attachment_id):

	query_executor.execute(selection_object.select_submissionattachmentmap(key_column, submission_id, attachment_id))
	submissionattachmentmap_check_query_result = query_executor.fetchall()
	result_list_length = len(submissionattachmentmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_submissionattachmentmap(key_column, submission_id, attachment_id))
		database_connection_object.commit()