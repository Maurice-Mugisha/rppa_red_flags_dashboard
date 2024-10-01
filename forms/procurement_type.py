
def insert_procurement_type(database_connection_object, query_executor, selection_object, insertion_object, procurement_type_id, code, name, description):

	query_executor.execute(selection_object.select_procurement_type(procurement_type_id))
	procurement_type_check_query_result = query_executor.fetchall()
	result_list_length = len(procurement_type_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_type(procurement_type_id))
		database_connection_object.commit()

	if len(str(code).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_type_code(procurement_type_id, code))
		database_connection_object.commit()


	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_type_name(procurement_type_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_type_description(procurement_type_id, description))
		database_connection_object.commit()
