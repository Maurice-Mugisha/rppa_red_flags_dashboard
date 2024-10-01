
def insert_awardtendermap(database_connection_object, query_executor, selection_object, insertion_object, key_column, award_id, tender_id):

	query_executor.execute(selection_object.select_awardtendermap(key_column, award_id, tender_id))
	awardtendermap_check_query_result = query_executor.fetchall()
	result_list_length = len(awardtendermap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_awardtendermap(key_column, award_id, tender_id))
		database_connection_object.commit()