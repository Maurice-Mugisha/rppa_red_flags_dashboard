
def insert_fiscal_year(database_connection_object, query_executor, selection_object, insertion_object, fiscal_year_id, start_date, end_date):

	query_executor.execute(selection_object.select_fiscal_year(fiscal_year_id))
	fiscal_year_check_query_result = query_executor.fetchall()
	result_list_length = len(fiscal_year_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_fiscal_year(fiscal_year_id))
		database_connection_object.commit()

	if len(str(start_date).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_fiscal_year_start_date(fiscal_year_id, start_date))
		database_connection_object.commit()


	if len(str(end_date).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_fiscal_year_end_date(fiscal_year_id, end_date))
		database_connection_object.commit()
