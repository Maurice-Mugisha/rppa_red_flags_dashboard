
def insert_plansubmissionmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, plan_id, submission_id):

	query_executor.execute(selection_object.select_plansubmissionmap(key_column, plan_id, submission_id))
	plansubmissionmap_check_query_result = query_executor.fetchall()
	result_list_length = len(plansubmissionmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_plansubmissionmap(key_column, plan_id, submission_id))
		database_connection_object.commit()