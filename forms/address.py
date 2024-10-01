
def insert_address(database_connection_object, query_executor, selection_object, insertion_object, address_id, country, address_line_1, address_line_2, address_line_3, address_line_4, address_line_5, address_line_6, address_line_7, address_line_8, address_line_9, x_coord, y_coord, status, description, short_form):

	query_executor.execute(selection_object.select_address(address_id))
	address_check_query_result = query_executor.fetchall()
	result_list_length = len(address_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_address(address_id))
		database_connection_object.commit()

	if len(str(country).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_country(address_id, country))
		database_connection_object.commit()


	if len(str(address_line_1).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_address_line_1(address_id, address_line_1))
		database_connection_object.commit()


	if len(str(address_line_2).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_address_line_2(address_id, address_line_2))
		database_connection_object.commit()


	if len(str(address_line_3).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_address_line_3(address_id, address_line_3))
		database_connection_object.commit()


	if len(str(address_line_4).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_address_line_4(address_id, address_line_4))
		database_connection_object.commit()


	if len(str(address_line_5).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_address_line_5(address_id, address_line_5))
		database_connection_object.commit()


	if len(str(address_line_6).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_address_line_6(address_id, address_line_6))
		database_connection_object.commit()


	if len(str(address_line_7).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_address_line_7(address_id, address_line_7))
		database_connection_object.commit()


	if len(str(address_line_8).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_address_line_8(address_id, address_line_8))
		database_connection_object.commit()


	if len(str(address_line_9).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_address_line_9(address_id, address_line_9))
		database_connection_object.commit()


	if len(str(x_coord).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_x_coord(address_id, x_coord))
		database_connection_object.commit()


	if len(str(y_coord).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_y_coord(address_id, y_coord))
		database_connection_object.commit()


	if len(str(status).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_status(address_id, status))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_description(address_id, description))
		database_connection_object.commit()


	if len(str(short_form).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_address_short_form(address_id, short_form))
		database_connection_object.commit()
