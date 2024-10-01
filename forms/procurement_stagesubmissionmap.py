
def insert_procurement_stagesubmissionmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, procurement_stage_id, submission_id):

	query_executor.execute(selection_object.select_procurement_stagesubmissionmap(key_column, procurement_stage_id, submission_id))
	procurement_stagesubmissionmap_check_query_result = query_executor.fetchall()
	result_list_length = len(procurement_stagesubmissionmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_stagesubmissionmap(key_column, procurement_stage_id, submission_id))
		database_connection_object.commit()