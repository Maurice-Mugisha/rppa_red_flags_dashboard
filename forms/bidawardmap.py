
def insert_bidawardmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, bid_id, award_id):

	query_executor.execute(selection_object.select_bidawardmap(key_column, bid_id, award_id))
	bidawardmap_check_query_result = query_executor.fetchall()
	result_list_length = len(bidawardmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_bidawardmap(key_column, bid_id, award_id))
		database_connection_object.commit()