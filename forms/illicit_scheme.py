
def insert_illicit_scheme(database_connection_object, query_executor, selection_object, insertion_object, illicit_scheme_id, name, description):

	query_executor.execute(selection_object.select_illicit_scheme(illicit_scheme_id))
	illicit_scheme_check_query_result = query_executor.fetchall()
	result_list_length = len(illicit_scheme_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_illicit_scheme(illicit_scheme_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_illicit_scheme_name(illicit_scheme_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_illicit_scheme_description(illicit_scheme_id, description))
		database_connection_object.commit()
