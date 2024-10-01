
def insert_procuring_entitytendermap(database_connection_object, query_executor, selection_object, insertion_object, key_column, procuring_entity_id, tender_id):

	query_executor.execute(selection_object.select_procuring_entitytendermap(key_column, procuring_entity_id, tender_id))
	procuring_entitytendermap_check_query_result = query_executor.fetchall()
	result_list_length = len(procuring_entitytendermap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entitytendermap(key_column, procuring_entity_id, tender_id))
		database_connection_object.commit()