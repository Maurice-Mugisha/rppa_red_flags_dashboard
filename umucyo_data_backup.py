################################################################################
#     Algorithm for incremental backup of data between two databases           #
################################################################################



#          PSEUDOCODE


# Consider two databases Dx and Dy and that a database is simply a set of tables
# Dx = {T1, T2, T3, ... , Tn} such that |Dx| = n, and Dy = {T1', T2', T3', ... , Tm'} such that |Dy| = m
# Dx is the source database and Dy is the destination database for incremental backup
# The tables sets for both Dx and Dy are such that they are not a result of derived entities, otherwise, Dx and Dy are supersets each of strong and derived entity tables
# For each and every table Ti' element of Dx, count the number of entries or rows and store the result in a dictionary {xh:xc} where xh is the table key calculated from its hashcode and xc is the table row count obtained from a query
# Every table in Dy can be mapped to one or more tables in Dx. The inverse is not explored in this algorithm simply because Dx is the source batabase and Dy is the destination database (source to sink)
# For each and every table Ty' element of Dy, count the number of entries or rows and store the result in a dictionary {yh:yc} where yh is the table key calculated from its hashcode and yc is the table row count obtained from a query
#    Let R = yc
#    for each table table Tx that maps to Ty, with a row count R = xc
#        if R = 0,
#             continue to the next table Ty+1
#        else if R = Q
#             the database tables have the same row count (row count is upto date and you need not to do anything except to check for DML operational updates)
#        else if R < Q
#             select all the table's entries according to its key set in some order, that is, ascending or descending order and select an entry at row number R + 1
#             Check if the selected key set already exists in the new database specifically in table Ty (lexicographic sorting due to alphanumeric keys does not maintain the intended order)
#             if the new key does not exist,
#                  insert the key and add all its corresponding fields to the target tables, for example, entities where this table has foreign keys (1:*)
#             else if the key already exists,
#                  check whether all the corresponding fields are there and equal, otherwise, add and/or update them.




#          SOURCE CODE


import os
import psycopg2
import psycopg2.extras
from forms.all_entity_insertions import *
from includes.idgenerator import *
from includes.business_logic_functions import *
from crud.ddl import *
from crud.insert import *
from crud.selection import *
from crud.update import *
from urllib.parse import quote
from includes.date_time import *




class Database:

    def __init__(self, name, table_set):
        self.name = name
        self.table_set = table_set

    def get_table_set(self):
        return self.table_set

    def add_table(self, table):
        self.table_set.add(table)




class Table:

    key_set = set()

    def __init__(self, name, column_list, crud_callback_dictionary):
        self.name = name
        self.column_list = column_list
        self.crud_callback_dictionary = crud_callback_dictionary

    def get_name(self):
        return self.name.lower()

    def get_column_list(self):
        self.column_list = column_list

    def add_column(self, column):
        if column.is_a_key_column() == True:
            self.key_set.add(column)
        self.column_list.append(column)
        return self

    def set_crud_callback_dictionary(self, crud_callback_dictionary):
        self.crud_callback_dictionary = crud_callback_dictionary

    def get_crud_callback_dictionary(self):
        return self.crud_callback_dictionary

    def set_tuple_building_callback_dictionary(self, tuple_building_callback_dictionary):
        self.tuple_building_callback_dictionary = tuple_building_callback_dictionary

    def get_tuple_building_callback_dictionary(self, mapped_table_name):
        return self.tuple_building_callback_dictionary[mapped_table_name]

    def get_comma_separated_key_string(self):
        key_list = list()
        for key_column in self.column_list:
            if key_column.is_a_key_column():
                key_list.append(key_column.get_name())
        comma_separated_key_string = "".join(key_list)
        return comma_separated_key_string




class Column:

    def __init__(self, name, is_numeric, is_a_key):
        self.name = name
        self.is_numeric = is_numeric
        self.is_a_key = is_a_key

    def get_name(self):
        return self.name.lower()

    def is_a_numeric_type(self):
        return self.is_numeric

    def is_a_key_column(self):
        return self.is_a_key




class QueryExecutor:

    def __init__(self, credentials_dictionary):
        self.database_name = credentials_dictionary['database']
        self.credentials_dictionary = credentials_dictionary

    def select_a_table_row(self, table_name, order_by, order, offset, limit):
        query_result_list = {}
        database_object = self.connect_to_the_database()
        database_cursor = database_object.cursor(cursor_factory = psycopg2.extras.DictCursor)
        sql_query = "SELECT * FROM " + table_name + " ORDER BY " + order_by + " OFFSET " + str(offset) + " LIMIT " + str(limit)
        database_cursor.execute(sql_query)
        query_result_list = database_cursor.fetchall()
        database_object.close()
        return query_result_list

    def get_table_entry_count(self, table_name):
        query_result_list = {}
        database_object = self.connect_to_the_database()
        database_cursor = database_object.cursor(cursor_factory = psycopg2.extras.DictCursor)
        sql_query = "SELECT COUNT(*) AS row_count FROM " + table_name + ";"
        database_cursor.execute(sql_query)
        query_result_list = database_cursor.fetchone()
        database_object.close()
        return query_result_list['row_count']

    def connect_to_the_database(self):
        database_name = self.credentials_dictionary['database']
        host_ip = self.credentials_dictionary['host']
        user_name = self.credentials_dictionary['user']
        user_password = self.credentials_dictionary['password']
        port_number = self.credentials_dictionary['port']
        database_object = psycopg2.connect(database=database_name, host=host_ip, user=user_name, password=user_password, port=port_number)
        return database_object

    def get_cursor(self):
        database_object = self.connect_to_the_database()
        database_cursor = database_object.cursor(cursor_factory = psycopg2.extras.DictCursor)
        return database_cursor




