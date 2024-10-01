
def insert_red_flag(database_connection_object, query_executor, selection_object, insertion_object, red_flag_id, name, description, status):

	query_executor.execute(selection_object.select_red_flag(red_flag_id))
	red_flag_check_query_result = query_executor.fetchall()
	result_list_length = len(red_flag_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_red_flag(red_flag_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_red_flag_name(red_flag_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_red_flag_description(red_flag_id, description))
		database_connection_object.commit()


	if len(str(status).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_red_flag_status(red_flag_id, status))
		database_connection_object.commit()
