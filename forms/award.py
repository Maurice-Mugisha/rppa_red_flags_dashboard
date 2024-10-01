
def insert_award(database_connection_object, query_executor, selection_object, insertion_object, award_id, is_accepted, date_replied, reply_reason, award_amount):

	query_executor.execute(selection_object.select_award(award_id))
	award_check_query_result = query_executor.fetchall()
	result_list_length = len(award_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_award(award_id))
		database_connection_object.commit()

	if len(str(is_accepted).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_award_is_accepted(award_id, is_accepted))
		database_connection_object.commit()


	if len(str(date_replied).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_award_date_replied(award_id, date_replied))
		database_connection_object.commit()


	if len(str(reply_reason).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_award_reply_reason(award_id, reply_reason))
		database_connection_object.commit()


	if len(str(award_amount).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_award_award_amount(award_id, award_amount))
		database_connection_object.commit()