class FieldSanitizer:

    def __init__(self):
        self.field = None

    def sanitize_date(self, field):
        self.field = field
        if str(field).isalnum() == False or str(field) == None:
            field = ""
        if isinstance(field, str) == False:
            field = " "
        if len(field) < 8:
            field = "1970-01-01 00:00:00"
        return field

    def sanitize_string_field(self, field):
        self.field = field
        if str(field).isalnum() == False or str(field) == None:
            field = ""
        if isinstance(field, str) == False:
            field = " "
        if len(field) < 1:
            field = ""
        quote_index = field.find("'")
        if quote_index > -1:
            field = quote(field)
        return field

    def sanitize_year(self, year):
        if len(str(year)) <= 3:
            year = "1970"
        if str(year).isalpha():
            year = "1970"
        if int(year) < 1970:
            year = "1970"
        if len(str(year)) == 8:
            year = int(str(year)[-4:])
        return str(year)

    def numeric_to_string(self, field):
        return str(field)




#########################################################
# All relavant callback functions for all source tables #
#########################################################


# Party table contains both the procuring and supplying entities.
# The supplying entity also has a TIN number which can be used to reference the different supplying entities in the umucyo public procurement system specifically in the
# Bidder, Award, and Contract tables
# The planning table contains the fiscal year information in a correspondingly named field. The same field can be found in the tender, award, and contract tables  



def plan_tuple_maker(query_executor, selection_object, id_generator_object, date_and_time_object, field_sanitizer, row_dictionary):
    plan_related_tuple_dictionary = {}
    plan_related_tuple_dictionary['ordered_key_list'] = list()

    plan_id = field_sanitizer.numeric_to_string(row_dictionary['id'])
    procuring_entity_name = field_sanitizer.sanitize_string_field(row_dictionary['entity'])
    year = field_sanitizer.sanitize_year(row_dictionary['year'])
    budget = row_dictionary['budget']
    total = row_dictionary['total']
    user_id = field_sanitizer.numeric_to_string(row_dictionary['f_account'])
    description = field_sanitizer.sanitize_string_field(row_dictionary['description'])
    submission_date_and_time = field_sanitizer.sanitize_string_field(row_dictionary['submitted_at'])
    file_name = field_sanitizer.sanitize_string_field(row_dictionary['file_name'])

    fiscal_year_id = id_generator_object.generate_fiscal_year_id()
    start_month_and_day = "01-01"
    end_month_and_day = "12-31"
    fiscal_year_start_date = year + "-" + start_month_and_day
    fiscal_year_end_date = year + "-" + end_month_and_day

    key_column = date_and_time_object.get_date_and_time()

    plan_related_tuple_dictionary['plan'] = (plan_id, budget, submission_date_and_time, description)
    plan_related_tuple_dictionary['ordered_key_list'].append('plan')
    plan_related_tuple_dictionary['fiscal_year'] = (fiscal_year_id, start_date, end_date)
    plan_related_tuple_dictionary['ordered_key_list'].append('fiscal_year')
    plan_related_tuple_dictionary['fiscal_yearplanmap'] = (key_column, fiscal_year_id, plan_id)
    plan_related_tuple_dictionary['ordered_key_list'].append('fiscal_yearplanmap')
    plan_related_tuple_dictionary['user_accountplanmap'] = (key_column, user_id, plan_id)
    plan_related_tuple_dictionary['ordered_key_list'].append('user_accountplanmap')
    plan_related_tuple_dictionary['procuring_entityplanmap'] = (key_column, procuring_entity_id, plan_id)
    plan_related_tuple_dictionary['ordered_key_list'].append('procuring_entityplanmap')

    return plan_related_tuple_dictionary



