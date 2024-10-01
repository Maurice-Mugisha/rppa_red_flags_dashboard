
def insert_alertattachmentmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, alert_id, attachment_id):

	query_executor.execute(selection_object.select_alertattachmentmap(key_column, alert_id, attachment_id))
	alertattachmentmap_check_query_result = query_executor.fetchall()
	result_list_length = len(alertattachmentmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_alertattachmentmap(key_column, alert_id, attachment_id))
		database_connection_object.commit()