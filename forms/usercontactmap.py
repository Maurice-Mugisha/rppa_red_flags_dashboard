
def insert_usercontactmap(query_executor, selection_object, insertion_object, key_column, user_id, contact_id):

	query_executor.execute(selection_object.select_usercontactmap(key_column, user_id, contact_id))
	usercontactmap_check_query_result = query_executor.fetchall()
	result_list_length = len(usercontactmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_usercontactmap(key_column, user_id, contact_id))
		database_connection_object.commit()