def entity_tuple_maker(query_executor, selection_object, id_generator_object, date_and_time_object, field_sanitizer, row_dictionary):

    entity_related_tuple_dictionary = {}
    entity_related_tuple_dictionary['ordered_key_list'] = list()

    entity_registration_date = field_sanitizer.sanitize_date(row_dictionary['year_company_reg'])
    entity_id = field_sanitizer.numeric_to_string(row_dictionary['id'])
    entity_type = field_sanitizer.sanitize_date(row_dictionary['type_auth'])
    name = field_sanitizer.sanitize_string_field(row_dictionary['name_auth'])
    tax_identifier = "TPIN"
    tax_identifier_value = field_sanitizer.sanitize_string_field(row_dictionary['taxation_id'])
    registration_number = field_sanitizer.sanitize_string_field(row_dictionary['registration_number'])
    registration_date = field_sanitizer.sanitize_date(row_dictionary['reg_date'])
    status = field_sanitizer.sanitize_string_field(row_dictionary['status'])

    if entity_type.lower().endswith("ca"):
        procuring_entity_id = entity_id
        entity_related_tuple_dictionary["procuring_entity"] = (procuring_entity_id, name, tax_identifier, tax_identifier_value, registration_number, registration_date, status)
        entity_related_tuple_dictionary['ordered_key_list'].append('procuring_entity')
        entity_related_tuple_dictionary["contact"] = list()
        entity_related_tuple_dictionary['ordered_key_list'].append('contact')
        entity_related_tuple_dictionary["address"] = list()
        entity_related_tuple_dictionary['ordered_key_list'].append('address')
        entity_related_tuple_dictionary["procuring_entitycontactmap"] = list()
        entity_related_tuple_dictionary['ordered_key_list'].append('procuring_entitycontactmap')
        entity_related_tuple_dictionary["procuring_entityaddressmap"] = list()
        entity_related_tuple_dictionary['ordered_key_list'].append('procuring_entityaddressmap')

    elif entity_type.lower().endswith("eo"):
        supplying_entity_id = entity_id
        entity_related_tuple_dictionary["supplying_entity"] = (supplying_entity_id, name, tax_identifier, tax_identifier_value, registration_number, registration_date, status)
        entity_related_tuple_dictionary['ordered_key_list'].append('supplying_entity')
        entity_related_tuple_dictionary["contact"] = list()
        entity_related_tuple_dictionary['ordered_key_list'].append('contact')
        entity_related_tuple_dictionary["address"] = list()
        entity_related_tuple_dictionary['ordered_key_list'].append('address')
        entity_related_tuple_dictionary["supplying_entitycontactmap"] = list()
        entity_related_tuple_dictionary['ordered_key_list'].append('supplying_entitycontactmap')
        entity_related_tuple_dictionary["supplying_entityaddressmap"] = list()
        entity_related_tuple_dictionary['ordered_key_list'].append('supplying_entityaddressmap')

    contact_name_value_dictionary = {}
    contact_name_value_dictionary['email'] = field_sanitizer.sanitize_string_field(row_dictionary['email'])
    contact_name_value_dictionary['phone'] = field_sanitizer.sanitize_string_field(row_dictionary['phone'])
    contact_name_value_dictionary['fax'] = field_sanitizer.sanitize_string_field(row_dictionary['fax'])
    contact_name_value_dictionary['website'] = field_sanitizer.sanitize_string_field(row_dictionary['site'])

    for name in contact_name_value_dictionary:
        contact_id = id_generator_object.generate_contact_id()
        value = contact_name_value_dictionary[name]
        entity_related_tuple_dictionary["contact"].append((contact_id, name, value, status))

        key_column = date_and_time_object.get_date_and_time()
        if entity_type.lower().endswith("ca"):
            procuring_entity_id = entity_id
            entity_related_tuple_dictionary["procuring_entitycontactmap"].append((key_column, procuring_entity_id, contact_id))

        elif entity_type.lower().endswith("eo"):
            supplying_entity_id = entity_id
            entity_related_tuple_dictionary["supplying_entitycontactmap"].append((key_column, supplying_entity_id, contact_id))

    address_id = id_generator_object.generate_address_id()
    country = ""
    address_line_1 = ""
    address_line_2 = ""
    address_line_3 = ""
    address_line_4 = ""
    address_line_5 = ""
    address_line_6 = ""
    address_line_7 = ""
    address_line_8 = ""
    address_line_9 = ""
    x_coord = ""
    y_coord = ""
    status = ""
    short_form = field_sanitizer.numeric_to_string(row_dictionary['address'])
    description = field_sanitizer.numeric_to_string(row_dictionary['city'])

    key_column = date_and_time_object.get_date_and_time()
    if entity_type.lower().endswith("ca"):
        procuring_entity_id = entity_id
        entity_related_tuple_dictionary["procuring_entityaddressmap"].append((key_column, procuring_entity_id, address_id))

    elif entity_type.lower().endswith("eo"):
        supplying_entity_id = entity_id
        entity_related_tuple_dictionary["supplying_entityaddressmap"].append((key_column, supplying_entity_id, address_id))

    return entity_related_tuple_dictionary





