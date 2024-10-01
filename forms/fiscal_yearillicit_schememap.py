
def insert_fiscal_yearillicit_schememap(database_connection_object, query_executor, selection_object, insertion_object, key_column, fiscal_year_id, illicit_scheme_id):

	query_executor.execute(selection_object.select_fiscal_yearillicit_schememap(key_column, fiscal_year_id, illicit_scheme_id))
	fiscal_yearillicit_schememap_check_query_result = query_executor.fetchall()
	result_list_length = len(fiscal_yearillicit_schememap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_fiscal_yearillicit_schememap(key_column, fiscal_year_id, illicit_scheme_id))
		database_connection_object.commit()