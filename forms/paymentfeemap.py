
def insert_paymentfeemap(database_connection_object, query_executor, selection_object, insertion_object, key_column, payment_id, fee_id):

	query_executor.execute(selection_object.select_paymentfeemap(key_column, payment_id, fee_id))
	paymentfeemap_check_query_result = query_executor.fetchall()
	result_list_length = len(paymentfeemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_paymentfeemap(key_column, payment_id, fee_id))
		database_connection_object.commit()