def user_account_tuple_maker(query_executor, selection_object, id_generator_object, date_and_time_object, field_sanitizer, row_dictionary):
    user_account_related_tuple_dictionary = {}
    user_account_related_tuple_dictionary['ordered_key_list'] = list()

    user_account_id = field_sanitizer.numeric_to_string(row_dictionary['f_principal'])
    procurement_actor_id = field_sanitizer.numeric_to_string(row_dictionary['f_authority'])
    first_name = field_sanitizer.sanitize_string_field(row_dictionary['firstname'])
    last_name = field_sanitizer.sanitize_string_field(row_dictionary['lastname'])
    other_names = ""
    date_of_birth = ""
    gender = " "
    national_id = field_sanitizer.sanitize_string_field(row_dictionary['national_id'])
    status = field_sanitizer.numeric_to_string(row_dictionary['status'])
    registration_date = field_sanitizer.sanitize_date(row_dictionary['registration_date'])
    category = field_sanitizer.sanitize_string_field(row_dictionary['user_type'])
    password = field_sanitizer.sanitize_string_field(row_dictionary['passwd'])
    photo = ""

    email = field_sanitizer.sanitize_string_field(row_dictionary['email'])
    phone = field_sanitizer.numeric_to_string(row_dictionary['phone'])
    category = field_sanitizer.sanitize_string_field(row_dictionary['user_type'])

    user_account_related_tuple_dictionary["user_account"] = (user_account_id, national_id_number, category, first_name, last_name, other_names, date_of_birth, gender[:12], status, email, password, photo)
    user_account_related_tuple_dictionary['ordered_key_list'].append('user_account')
    user_account_related_tuple_dictionary["contact"] = list()
    user_account_related_tuple_dictionary['ordered_key_list'].append('contact')
    user_account_related_tuple_dictionary["address"] = list()
    user_account_related_tuple_dictionary['ordered_key_list'].append('address')
    user_account_related_tuple_dictionary["user_accountcontactmap"] = list()
    user_account_related_tuple_dictionary['ordered_key_list'].append('user_accountcontactmap')
    user_account_related_tuple_dictionary["user_accountaddressmap"] = list()
    user_account_related_tuple_dictionary['ordered_key_list'].append('user_accountaddressmap')

    contact_name_value_dictionary = {}
    contact_name_value_dictionary['email'] = field_sanitizer.sanitize_string_field(row_dictionary['email'])
    contact_name_value_dictionary['phone'] = field_sanitizer.numeric_to_string(row_dictionary['phone'])
    key_column = date_and_time_object.get_date_and_time()

    for name in contact_name_value_dictionary:
        contact_id = id_generator_object.generate_contact_id()
        value = contact_name_value_dictionary[name]
        user_account_related_tuple_dictionary["contact"].append((contact_id, name, value, status))
        user_account_related_tuple_dictionary["user_accountcontactmap"].append((key_column, user_account_id, contact_id))

    address_id = id_generator_object.generate_address_id()
    country = ""
    address_line_1 = ""
    address_line_2 = ""
    address_line_3 = ""
    address_line_4 = ""
    address_line_5 = ""
    address_line_6 = ""
    address_line_7 = ""
    address_line_8 = ""
    address_line_9 = ""
    x_coord = ""
    y_coord = ""
    status = ""
    description = field_sanitizer.sanitize_string_field(row_dictionary['city'])
    short_form = field_sanitizer.sanitize_string_field(row_dictionary['address'])

    user_account_related_tuple_dictionary["address"].append((address_id, country, address_line_1, address_line_2, address_line_3, address_line_4, address_line_5, address_line_6, address_line_7, address_line_8, address_line_9, x_coord, y_coord, status, description, short_form))
    user_account_related_tuple_dictionary["user_accountaddressmap"].append((key_column, user_id, address_id))

    return user_account_related_tuple_dictionary



def tender_tuple_maker(query_executor, selection_object, fiscal_year_dictionary, id_generator_object, date_and_time_object, field_sanitizer, row_dictionary):
    tender_related_tuple_dictionary = {}
    tender_related_tuple_dictionary['ordered_key_list'] = list()

    tender_id = field_sanitizer.numeric_to_string(row_dictionary['id'])
    procuring_entity_name = field_sanitizer.sanitize_string_field(row_dictionary['ca_name'])
    contracting_agency_name = procuring_entity_name
    call_for_tender_number = field_sanitizer.numeric_to_string(row_dictionary['ca_unique_cft_number'])
    title = field_sanitizer.sanitize_string_field(row_dictionary['title'])
    description = field_sanitizer.sanitize_string_field(row_dictionary['abstract'])
    budget = row_dictionary['estimated_value']
    publication_date_and_time = field_sanitizer.sanitize_date(row_dictionary['date_published'])
    submission_cut_off_date_and_time = field_sanitizer.sanitize_date(row_dictionary['tendersubmissiondeadline'])
    evaluate_mechanism = field_sanitizer.sanitize_string_field(row_dictionary['evaluate_mechanism'])
    status = field_sanitizer.sanitize_string_field(row_dictionary['status'])
    award_notice_date = field_sanitizer.sanitize_date(row_dictionary['award_notice_date'])
    contract_notice_date = field_sanitizer.sanitize_date(row_dictionary['contract_notice_date'])
    key_column = date_and_time_object.get_date_and_time()

    fiscal_year_id = ""
    for fiscal_year_key in fiscal_year_dictionary:
        start_date = fiscal_year_dictionary[fiscal_year_key]
        start_year = int(start_date[:4])
        publication_year = int(publication_date_and_time[:4])
        if publication_year == start_year:
            fiscal_year_id = fiscal_year_key
            break

    procuring_entity_id = ""
    procuring_entity_dictionary = get_procuring_entities(selection_object, query_executor)
    for procuring_entity_key in procuring_entity_dictionary:
        procuring_entity_name = procuring_entity_dictionary[procuring_entity_key]
        if procuring_entity_name == contracting_agency_name:
            procuring_entity_id = procuring_entity_key
            break

    tender_related_tuple_dictionary["tender"] = (tender_id, title, description, budget, status, evaluate_mechanism, publication_date_and_time, submission_cut_off_date_and_time, award_notice_date, contract_notice_date)
    tender_related_tuple_dictionary['ordered_key_list'].append('tender')
    tender_related_tuple_dictionary["procuring_entitytendermap"] = list()
    tender_related_tuple_dictionary['ordered_key_list'].append('procuring_entitytendermap')
    tender_related_tuple_dictionary["fiscal_yeartendermap"] = list()
    tender_related_tuple_dictionary['ordered_key_list'].append('fiscal_yeartendermap')
    tender_related_tuple_dictionary["procuring_entitytendermap"].append((key_column, procuring_entity_id, tender_id))
    tender_related_tuple_dictionary['ordered_key_list'].append('procuring_entitytendermap')

    if len(fiscal_year_id) > 0:
        tender_related_tuple_dictionary["fiscal_yeartendermap"].append((key_column, fiscal_year_id, tender_id))

    return tender_related_tuple_dictionary



