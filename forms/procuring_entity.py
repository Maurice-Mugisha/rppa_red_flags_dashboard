
def insert_procuring_entity(database_connection_object, query_executor, selection_object, insertion_object, procuring_entity_id, name, tax_identifier, tax_identifier_value, registration_number, registration_date, status):

	query_executor.execute(selection_object.select_procuring_entity(procuring_entity_id))
	procuring_entity_check_query_result = query_executor.fetchall()
	result_list_length = len(procuring_entity_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entity(procuring_entity_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entity_name(procuring_entity_id, name))
		database_connection_object.commit()


	if len(str(tax_identifier).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entity_tax_identifier(procuring_entity_id, tax_identifier))
		database_connection_object.commit()


	if len(str(tax_identifier_value).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entity_tax_identifier_value(procuring_entity_id, tax_identifier_value))
		database_connection_object.commit()


	if len(str(registration_number).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entity_registration_number(procuring_entity_id, registration_number))
		database_connection_object.commit()


	if len(str(registration_date).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entity_registration_date(procuring_entity_id, registration_date))
		database_connection_object.commit()


	if len(str(status).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procuring_entity_status(procuring_entity_id, status))
		database_connection_object.commit()
