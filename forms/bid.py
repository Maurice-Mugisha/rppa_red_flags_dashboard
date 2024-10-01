
def insert_bid(database_connection_object, query_executor, selection_object, insertion_object, bid_id, submission_date, amount, extra_information):

	query_executor.execute(selection_object.select_bid(bid_id))
	bid_check_query_result = query_executor.fetchall()
	result_list_length = len(bid_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_bid(bid_id))
		database_connection_object.commit()

	if len(str(submission_date).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_bid_submission_date(bid_id, submission_date))
		database_connection_object.commit()


	if len(str(amount).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_bid_amount(bid_id, amount))
		database_connection_object.commit()


	if len(str(extra_information).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_bid_extra_information(bid_id, extra_information))
		database_connection_object.commit()