def payment_tuple_maker(query_executor, selection_object, id_generator_object, date_and_time_object, field_sanitizer, row_dictionary):
    payment_related_tuple_dictionary = {}
    payment_related_tuple_dictionary['ordered_key_list'] = list()

    payment_id = field_sanitizer.numeric_to_string(row_dictionary['id'])
    transaction_id = field_sanitizer.sanitize_string_field(row_dictionary['transaction_id'])
    date_received = field_sanitizer.sanitize_date(row_dictionary['date_and_time'])
    amount = field_sanitizer.sanitize_string_field(row_dictionary['amount'])
    currency = field_sanitizer.sanitize_string_field(row_dictionary['currency'])
    date_and_time = field_sanitizer.sanitize_date(row_dictionary['timestamp'])
    status = field_sanitizer.sanitize_string_field(row_dictionary['status'])
    type = field_sanitizer.sanitize_string_field(row_dictionary['kind'])
    extra_information = field_sanitizer.sanitize_string_field(row_dictionary['kind'])
    key_column = date_and_time_object.get_date_and_time()
    supplying_entity_id = field_sanitizer.sanitize_string_field(row_dictionary['f_authority'])
    tender_id = field_sanitizer.sanitize_string_field(row_dictionary['f_resource'])
    fee_id = ""
    bid_id = id_generator_object.generate_bid_id()
    submission_date = field_sanitizer.sanitize_date(date_and_time)

    fee_dictionary = get_fees(selection_object, query_executor)
    for fee_key in fee_dictionary:
        fee_type = fee_dictionary[fee_key]["type"]
        if type.lower() == fee_type.lower():
            fee_id = fee_key
            break

    if len(fee_id) == 0:
        fee_id = id_generator_object.generate_fee_id()
        name = type
        payment_related_tuple_dictionary["fee"] = (fee_id, name, amount, type)
        payment_related_tuple_dictionary['ordered_key_list'].append('fee')


    amount = 0 # no bid amounts are given for every tender
    extra_information = ""
    if type.strip().lower().endswith("tender"):
        payment_related_tuple_dictionary["payment"] = (payment_id, transaction_id, date_received, amount, currency, status, extra_information)
        payment_related_tuple_dictionary['ordered_key_list'].append('payment')

        payment_related_tuple_dictionary["supplying_entitypaymentmap"] = (key_column, supplying_entity_id, payment_id)
        payment_related_tuple_dictionary['ordered_key_list'].append('supplying_entitypaymentmap')
        payment_related_tuple_dictionary["bid"] = (bid_id, submission_date, amount, extra_information)
        payment_related_tuple_dictionary['ordered_key_list'].append('bid')
        payment_related_tuple_dictionary["tenderbidmap"] = (key_column, tender_id, bid_id)
        payment_related_tuple_dictionary['ordered_key_list'].append('tenderbidmap')
        payment_related_tuple_dictionary["tenderfeemap"] = (key_column, tender_id, fee_id)
        payment_related_tuple_dictionary['ordered_key_list'].append('tenderfeemap')
        payment_related_tuple_dictionary["tenderpaymentmap"] = (key_column, tender_id, payment_id)
        payment_related_tuple_dictionary['ordered_key_list'].append('tenderpaymentmap')
        payment_related_tuple_dictionary["bidpaymentmap"] = (key_column, bid_id, payment_id)
        payment_related_tuple_dictionary['ordered_key_list'].append('bidpaymentmap')
        payment_related_tuple_dictionary["bidfeemap"] = (key_column, bid_id, fee_id)
        payment_related_tuple_dictionary['ordered_key_list'].append('bidfeemap')

    if type.strip().lower().endswith("appeal") and len(tender_id.strip().lower()) > 0:
        appeal_id = id_generator_object.generate_appeal_id()
        subject = ""
        description = ""
        payment_related_tuple_dictionary["appeal"] = (appeal_id, subject, description)
        payment_related_tuple_dictionary['ordered_key_list'].append('appeal')
        payment_related_tuple_dictionary["tenderappealmap"] = list()
        payment_related_tuple_dictionary['ordered_key_list'].append('tenderappealmap')
        payment_related_tuple_dictionary["tenderappealmap"].append((key_column, tender_id, appeal_id))
        payment_related_tuple_dictionary["paymentfeemap"] = list()
        payment_related_tuple_dictionary['ordered_key_list'].append('paymentfeemap')
        payment_related_tuple_dictionary["paymentfeemap"].append((key_column, payment_id, fee_id))
        payment_related_tuple_dictionary["supplying_entitybidmap"] = list()
        payment_related_tuple_dictionary['ordered_key_list'].append('supplying_entitybidmap')
        payment_related_tuple_dictionary["supplying_entitybidmap"].append((key_column, supplying_entity_id, bid_id))

    if type.strip().lower().endswith("tender"):
        payment_related_tuple_dictionary["supplying_entitytendermap"] = list()
        payment_related_tuple_dictionary['ordered_key_list'].append('supplying_entitytendermap')
        payment_related_tuple_dictionary["supplying_entitytendermap"].append((key_column, supplying_entity_id, tender_id))

    return payment_related_tuple_dictionary



