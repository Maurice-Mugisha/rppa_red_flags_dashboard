
def insert_awardappealmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, award_id, appeal_id):

	query_executor.execute(selection_object.select_awardappealmap(key_column, award_id, appeal_id))
	awardappealmap_check_query_result = query_executor.fetchall()
	result_list_length = len(awardappealmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_awardappealmap(key_column, award_id, appeal_id))
		database_connection_object.commit()