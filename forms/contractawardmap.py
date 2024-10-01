
def insert_contractawardmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, contract_id, award_id):

	query_executor.execute(selection_object.select_contractawardmap(key_column, contract_id, award_id))
	contractawardmap_check_query_result = query_executor.fetchall()
	result_list_length = len(contractawardmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_contractawardmap(key_column, contract_id, award_id))
		database_connection_object.commit()