def award_tuple_maker(query_executor, selection_object, id_generator_object, date_and_time_object, field_sanitizer, row_dictionary):
    award_related_tuple_dictionary = {}
    award_related_tuple_dictionary['ordered_key_list'] = list()

    award_id = field_sanitizer.numeric_to_string(row_dictionary['id'])
    is_accepted = field_sanitizer.sanitize_string_field(row_dictionary['is_accepted'])
    date_replied = field_sanitizer.sanitize_date(row_dictionary['date_replied'])
    reply_reason = field_sanitizer.sanitize_string_field(row_dictionary['reply_reason'])
    award_amount = row_dictionary['contract_value']
    supplying_entity_id = field_sanitizer.numeric_to_string(row_dictionary['eo_id'])
    tender_id = field_sanitizer.numeric_to_string(row_dictionary['cft_id'])

    contract_id = award_id
    contract_title = row_dictionary['contract_title']
    contract_description = row_dictionary['contract_description']

    tender_fiscal_year_dictionary = get_specific_tender_fiscal_years(selection_object, query_executor, tender_id)
    fiscal_year_id = ""

    for fiscal_year_key in tender_fiscal_year_dictionary:
        fiscal_year_id = fiscal_year_key
        break

    award_related_tuple_dictionary['award'] = (award_id, is_accepted, date_replied, reply_reason, award_amount)
    award_related_tuple_dictionary['ordered_key_list'].append('award')
    award_related_tuple_dictionary['supplying_entityawardmap'] = list()
    award_related_tuple_dictionary['supplying_entityawardmap'].append((key_column, supplying_entity_id, award_id))
    award_related_tuple_dictionary['ordered_key_list'].append('supplying_entityawardmap')
    if len(fiscal_year_id) > 0:
        award_related_tuple_dictionary['fiscal_yearawardmap'] = list()
        award_related_tuple_dictionary['fiscal_yearawardmap'].append((key_column, fiscal_year_id, award_id))
        award_related_tuple_dictionary['ordered_key_list'].append('fiscal_yearawardmap')
    award_related_tuple_dictionary['awardtendermap'] = list()
    award_related_tuple_dictionary['awardtendermap'].append((key_column, award_id, tender_id))
    award_related_tuple_dictionary['ordered_key_list'].append('fiscal_yeartendermap')
    award_related_tuple_dictionary['contract'] = (contract_id, title, amount, status, description)
    award_related_tuple_dictionary['ordered_key_list'].append('contract')
    award_related_tuple_dictionary['procuring_entityawardmap'] = list()
    award_related_tuple_dictionary['procuring_entityawardmap'].append((key_column, procuring_entity_id, award_id))
    award_related_tuple_dictionary['ordered_key_list'].append('procuring_entityawardmap')

    return award_related_tuple_dictionary



##########
#   End  #
##########




field_sanitizer = FieldSanitizer()
# Client continent
client_continent = "Africa"
# Client country name
client_country_name = "Zambia"
# Client capital city
client_capital_city = "Lusaka"
# Date and timezone relative to a particular country
timezone_string = client_continent + os.sep + client_capital_city

date_and_time_object = DateTimeProvider(timezone_string)
id_generator_object = IDGenerator(client_continent, client_capital_city)


# Source and sink database authentication credentials and connection objects
source_database_credentials_dictionary = {"database":"umucyo_backup", "host":"127.0.0.1", "user":"postgres", "password":"CGPA5.0class", "port":"5432"}
source_database_object = QueryExecutor(source_database_credentials_dictionary)
source_database_connection_object = source_database_object.connect_to_the_database()

sink_database_credentials_dictionary = {"database":"public_procurement", "host":"127.0.0.1", "user":"postgres", "password":"CGPA5.0class", "port":"5432"}
sink_database_object = QueryExecutor(sink_database_credentials_dictionary)
sink_database_connection_object = sink_database_object.connect_to_the_database()

# Always change the source database instance but the sink database instance will always be the same
source_database = Database("umucyo_backup", set())

source_table_1 = Table(name="epps_authority", column_list=list(), crud_callback_dictionary={})
tuple_maker_callback_dictionary = {"procuring_entity": entity_tuple_maker, "supplying_entity": entity_tuple_maker}
source_table_1.set_tuple_building_callback_dictionary(tuple_maker_callback_dictionary)
srct_1_c1 = Column(name="id", is_numeric=True, is_a_key=True)
source_table_1.add_column(srct_1_c1)


source_table_2 = Table(name="epps_account", column_list=list(), crud_callback_dictionary={})
tuple_maker_callback_dictionary = {"user_account": user_account_tuple_maker}
source_table_2.set_tuple_building_callback_dictionary(tuple_maker_callback_dictionary)
srct_2_c1 = Column(name="f_authority", is_numeric=True, is_a_key=True)
source_table_2.add_column(srct_2_c1)

source_table_3 = Table(name="epps_plan_submission", column_list=list(), crud_callback_dictionary={})
tuple_maker_callback_dictionary = {"plan": plan_tuple_maker}
source_table_3.set_tuple_building_callback_dictionary(tuple_maker_callback_dictionary)
srct_3_c1 = Column(name="id", is_numeric=True, is_a_key=True)
source_table_1.add_column(srct_3_c1)

source_table_4 = Table(name="epps_call_for_tender", column_list=list(), crud_callback_dictionary={})
tuple_maker_callback_dictionary = {"tender": tender_tuple_maker}
source_table_4.set_tuple_building_callback_dictionary(tuple_maker_callback_dictionary)
srct_4_c1 = Column(name="id", is_numeric=True, is_a_key=True)
source_table_4.add_column(srct_4_c1)

source_table_5 = Table(name="epps_payment", column_list=list(), crud_callback_dictionary={})
tuple_maker_callback_dictionary = {"payment": payment_tuple_maker}
source_table_5.set_tuple_building_callback_dictionary(tuple_maker_callback_dictionary)
srct_5_c1 = Column(name="id", is_numeric=True, is_a_key=True)
source_table_5.add_column(srct_5_c1)

