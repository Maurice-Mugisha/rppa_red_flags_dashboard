
def insert_feefee_typemap(query_executor, selection_object,  insertion_object, key_column, fee_id, fee_type_id):

	query_executor.execute(selection_object.select_feefee_typemap(key_column, fee_id, fee_type_id))
	feefee_typemap_check_query_result = query_executor.fetchall()
	result_list_length = len(feefee_typemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_feefee_typemap(key_column, fee_id, fee_type_id))
		database_connection_object.commit()