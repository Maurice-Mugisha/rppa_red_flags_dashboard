
def insert_countryfiscal_yearmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, country_id, fiscal_year_id):

	query_executor.execute(selection_object.select_countryfiscal_yearmap(key_column, country_id, fiscal_year_id))
	countryfiscal_yearmap_check_query_result = query_executor.fetchall()
	result_list_length = len(countryfiscal_yearmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_countryfiscal_yearmap(key_column, country_id, fiscal_year_id))
		database_connection_object.commit()