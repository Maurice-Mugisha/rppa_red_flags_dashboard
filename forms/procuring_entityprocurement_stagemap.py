
def insert_procuring_entityprocurement_stagemap(database_connection_object, query_executor, selection_object, insertion_object, key_column, procuring_entity_id, procurement_stage_id):

	query_executor.execute(selection_object.select_procuring_entityprocurement_stagemap(key_column, procuring_entity_id, procurement_stage_id))
	procuring_entityprocurement_stagemap_check_query_result = query_executor.fetchall()
	result_list_length = len(procuring_entityprocurement_stagemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entityprocurement_stagemap(key_column, procuring_entity_id, procurement_stage_id))
		database_connection_object.commit()