source_table_6 = Table(name="epps_eo_awarding", column_list=list(), crud_callback_dictionary={})
tuple_maker_callback_dictionary = {"award": award_tuple_maker}
source_table_6.set_tuple_building_callback_dictionary(tuple_maker_callback_dictionary)
srct_6_c1 = Column(name="id", is_numeric=True, is_a_key=True)
source_table_6.add_column(srct_6_c1)


# Adding tables to the source database
source_database.add_table(source_table_1)
source_database.add_table(source_table_2)
source_database.add_table(source_table_3)
source_database.add_table(source_table_4)
source_database.add_table(source_table_5)
source_database.add_table(source_table_6)


# The sink database will always be the same for the database red flags dashboard application and may not be the cause for modifications to this tool.
# Actually these tables may not be necessary right now
sink_database = Database("public procurement", set())
insertion_object = Insert("ZPPA insertion object 1")
selection_object = Select("ZPPA selection object 1")

callback_dictionary = {"insert":insert_fiscal_year, "select": get_specific_fiscal_year}
sink_table_1 = Table(name="Fiscal_year", column_list=list(), crud_callback_dictionary=callback_dictionary)
skt_1_c1 = Column(name="fiscal_year_id", is_numeric=False, is_a_key=True)
sink_table_1.add_column(skt_1_c1)

callback_dictionary = {"insert":insert_procuring_entity, "select": get_specific_procuring_entity}
sink_table_2 = Table(name="Procuring_entity", column_list=list(), crud_callback_dictionary=callback_dictionary)
skt_2_c1 = Column(name="procuring_entity_id", is_numeric=False, is_a_key=True)
sink_table_2.add_column(skt_2_c1)

callback_dictionary = {"insert":insert_supplying_entity, "select": get_specific_supplying_entity}
sink_table_3 = Table(name="Supplying_entity", column_list=list(), crud_callback_dictionary=callback_dictionary)
skt_3_c1 = Column(name="supplying_entity_id", is_numeric=False, is_a_key=True)
sink_table_3.add_column(skt_3_c1)

callback_dictionary = {"insert":insert_user_account, "select": get_specific_user_account}
sink_table_4 = Table(name="User_account", column_list=list(), crud_callback_dictionary=callback_dictionary)
skt_4_c1 = Column(name="user_account_id", is_numeric=False, is_a_key=True)
sink_table_4.add_column(skt_4_c1)

callback_dictionary = {"insert":insert_tender, "select": get_specific_tender}
sink_table_5 = Table(name="Tender", column_list=list(), crud_callback_dictionary=callback_dictionary)
skt_5_c1 = Column(name="tender_id", is_numeric=False, is_a_key=True)
sink_table_5.add_column(skt_5_c1)

callback_dictionary = {"insert":insert_bid, "select": get_specific_bid}
sink_table_6 = Table(name="Bid", column_list=list(), crud_callback_dictionary=callback_dictionary)
skt_6_c1 = Column(name="bid_id", is_numeric=False, is_a_key=True)
sink_table_6.add_column(skt_6_c1)

callback_dictionary = {"insert":insert_award, "select": get_specific_award}
sink_table_7 = Table(name="Award", column_list=list(), crud_callback_dictionary=callback_dictionary)
skt_7_c1 = Column(name="award_id", is_numeric=False, is_a_key=True)
sink_table_7.add_column(skt_7_c1)

callback_dictionary = {"insert":insert_payment, "select": get_specific_payment}
sink_table_8 = Table(name="Payment", column_list=list(), crud_callback_dictionary=callback_dictionary)
skt_8_c1 = Column(name="payment_id", is_numeric=False, is_a_key=True)
sink_table_8.add_column(skt_8_c1)

callback_dictionary = {"insert":insert_fee, "select": get_specific_fee}
sink_table_9 = Table(name="Fee", column_list=list(), crud_callback_dictionary=callback_dictionary)
skt_9_c1 = Column(name="fee_id", is_numeric=False, is_a_key=True)
sink_table_9.add_column(skt_9_c1)

callback_dictionary = {"insert":insert_contract, "select": get_specific_contract}
sink_table_10 = Table(name="Contract", column_list=list(), crud_callback_dictionary=callback_dictionary)
skt_10_c1 = Column(name="contract_id", is_numeric=False, is_a_key=True)
sink_table_10.add_column(skt_10_c1)

callback_dictionary = {"insert":insert_appeal, "select": get_specific_appeal}
sink_table_11 = Table(name="Appeal", column_list=list(), crud_callback_dictionary=callback_dictionary)
skt_11_c1 = Column(name="appeal_id", is_numeric=False, is_a_key=True)
sink_table_11.add_column(skt_11_c1)

callback_dictionary = {"insert":insert_plan, "select": get_specific_plan}
sink_table_12 = Table(name="Plan", column_list=list(), crud_callback_dictionary=callback_dictionary)
skt_12_c1 = Column(name="plan_id", is_numeric=False, is_a_key=True)
sink_table_12.add_column(skt_12_c1)


sink_database.add_table(sink_table_1)
sink_database.add_table(sink_table_2)
sink_database.add_table(sink_table_3)
sink_database.add_table(sink_table_4)
sink_database.add_table(sink_table_5)
sink_database.add_table(sink_table_6)
sink_database.add_table(sink_table_7)
sink_database.add_table(sink_table_8)
sink_database.add_table(sink_table_9)


