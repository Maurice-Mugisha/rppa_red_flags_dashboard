
def insert_countryprocuring_entitymap(database_connection_object, query_executor, selection_object, insertion_object, key_column, country_id, procuring_entity_id):

	query_executor.execute(selection_object.select_countryprocuring_entitymap(key_column, country_id, procuring_entity_id))
	countryprocuring_entitymap_check_query_result = query_executor.fetchall()
	result_list_length = len(countryprocuring_entitymap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_countryprocuring_entitymap(key_column, country_id, procuring_entity_id))
		database_connection_object.commit()