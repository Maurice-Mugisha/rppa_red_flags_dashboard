
def insert_plan(database_connection_object, query_executor, selection_object, insertion_object, plan_id, budget, submission_date_and_time, description):

	query_executor.execute(selection_object.select_plan(plan_id))
	plan_check_query_result = query_executor.fetchall()
	result_list_length = len(plan_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_plan(plan_id))
		database_connection_object.commit()

	if len(str(budget).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_plan_budget(plan_id, budget))
		database_connection_object.commit()


	if len(str(submission_date_and_time).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_plan_submission_date_and_time(plan_id, submission_date_and_time))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_plan_description(plan_id, description))
		database_connection_object.commit()
