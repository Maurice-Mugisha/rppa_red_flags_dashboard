
def insert_item(database_connection_object, query_executor, selection_object, insertion_object, item_id, code, name, unit_cost, description):

	query_executor.execute(selection_object.select_item(item_id))
	item_check_query_result = query_executor.fetchall()
	result_list_length = len(item_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_item(item_id))
		database_connection_object.commit()

	if len(str(code).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_item_code(item_id, code))
		database_connection_object.commit()


	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_item_name(item_id, name))
		database_connection_object.commit()


	if len(str(unit_cost).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_item_unit_cost(item_id, unit_cost))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_item_description(item_id, description))
		database_connection_object.commit()
