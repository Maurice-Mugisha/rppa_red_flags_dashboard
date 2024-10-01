
def insert_bidpaymentmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, bid_id, payment_id):

	query_executor.execute(selection_object.select_bidpaymentmap(key_column, bid_id, payment_id))
	bidpaymentmap_check_query_result = query_executor.fetchall()
	result_list_length = len(bidpaymentmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_bidpaymentmap(key_column, bid_id, payment_id))
		database_connection_object.commit()