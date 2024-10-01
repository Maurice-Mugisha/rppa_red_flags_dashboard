
def insert_countrysupplying_entitymap(database_connection_object, query_executor, selection_object, insertion_object, key_column, country_id, supplying_entity_id):

	query_executor.execute(selection_object.select_countrysupplying_entitymap(key_column, country_id, supplying_entity_id))
	countrysupplying_entitymap_check_query_result = query_executor.fetchall()
	result_list_length = len(countrysupplying_entitymap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_countrysupplying_entitymap(key_column, country_id, supplying_entity_id))
		database_connection_object.commit()