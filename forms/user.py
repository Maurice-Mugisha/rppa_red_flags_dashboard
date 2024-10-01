
def insert_user(query_executor, selection_object, insertion_object, user_id, national_id_number, category, first_name, last_name, other_names, date_of_birth, gender, status, email, password, photo):

	query_executor.execute(selection_object.select_user(user_id))
	user_check_query_result = query_executor.fetchall()
	result_list_length = len(user_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_user(user_id))
		database_connection_object.commit()

	if len(str(national_id_number).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_national_id_number(user_id, national_id_number))
		database_connection_object.commit()


	if len(str(category).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_category(user_id, category))
		database_connection_object.commit()


	if len(str(first_name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_first_name(user_id, first_name))
		database_connection_object.commit()


	if len(str(last_name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_last_name(user_id, last_name))
		database_connection_object.commit()


	if len(str(other_names).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_other_names(user_id, other_names))
		database_connection_object.commit()


	if len(str(date_of_birth).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_date_of_birth(user_id, date_of_birth))
		database_connection_object.commit()


	if len(str(gender).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_gender(user_id, gender))
		database_connection_object.commit()


	if len(str(status).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_status(user_id, status))
		database_connection_object.commit()


	if len(str(email).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_email(user_id, email))
		database_connection_object.commit()


	if len(str(password).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_password(user_id, password))
		database_connection_object.commit()


	if len(str(photo).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_photo(user_id, photo))
		database_connection_object.commit()
