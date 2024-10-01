
def insert_procurement_stage(database_connection_object, query_executor, selection_object, insertion_object, procurement_stage_id, name, description):

	query_executor.execute(selection_object.select_procurement_stage(procurement_stage_id))
	procurement_stage_check_query_result = query_executor.fetchall()
	result_list_length = len(procurement_stage_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_stage(procurement_stage_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_stage_name(procurement_stage_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_procurement_stage_description(procurement_stage_id, description))
		database_connection_object.commit()
