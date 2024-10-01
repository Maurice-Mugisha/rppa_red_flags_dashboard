
def insert_appealattachmentmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, appeal_id, attachment_id):

	query_executor.execute(selection_object.select_appealattachmentmap(key_column, appeal_id, attachment_id))
	appealattachmentmap_check_query_result = query_executor.fetchall()
	result_list_length = len(appealattachmentmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_appealattachmentmap(key_column, appeal_id, attachment_id))
		database_connection_object.commit()