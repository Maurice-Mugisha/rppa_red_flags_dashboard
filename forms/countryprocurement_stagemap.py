
def insert_countryprocurement_stagemap(database_connection_object, query_executor, selection_object, insertion_object, key_column, country_id, procurement_stage_id):

	query_executor.execute(selection_object.select_countryprocurement_stagemap(key_column, country_id, procurement_stage_id))
	countryprocurement_stagemap_check_query_result = query_executor.fetchall()
	result_list_length = len(countryprocurement_stagemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_countryprocurement_stagemap(key_column, country_id, procurement_stage_id))
		database_connection_object.commit()