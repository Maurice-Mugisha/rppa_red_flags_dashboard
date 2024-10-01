
def insert_supplying_entityusermap(query_executor, selection_object, insertion_object, key_column, supplying_entity_id, user_id):

	query_executor.execute(selection_object.select_supplying_entityusermap(key_column, supplying_entity_id, user_id))
	supplying_entityusermap_check_query_result = query_executor.fetchall()
	result_list_length = len(supplying_entityusermap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entityusermap(key_column, supplying_entity_id, user_id))
		database_connection_object.commit()