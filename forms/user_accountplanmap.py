
def insert_user_accountplanmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, user_account_id, plan_id):

	query_executor.execute(selection_object.select_user_accountplanmap(key_column, user_account_id, plan_id))
	user_accountplanmap_check_query_result = query_executor.fetchall()
	result_list_length = len(user_accountplanmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_accountplanmap(key_column, user_account_id, plan_id))
		database_connection_object.commit()