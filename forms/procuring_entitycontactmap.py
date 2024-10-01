
def insert_procuring_entitycontactmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, procuring_entity_id, contact_id):

	query_executor.execute(selection_object.select_procuring_entitycontactmap(key_column, procuring_entity_id, contact_id))
	procuring_entitycontactmap_check_query_result = query_executor.fetchall()
	result_list_length = len(procuring_entitycontactmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entitycontactmap(key_column, procuring_entity_id, contact_id))
		database_connection_object.commit()