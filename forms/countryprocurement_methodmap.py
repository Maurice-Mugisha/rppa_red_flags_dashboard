
def insert_countryprocurement_methodmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, country_id, procurement_method_id):

	query_executor.execute(selection_object.select_countryprocurement_methodmap(key_column, country_id, procurement_method_id))
	countryprocurement_methodmap_check_query_result = query_executor.fetchall()
	result_list_length = len(countryprocurement_methodmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_countryprocurement_methodmap(key_column, country_id, procurement_method_id))
		database_connection_object.commit()