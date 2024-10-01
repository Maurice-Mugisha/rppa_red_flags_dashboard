
def insert_userattachmentmap(query_executor, selection_object, insertion_object, key_column, user_id, attachment_id):

	query_executor.execute(selection_object.select_userattachmentmap(key_column, user_id, attachment_id))
	userattachmentmap_check_query_result = query_executor.fetchall()
	result_list_length = len(userattachmentmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_userattachmentmap(key_column, user_id, attachment_id))
		database_connection_object.commit()