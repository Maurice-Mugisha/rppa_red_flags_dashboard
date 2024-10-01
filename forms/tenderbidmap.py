
def insert_tenderbidmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, tender_id, bid_id):

	query_executor.execute(selection_object.select_tenderbidmap(key_column, tender_id, bid_id))
	tenderbidmap_check_query_result = query_executor.fetchall()
	result_list_length = len(tenderbidmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_tenderbidmap(key_column, tender_id, bid_id))
		database_connection_object.commit()