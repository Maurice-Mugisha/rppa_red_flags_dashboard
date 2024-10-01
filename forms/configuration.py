
def insert_configuration(database_connection_object, query_executor, selection_object, insertion_object, configuration_id, name, description, value, status):

	query_executor.execute(selection_object.select_configuration(configuration_id))
	configuration_check_query_result = query_executor.fetchall()
	result_list_length = len(configuration_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_configuration(configuration_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_configuration_name(configuration_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_configuration_description(configuration_id, description))
		database_connection_object.commit()


	if len(str(value).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_configuration_value(configuration_id, value))
		database_connection_object.commit()


	if len(str(status).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_configuration_status(configuration_id, status))
		database_connection_object.commit()
