
def insert_userplanmap(query_executor, selection_object, insertion_object, key_column, user_id, plan_id):

	query_executor.execute(selection_object.select_userplanmap(key_column, user_id, plan_id))
	userplanmap_check_query_result = query_executor.fetchall()
	result_list_length = len(userplanmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_userplanmap(key_column, user_id, plan_id))
		database_connection_object.commit()