
def insert_submission(database_connection_object, query_executor, selection_object, insertion_object, submission_id, name, description, reception_date_and_time, cut_off_date_and_time):

	query_executor.execute(selection_object.select_submission(submission_id))
	submission_check_query_result = query_executor.fetchall()
	result_list_length = len(submission_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_submission(submission_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_submission_name(submission_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_submission_description(submission_id, description))
		database_connection_object.commit()


	if len(str(reception_date_and_time).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_submission_reception_date_and_time(submission_id, reception_date_and_time))
		database_connection_object.commit()


	if len(str(cut_off_date_and_time).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_submission_cut_off_date_and_time(submission_id, cut_off_date_and_time))
		database_connection_object.commit()
