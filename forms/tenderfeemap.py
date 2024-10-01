
def insert_tenderfeemap(database_connection_object, query_executor, selection_object, insertion_object, key_column, tender_id, fee_id):

	query_executor.execute(selection_object.select_tenderfeemap(key_column, tender_id, fee_id))
	tenderfeemap_check_query_result = query_executor.fetchall()
	result_list_length = len(tenderfeemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_tenderfeemap(key_column, tender_id, fee_id))
		database_connection_object.commit()