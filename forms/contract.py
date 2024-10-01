
def insert_contract(database_connection_object, query_executor, selection_object, insertion_object, contract_id, title, amount, status, description):

	query_executor.execute(selection_object.select_contract(contract_id))
	contract_check_query_result = query_executor.fetchall()
	result_list_length = len(contract_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_contract(contract_id))
		database_connection_object.commit()

	if len(str(title).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_contract_title(contract_id, title))
		database_connection_object.commit()


	if len(str(amount).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_contract_amount(contract_id, amount))
		database_connection_object.commit()


	if len(str(status).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_contract_status(contract_id, status))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_contract_description(contract_id, description))
		database_connection_object.commit()
