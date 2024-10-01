
def insert_procurement_method(database_connection_object, query_executor, selection_object, insertion_object, procurement_method_id, code, name, description):

	query_executor.execute(selection_object.select_procurement_method(procurement_method_id))
	procurement_method_check_query_result = query_executor.fetchall()
	result_list_length = len(procurement_method_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_method(procurement_method_id))
		database_connection_object.commit()

	if len(str(code).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_method_code(procurement_method_id, code))
		database_connection_object.commit()


	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_method_name(procurement_method_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_method_description(procurement_method_id, description))
		database_connection_object.commit()
