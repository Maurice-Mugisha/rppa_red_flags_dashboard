
def insert_awardsubmissionmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, award_id, submission_id):

	query_executor.execute(selection_object.select_awardsubmissionmap(key_column, award_id, submission_id))
	awardsubmissionmap_check_query_result = query_executor.fetchall()
	result_list_length = len(awardsubmissionmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_awardsubmissionmap(key_column, award_id, submission_id))
		database_connection_object.commit()