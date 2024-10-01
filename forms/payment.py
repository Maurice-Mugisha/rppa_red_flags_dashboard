
def insert_payment(database_connection_object, query_executor, selection_object, insertion_object, payment_id, transaction_id, date_received, amount, currency, status, extra_information):

	query_executor.execute(selection_object.select_payment(payment_id))
	payment_check_query_result = query_executor.fetchall()
	result_list_length = len(payment_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_payment(payment_id))
		database_connection_object.commit()

	if len(str(transaction_id).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_payment_transaction_id(payment_id, transaction_id))
		database_connection_object.commit()


	if len(str(date_received).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_payment_date_received(payment_id, date_received))
		database_connection_object.commit()


	if len(str(amount).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_payment_amount(payment_id, amount))
		database_connection_object.commit()


	if len(str(currency).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_payment_currency(payment_id, currency))
		database_connection_object.commit()


	if len(str(status).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_payment_status(payment_id, status))
		database_connection_object.commit()


	if len(str(extra_information).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_payment_extra_information(payment_id, extra_information))
		database_connection_object.commit()
