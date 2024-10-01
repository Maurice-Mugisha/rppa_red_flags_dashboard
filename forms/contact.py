
def insert_contact(database_connection_object, query_executor, selection_object, insertion_object, contact_id, name, value, status):

	query_executor.execute(selection_object.select_contact(contact_id))
	contact_check_query_result = query_executor.fetchall()
	result_list_length = len(contact_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_contact(contact_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_contact_name(contact_id, name))
		database_connection_object.commit()


	if len(str(value).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_contact_value(contact_id, value))
		database_connection_object.commit()


	if len(str(status).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_contact_status(contact_id, status))
		database_connection_object.commit()
