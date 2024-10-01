
def insert_attachment(database_connection_object, query_executor, selection_object, insertion_object, attachment_id, type, name, description, link):

	query_executor.execute(selection_object.select_attachment(attachment_id))
	attachment_check_query_result = query_executor.fetchall()
	result_list_length = len(attachment_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_attachment(attachment_id))
		database_connection_object.commit()

	if len(str(type).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_attachment_type(attachment_id, type))
		database_connection_object.commit()


	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_attachment_name(attachment_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_attachment_description(attachment_id, description))
		database_connection_object.commit()


	if len(str(link).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_attachment_link(attachment_id, link))
		database_connection_object.commit()