# Create source-sink database table mappings. The key set and values must be changed for every backup instance
source_sink_table_mapping_dictionary = {
                                          source_table_1:[sink_table_2, sink_table_3],
                                          source_table_2:[sink_table_4],
                                          source_table_3:[sink_table_12],
                                          source_table_4:[sink_table_5],
                                          source_table_5:[sink_table_8],
                                          source_table_6:[sink_table_7, sink_table_10]
                                      }


mapping_sink_table_name_crud_callback_dictionary = {
                                                      "fiscal_year": insert_fiscal_year,
                                                      "plan": insert_plan,
                                                      "fiscal_yearplanmap": insert_fiscal_yearplanmap,
                                                      "user_accountplanmap": insert_user_accountplanmap,
                                                      "procuring_entityplanmap": insert_procuring_entityplanmap,
                                                      "procuring_entity": insert_procuring_entity,
                                                      "contact": insert_contact,
                                                      "address": insert_address,
                                                      "procuring_entitycontactmap": insert_procuring_entitycontactmap,
                                                      "procuring_entityaddressmap": insert_procuring_entityaddressmap,
                                                      "supplying_entity": insert_supplying_entity,
                                                      "supplying_entitycontactmap": insert_supplying_entitycontactmap,
                                                      "supplying_entityaddressmap": insert_supplying_entityaddressmap,
                                                      "user_account": insert_user_account,
                                                      "user_accountcontactmap": insert_user_accountcontactmap,
                                                      "user_accountaddressmap": insert_user_accountaddressmap,
                                                      "tender": insert_tender,
                                                      "procuring_entitytendermap": insert_procuring_entitytendermap,
                                                      "fiscal_yeartendermap": insert_fiscal_yeartendermap,
                                                      "payment": insert_payment,
                                                      "supplying_entitypaymentmap": insert_supplying_entitypaymentmap,
                                                      "bid": insert_bid,
                                                      "tenderbidmap": insert_tenderbidmap,
                                                      "tenderfeemap": insert_tenderfeemap,
                                                      "tenderpaymentmap": insert_tenderpaymentmap,
                                                      "bidpaymentmap": insert_bidpaymentmap,
                                                      "bidfeemap": insert_bidfeemap,
                                                      "appeal": insert_appeal,
                                                      "tenderappealmap": insert_tenderappealmap,
                                                      "paymentfeemap": insert_paymentfeemap,
                                                      "supplying_entitybidmap": insert_supplying_entitybidmap,
                                                      "supplying_entitytendermap": insert_supplying_entitytendermap,
                                                      "award": insert_award,
                                                      "supplying_entityawardmap": insert_supplying_entityawardmap,
                                                      "fiscal_yearawardmap": insert_fiscal_yearawardmap,
                                                      "awardtendermap": insert_awardtendermap,
                                                      "procuring_entityawardmap": insert_procuring_entityawardmap
                                                   }



#                                      THE ALGORITHM



fetch_size = 1
sink_crud_utility_tuple = (sink_database_connection_object, sink_database_object.get_cursor(), selection_object, insertion_object)
source_utility_tuple = (sink_database_connection_object, selection_object, id_generator_object, date_and_time_object, field_sanitizer)

for source_table in source_sink_table_mapping_dictionary:

    source_table_row_count = 1#source_database_object.get_table_entry_count(table_name=source_table.get_name())
    mapped_sink_table_dictionary = source_sink_table_mapping_dictionary[source_table]
    map_size = len(mapped_sink_table_dictionary)

    if map_size == 0:
        continue

    if map_size >= 1:
        total_sink_table_row_count = 0

        for sink_table in mapped_sink_table_dictionary:
            sink_table_row_count = sink_database_object.get_table_entry_count(table_name=sink_table.get_name())
            total_sink_table_row_count += sink_table_row_count

        if source_table_row_count == total_sink_table_row_count:
            continue

        if source_table_row_count > total_sink_table_row_count:
            row_count_difference = (source_table_row_count - total_sink_table_row_count)

            while row_count_difference > 0:
                key_string = source_table.get_comma_separated_key_string()
                start_count = total_sink_table_row_count
                source_table_row_dictionary = source_database_object.select_a_table_row(table_name=source_table.get_name(), order_by=key_string, order="ASC", offset=start_count, limit=fetch_size)
                source_callback_structure = source_table.get_tuple_building_callback_dictionary(sink_table.get_name())(*source_utility_tuple, source_table_row_dictionary)
                ordered_sink_table_list = source_callback_structure['ordered_key_list']

                for sink_table_name in ordered_sink_table_list:
                    sink_insertion_structure = source_callback_structure[sink_table_name]
                    if isinstance(sink_insertion_structure, tuple):
                        mapping_sink_table_name_crud_callback_dictionary[sink_table_name](*sink_crud_utility_tuple, *sink_insertion_structure)
                    elif isinstance(sink_insertion_structure, list):
                        for list_item in sink_insertion_structure:
                            if isinstance(list_item, tuple):
                                mapping_sink_table_name_crud_callback_dictionary[sink_table_name](*sink_crud_utility_tuple, *list_item)

                row_count_difference -= 1
                total_sink_table_row_count += 1





print(source_database_object.get_table_entry_count(table_name="award"))
print(source_database_object.select_a_table_row(table_name="award", order_by="id", order="DESC", offset=2, limit=1))
