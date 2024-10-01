
def insert_supplying_entity(database_connection_object, query_executor, selection_object, insertion_object, supplying_entity_id, name, tax_identifier, tax_identifier_value, registration_number, registration_date, status):

	query_executor.execute(selection_object.select_supplying_entity(supplying_entity_id))
	supplying_entity_check_query_result = query_executor.fetchall()
	result_list_length = len(supplying_entity_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entity(supplying_entity_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entity_name(supplying_entity_id, name))
		database_connection_object.commit()


	if len(str(tax_identifier).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entity_tax_identifier(supplying_entity_id, tax_identifier))
		database_connection_object.commit()


	if len(str(tax_identifier_value).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entity_tax_identifier_value(supplying_entity_id, tax_identifier_value))
		database_connection_object.commit()


	if len(str(registration_number).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entity_registration_number(supplying_entity_id, registration_number))
		database_connection_object.commit()


	if len(str(registration_date).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entity_registration_date(supplying_entity_id, registration_date))
		database_connection_object.commit()


	if len(str(status).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_supplying_entity_status(supplying_entity_id, status))
		database_connection_object.commit()
