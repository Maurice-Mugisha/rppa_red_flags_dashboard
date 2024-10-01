
def insert_tender(database_connection_object, query_executor, selection_object, insertion_object, tender_id, title, description, budget, status, evaluate_mechanism, publication_date_and_time, submission_cut_off_date_and_time, award_notice_date, contract_notice_date):

	query_executor.execute(selection_object.select_tender(tender_id))
	tender_check_query_result = query_executor.fetchall()
	result_list_length = len(tender_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_tender(tender_id))
		database_connection_object.commit()

	if len(str(title).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_tender_title(tender_id, title))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_tender_description(tender_id, description))
		database_connection_object.commit()


	if len(str(budget).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_tender_budget(tender_id, budget))
		database_connection_object.commit()


	if len(str(status).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_tender_status(tender_id, status))
		database_connection_object.commit()


	if len(str(evaluate_mechanism).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_tender_evaluate_mechanism(tender_id, evaluate_mechanism))
		database_connection_object.commit()


	if len(str(publication_date_and_time).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_tender_publication_date_and_time(tender_id, publication_date_and_time))
		database_connection_object.commit()


	if len(str(submission_cut_off_date_and_time).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_tender_submission_cut_off_date_and_time(tender_id, submission_cut_off_date_and_time))
		database_connection_object.commit()


	if len(str(award_notice_date).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_tender_award_notice_date(tender_id, award_notice_date))
		database_connection_object.commit()


	if len(str(contract_notice_date).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_tender_contract_notice_date(tender_id, contract_notice_date))
		database_connection_object.commit()
