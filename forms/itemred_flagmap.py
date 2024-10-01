
def insert_itemred_flagmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, item_id, red_flag_id):

	query_executor.execute(selection_object.select_itemred_flagmap(key_column, item_id, red_flag_id))
	itemred_flagmap_check_query_result = query_executor.fetchall()
	result_list_length = len(itemred_flagmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_itemred_flagmap(key_column, item_id, red_flag_id))
		database_connection_object.commit()