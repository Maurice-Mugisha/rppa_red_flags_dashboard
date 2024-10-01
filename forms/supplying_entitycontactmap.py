
def insert_supplying_entitycontactmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, supplying_entity_id, contact_id):

	query_executor.execute(selection_object.select_supplying_entitycontactmap(key_column, supplying_entity_id, contact_id))
	supplying_entitycontactmap_check_query_result = query_executor.fetchall()
	result_list_length = len(supplying_entitycontactmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entitycontactmap(key_column, supplying_entity_id, contact_id))
		database_connection_object.commit()