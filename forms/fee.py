
def insert_fee(database_connection_object, query_executor, selection_object, insertion_object, fee_id, name, amount, type):

	query_executor.execute(selection_object.select_fee(fee_id))
	fee_check_query_result = query_executor.fetchall()
	result_list_length = len(fee_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_fee(fee_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_fee_name(fee_id, name))
		database_connection_object.commit()


	if len(str(amount).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_fee_amount(fee_id, amount))
		database_connection_object.commit()


	if len(str(type).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_fee_type(fee_id, type))
		database_connection_object.commit()
