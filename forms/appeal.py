
def insert_appeal(database_connection_object, query_executor, selection_object, insertion_object, appeal_id, subject, description):

	query_executor.execute(selection_object.select_appeal(appeal_id))
	appeal_check_query_result = query_executor.fetchall()
	result_list_length = len(appeal_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_appeal(appeal_id))
		database_connection_object.commit()

	if len(str(subject).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_appeal_subject(appeal_id, subject))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_appeal_description(appeal_id, description))
		database_connection_object.commit()
