
def insert_supplying_entityattachmentmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, supplying_entity_id, attachment_id):

	query_executor.execute(selection_object.select_supplying_entityattachmentmap(key_column, supplying_entity_id, attachment_id))
	supplying_entityattachmentmap_check_query_result = query_executor.fetchall()
	result_list_length = len(supplying_entityattachmentmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entityattachmentmap(key_column, supplying_entity_id, attachment_id))
		database_connection_object.commit()