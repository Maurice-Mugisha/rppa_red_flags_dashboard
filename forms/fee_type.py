
def insert_fee_type(query_executor, selection_object,  insertion_object, fee_type_id, code, name):

	query_executor.execute(selection_object.select_fee_type(fee_type_id))
	fee_type_check_query_result = query_executor.fetchall()
	result_list_length = len(fee_type_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_fee_type(fee_type_id))
		database_connection_object.commit()

	if len(str(code).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_fee_type_code(fee_type_id, code))
		database_connection_object.commit()


	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_fee_type_name(fee_type_id, name))
		database_connection_object.commit()
