
def insert_fiscal_yearsupplying_entitymap(database_connection_object, query_executor, selection_object, insertion_object, key_column, fiscal_year_id, supplying_entity_id):

	query_executor.execute(selection_object.select_fiscal_yearsupplying_entitymap(key_column, fiscal_year_id, supplying_entity_id))
	fiscal_yearsupplying_entitymap_check_query_result = query_executor.fetchall()
	result_list_length = len(fiscal_yearsupplying_entitymap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_fiscal_yearsupplying_entitymap(key_column, fiscal_year_id, supplying_entity_id))
		database_connection_object.commit()