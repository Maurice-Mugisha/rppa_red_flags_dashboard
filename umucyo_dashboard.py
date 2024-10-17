import os

from includes.database_connection import DatabaseConnection
from crud.ddl import DDL
from crud.selection import Select
from includes.date_time import DateTimeProvider
from includes.country import Country
from includes.country_phone_code import Country
from includes.business_logic_functions import *
from includes.serialization import *
from datetime import datetime
from includes.visualization.matplotlib_bar_graph import *
from includes.visualization.matplotlib_pie_chart import *
from includes.report_generation.spreadsheet_creator import *
from includes.dashboard_markup import *
from includes.field_list_creator import *
from includes.non_image_visualization_markup import *
from includes.time_benchmark import *
import json

import time
from datetime import datetime









selection_object = Select("Umucyo selection object 1")

# Client continent
client_continent = "Africa"

# Client country name
client_country_name = "Rwanda"

# Client capital city
client_capital_city = "Kigali"

# Date and timezone relative to a particular country
timezone_string = client_continent + os.sep + client_capital_city
date_and_time_object = DateTimeProvider(timezone_string)

time_benchmark_object = TimeBenchmark()



# The authentication file rules are such that every credential appears on a separate line, in the form given below
# <<credential name>>=#=<<credential value>> where the <<credential name>> can be host and the <<credential value>> can be localhost
# The other credentials are also written following the same pattern..
# The delimiter between the credential name and the credential value is =#=, meaning that no credential name and value should contain the delimiter =#=
authentication_directory = "auth"
authentication_file = "auth.txt"
auth_credentials_file_name = authentication_directory + os.sep + authentication_file
database_connection_facility = DatabaseConnection(auth_credentials_file_name)
database_connection_object = database_connection_facility.get_database_connection_object()


# Rename the database connection object to query executor
# because the same connection object has access to the query executor, we rename it as such
query_executor = database_connection_object

# Number of fiscal years to compare for red flags dashboard
num_fiscal_year_check = 9

# variable to determine whether or not to recompute the current fiscal year
recompute_current_fiscal_year = False

# variable to store the current fiscal year
current_fiscal_year = ""

# A serialization cache creator for performance optimization
serialization_deserialization_file_dictionary = {}
serialization_deserialization_object = SerializeDeserializeInJSON()
directory_dictionary = {
                          "data": "data" + os.sep + "cached_serialized_data" + os.sep,
                          "calculations_data": "data" + os.sep + "cached_serialized_calculations_data" + os.sep
                       }
serialization_deserialization_object.set_data_format_encoder(TypeToJSONEncoder)
serialization_deserialization_object.set_data_format_decoder(TypeToJSONDecoder)



# counting entries into the different tables for update detection
table_entry_count_dictionary = {"party":0, "planning":0, "tender":0, "bidder":0, "award":0, "contract":0}
for table_name in table_entry_count_dictionary:
    entry_count = get_table_count(selection_object, query_executor, table_name)
    table_entry_count_dictionary[table_name] = entry_count

table_entry_count_comparison_dictionary = {}
cached_entry_calculations_file = directory_dictionary["calculations_data"] + "tables" + os.sep + "entry_count.json"
serialization_deserialization_object.set_serialization_file_name(cached_entry_calculations_file)
file_exists = serialization_deserialization_object.check_file_exists()
if file_exists:
    table_entry_count_comparison_dictionary = json.loads(serialization_deserialization_object.deserialize_from_json())
else:
    serialization_deserialization_object.set_serialization_data(table_entry_count_dictionary)
    serialization_deserialization_object.serialize_in_json()
    table_entry_count_comparison_dictionary = table_entry_count_dictionary


are_entries_equal = True
print("")
#print(table_entry_count_dictionary)
#print(table_entry_count_comparison_dictionary)
print("")
print("%-15s %-20s %-24s %-s\n" % ("Table name", "Stored entry count", "Calculated entry count", "Count matches?"))
for table_name in table_entry_count_dictionary:
    table_count = table_entry_count_dictionary[table_name]
    comparison_count = table_entry_count_comparison_dictionary[table_name]
    are_counts_equal = (table_count == comparison_count)
    if are_counts_equal == False:
        are_entries_equal = False
        recompute_current_fiscal_year = False
        break
    print("%-15s %-20s %-24s %-s" % (table_name, table_count, comparison_count, are_counts_equal))
print("\n")




# Get all available fiscal years.
# Operation: select distinct fiscal years from the planning table or any other tables in which the fiscal year field appears as ext_fiscal_year
time_benchmark_object.set_task_name("Retrieving " + str(num_fiscal_year_check) + " fiscal years in the system")
time_benchmark_object.take_start_time()

fiscal_year_dictionary = get_fiscal_years(selection_object, query_executor)

time_difference = time_benchmark_object.get_time_difference()

print("Fiscal year retrieval \n")
new_fiscal_year_dictionary = {}
count = 0
max_fiscal_year_end_year = 0
for fiscal_year_key in fiscal_year_dictionary:
    if count < num_fiscal_year_check:
        new_fiscal_year_dictionary[fiscal_year_key] = fiscal_year_dictionary[fiscal_year_key]
        fiscal_year_start_year, fiscal_year_end_year = fiscal_year_key.split("/")
        if int(fiscal_year_end_year) > max_fiscal_year_end_year:
            max_fiscal_year_end_year = int(fiscal_year_end_year)
            current_fiscal_year = fiscal_year_key
        count += 1
    else:
        break
    print(fiscal_year_key)
fiscal_year_dictionary = new_fiscal_year_dictionary
time_benchmark_object.print_time_taken()
print("\n")
print("Current fiscal year: " + current_fiscal_year)
print("Current fiscal year requires data re-computation: " + str(recompute_current_fiscal_year))


# Dictionary to hold information on whether or not a given fiscal year's data should be re-computed
recompute_fiscal_year_dictionary = {}

for fiscal_year_key in fiscal_year_dictionary:
    if fiscal_year_key == current_fiscal_year:
        recompute_fiscal_year_dictionary[fiscal_year_key] = recompute_current_fiscal_year
    else:
        recompute_fiscal_year_dictionary[fiscal_year_key] = False

print("")
print("Fiscal year data recomputation status matrix\n")
print("%-15s %-20s\n" % ("Fiscal year", "To be recomputed?"))
for fiscal_year_key in recompute_fiscal_year_dictionary:
    print("%-15s %-20s" % (fiscal_year_key, recompute_fiscal_year_dictionary[fiscal_year_key]))


# Get a specific fiscal year procuring entities
# Operation: you actually just select all procuring entities and assume that they appear every fiscal year in this case
# Calculated data at rest files:
time_benchmark_object.set_task_name("Retrieving " + str(num_fiscal_year_check) + " fiscal years' procuring entities in the system")
time_benchmark_object.take_start_time()

fiscal_year_procuring_entity_dictionary = {}
#procuring_entity_dictionary = get_procurement_actor(selection_object, query_executor, "{buyer}")
for fiscal_year_id in fiscal_year_dictionary:

    data_cache_file_name = directory_dictionary["data"] + "procuring_entities" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "procuring_entities" + ".json"
    serialization_deserialization_object.set_serialization_file_name(data_cache_file_name)
    file_exists = serialization_deserialization_object.check_file_exists()

    if file_exists and recompute_fiscal_year_dictionary[fiscal_year_id] == False:
        fiscal_year_procuring_entity_dictionary[fiscal_year_id] = json.loads(serialization_deserialization_object.deserialize_from_json())
    else:
        specific_procuring_entities = get_procurement_actor(selection_object, query_executor, "{buyer}")
        fiscal_year_procuring_entity_dictionary[fiscal_year_id] = specific_procuring_entities
        if len(specific_procuring_entities) > 0:
            serialization_deserialization_object.set_serialization_data(specific_procuring_entities)
            serialization_deserialization_object.serialize_in_json()

print(" ")
print("\nProcuring entity list\n")
count = 0
for fiscal_year_id in fiscal_year_dictionary:
    for procuring_entity_id in fiscal_year_procuring_entity_dictionary[fiscal_year_id]:
        print(fiscal_year_procuring_entity_dictionary[fiscal_year_id][procuring_entity_id]['name'])
        if count == 14:
            break;
        count += 1
    if count == 14:
        break;

time_difference = time_benchmark_object.get_time_difference()
time_benchmark_object.print_time_taken()
print(" ")


# Get a specific fiscal year supplying entities
# Operation: check them by whether they have atleast a single bid every fiscal year to qualify them to appear in this dictionary's entries
#
time_benchmark_object.set_task_name("Retrieving " + str(num_fiscal_year_check) + " fiscal years' supplying entities in the system")
time_benchmark_object.take_start_time()

fiscal_year_supplying_entity_dictionary = {}

for fiscal_year_id in fiscal_year_dictionary:

    data_cache_file_name = directory_dictionary["data"] + "suppliers" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "suppliers" + ".json"
    serialization_deserialization_object.set_serialization_file_name(data_cache_file_name)
    file_exists = serialization_deserialization_object.check_file_exists()

    if file_exists and recompute_fiscal_year_dictionary[fiscal_year_id] == False:
        fiscal_year_supplying_entity_dictionary[fiscal_year_id] = json.loads(serialization_deserialization_object.deserialize_from_json())
        continue

    supplying_entity_dictionary = get_fiscal_year_supplying_entity(selection_object, query_executor, "{supplier}", fiscal_year_id)
    new_supplying_entity_dictionary = {}
    for supplying_entity_id in supplying_entity_dictionary:
        ext_tin = supplying_entity_dictionary[supplying_entity_id]['ext_tin']
        new_supplying_entity_dictionary[ext_tin] = supplying_entity_dictionary[supplying_entity_id]
    supplying_entity_dictionary = new_supplying_entity_dictionary
    fiscal_year_supplying_entity_dictionary[fiscal_year_id] = new_supplying_entity_dictionary


    if len(new_supplying_entity_dictionary) > 0:
        serialization_deserialization_object.set_serialization_data(fiscal_year_supplying_entity_dictionary[fiscal_year_id])
        serialization_deserialization_object.serialize_in_json()



print(" ")
print("\nSupplying entity list\n")
count = 0

for fiscal_year_id in fiscal_year_dictionary:
    if fiscal_year_id not in fiscal_year_supplying_entity_dictionary:
        continue
    specific_supplying_entity_dictionary = fiscal_year_supplying_entity_dictionary[fiscal_year_id]
    for supplying_entity_id in specific_supplying_entity_dictionary:
        #print(supplying_entity_id)
        print(fiscal_year_supplying_entity_dictionary[fiscal_year_id][supplying_entity_id]['name'])
        if count == 14:
            break;
        count += 1
    if count == 14:
        break;

time_difference = time_benchmark_object.get_time_difference()
time_benchmark_object.print_time_taken()
print("\n")


# (important for red flag 1)
# Get a specific fiscal year's procuring entities' procuring plans, this is sufficient to calculate red flag 1
# The dictionary on the next line is sufficient to handle the information needed to calculate red flag 1 and consequently visualize it
# The legacy id is used to reference the procuring enttty id in the planning table, so use use it to key a particular entity's plans. In the planning rable, it's called ext_pe_code
time_benchmark_object.set_task_name("Retrieving " + str(num_fiscal_year_check) + " fiscal years' procuring entities' procuring plans in the system")
time_benchmark_object.take_start_time()

fiscal_year_procuring_entity_plan_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    fiscal_year_procuring_entity_plan_dictionary[fiscal_year_id] = {}
    procuring_entity_dictionary = fiscal_year_procuring_entity_dictionary[fiscal_year_id]

    data_cache_file_name = directory_dictionary["data"] + os.sep + "plans" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "plans" + ".json"
    serialization_deserialization_object.set_serialization_file_name(data_cache_file_name)
    file_exists = serialization_deserialization_object.check_file_exists()

    if file_exists and recompute_fiscal_year_dictionary[fiscal_year_id] == False:
        fiscal_year_procuring_entity_plan_dictionary[fiscal_year_id] = json.loads(serialization_deserialization_object.deserialize_from_json())
    else:
        for procuring_entity_id in procuring_entity_dictionary:
            legacy_id = procuring_entity_dictionary[procuring_entity_id]['legacy_id']
            party_id = legacy_id
            procuring_entity_id = legacy_id
            specific_fiscal_year_procuring_entity_plan = get_specific_party_fiscal_year_plans(selection_object, query_executor, fiscal_year_id, party_id)
            fiscal_year_procuring_entity_plan_dictionary[fiscal_year_id][procuring_entity_id] = specific_fiscal_year_procuring_entity_plan

        if len(fiscal_year_procuring_entity_plan_dictionary[fiscal_year_id]) > 0:
            serialization_deserialization_object.set_serialization_data(fiscal_year_procuring_entity_plan_dictionary[fiscal_year_id])
            serialization_deserialization_object.serialize_in_json()




count = 0
print(" ")
print("\n%-70s  %-s\n" % ("Procuring actor legacy id", "Plan"))
for fiscal_year_id in fiscal_year_dictionary:
    specific_procuring_entity_dictionary = fiscal_year_procuring_entity_dictionary[fiscal_year_id]
    for procuring_entity_id in specific_procuring_entity_dictionary:
        legacy_id = specific_procuring_entity_dictionary[procuring_entity_id]['legacy_id']
        plan_dictionary = fiscal_year_procuring_entity_plan_dictionary[fiscal_year_id][legacy_id]
        for plan_id in plan_dictionary:
            if isinstance(plan_dictionary[plan_id], str):
                plan_dictionary[plan_id] = json.loads(plan_dictionary[plan_id])
            ext_pe_code = plan_dictionary[plan_id]['ext_pe_code']
            plan_count = len(plan_dictionary)
            print(" %-70s %-3s" % (ext_pe_code, str(plan_count)))
            break;
        if count == 14:
            break;
        count += 1
    if count == 1:
        break;

time_difference = time_benchmark_object.get_time_difference()
time_benchmark_object.print_time_taken()
print(" ")


# (Important for red flag 4)
# Get fiscal year supplying entities contacts
time_benchmark_object.set_task_name("Retrieving " + str(num_fiscal_year_check) + " fiscal years' supplying entities' contacts in the system")
time_benchmark_object.take_start_time()

fiscal_year_supplying_entity_contact_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    fiscal_year_supplying_entity_contact_dictionary[fiscal_year_id] = {}
    if fiscal_year_id not in fiscal_year_supplying_entity_dictionary:
        continue
    specific_fiscal_year_supplying_entities = fiscal_year_supplying_entity_dictionary[fiscal_year_id]
    for supplying_entity_id in specific_fiscal_year_supplying_entities:
        email = specific_fiscal_year_supplying_entities[supplying_entity_id]['contact_point_email']
        phone = specific_fiscal_year_supplying_entities[supplying_entity_id]['contact_point_telephone']
        if phone is None:
            phone = ""
        if email is None:
            email = ""
        contact_dictionary = {}
        contact_dictionary['0'] = {}
        contact_dictionary['0']['name'] = 'email'
        contact_dictionary['0']['value'] = email
        contact_dictionary['1'] = {}
        contact_dictionary['1']['name'] = 'phone'
        contact_dictionary['1']['value'] = phone
        fiscal_year_supplying_entity_contact_dictionary[fiscal_year_id][supplying_entity_id] = contact_dictionary


print("Able to get the supplying entity contacts for " + str(len(fiscal_year_supplying_entity_contact_dictionary)) +" fiscal years")
time_difference = time_benchmark_object.get_time_difference()
time_benchmark_object.print_time_taken()
print(" ")


# Get a specific fiscal year tenders' bids
# This has sufficient information to calculate red flag number 2, 6, 8 (in conjunction with awards) and all such variants
# Get a specific fiscal year tenders, for the last y number of years
# Get a specific tender's bids
print("\nRetrieving fiscal year tenders")
time_benchmark_object.set_task_name("Retrieving " + str(num_fiscal_year_check) + " fiscal years' tenders in the system")
time_benchmark_object.take_start_time()

fiscal_year_tender_dictionary = {}

for fiscal_year_id in fiscal_year_dictionary:

    fiscal_year_tender_dictionary[fiscal_year_id] = {}

    data_cache_file_name = directory_dictionary["data"] + os.sep + "tenders" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "tenders" + ".json"
    serialization_deserialization_object.set_serialization_file_name(data_cache_file_name)
    file_exists = serialization_deserialization_object.check_file_exists()

    if file_exists and recompute_fiscal_year_dictionary[fiscal_year_id] == False:
        #print("Deserialized")
        fiscal_year_tender_dictionary[fiscal_year_id] = json.loads(serialization_deserialization_object.deserialize_from_json())
    else:
        specific_fiscal_year_tenders = get_specific_fiscal_year_tenders(selection_object, query_executor, fiscal_year_id)
        fiscal_year_tender_dictionary[fiscal_year_id] = specific_fiscal_year_tenders
        if len(specific_fiscal_year_tenders) > 0:
            #print("Tender count: " + str(len(specific_fiscal_year_tenders)))
            serialization_deserialization_object.set_serialization_data(specific_fiscal_year_tenders)
            serialization_deserialization_object.serialize_in_json()

time_difference = time_benchmark_object.get_time_difference()
time_benchmark_object.print_time_taken()
print(" ")


print("\nRetrieving fiscal year tenders and corresponding bids")
time_benchmark_object.set_task_name("Retrieving " + str(num_fiscal_year_check) + " fiscal years' tenders and corresponding bids in the system")
time_benchmark_object.take_start_time()

fiscal_year_tender_bid_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:

    fiscal_year_tender_bid_dictionary[fiscal_year_id] = {}
    data_cache_file_name = directory_dictionary["data"] + os.sep + "tender_bids" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "bids" + ".json"
    serialization_deserialization_object.set_serialization_file_name(data_cache_file_name)
    file_exists = serialization_deserialization_object.check_file_exists()

    if file_exists and recompute_fiscal_year_dictionary[fiscal_year_id] == False:
         fiscal_year_tender_bid_dictionary[fiscal_year_id] = json.loads(serialization_deserialization_object.deserialize_from_json())
    else:
        for tender_id in fiscal_year_tender_dictionary[fiscal_year_id]:
            fiscal_year_tender_bid_dictionary[fiscal_year_id][tender_id] = get_tender_bidders(selection_object, query_executor, tender_id)
        if len(fiscal_year_tender_bid_dictionary[fiscal_year_id]) > 0:
            serialization_deserialization_object.set_serialization_data(fiscal_year_tender_bid_dictionary[fiscal_year_id])
            serialization_deserialization_object.serialize_in_json()

time_difference = time_benchmark_object.get_time_difference()
time_benchmark_object.print_time_taken()
print(" ")


print("\nRetrieving fiscal year bids")
time_benchmark_object.set_task_name("Retrieving " + str(num_fiscal_year_check) + " fiscal years' bids in the system")
time_benchmark_object.take_start_time()

fiscal_year_bid_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:

    fiscal_year_bid_dictionary[fiscal_year_id] = {}
    data_cache_file_name = directory_dictionary["data"] + os.sep + "bids" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "bids" + ".json"
    serialization_deserialization_object.set_serialization_file_name(data_cache_file_name)
    file_exists = serialization_deserialization_object.check_file_exists()

    if file_exists and recompute_fiscal_year_dictionary[fiscal_year_id] == False:
        fiscal_year_bid_dictionary[fiscal_year_id] = json.loads(serialization_deserialization_object.deserialize_from_json())
    else:
        specific_fiscal_year_bid_dictionary = get_specific_fiscal_year_bidder(selection_object, query_executor, fiscal_year_id)
        fiscal_year_bid_dictionary[fiscal_year_id] = specific_fiscal_year_bid_dictionary
        if len(fiscal_year_bid_dictionary[fiscal_year_id]) > 0:
            serialization_deserialization_object.set_serialization_data(specific_fiscal_year_bid_dictionary)
            serialization_deserialization_object.serialize_in_json()

time_difference = time_benchmark_object.get_time_difference()
time_benchmark_object.print_time_taken()
print(" ")




# (important for red flag 3)
# Get a specific fiscal year tender fee payments
print("Fiscal year tender fee payments")
time_benchmark_object.set_task_name("Retrieving " + str(num_fiscal_year_check) + " fiscal years' bids in the system")
time_benchmark_object.take_start_time()

fiscal_year_tender_payment_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    fiscal_year_tender_payment_dictionary[fiscal_year_id] = {}
    for tender_id in fiscal_year_tender_dictionary[fiscal_year_id]:
        specific_tender_payment = {}
        fiscal_year_tender_payment_dictionary[fiscal_year_id][tender_id] = specific_tender_payment

time_difference = time_benchmark_object.get_time_difference()
time_benchmark_object.print_time_taken()
print(" ")


# (Important for red flag 8 and 10)
# Get a specific fiscal year supplying entitys' bids
print("Fiscal year supplying entities' bids")
time_benchmark_object.set_task_name("Retrieving " + str(num_fiscal_year_check) + " fiscal years' supplying entities' bids in the system")
time_benchmark_object.take_start_time()

fiscal_year_supplying_entity_bid_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    fiscal_year_supplying_entity_bid_dictionary[fiscal_year_id] = {}
    if fiscal_year_id not in fiscal_year_supplying_entity_dictionary:
        continue
    specific_fiscal_year_supplying_entity_dictionary = fiscal_year_supplying_entity_dictionary[fiscal_year_id] # Maybe use all the supplying entities if the year mappings are not sufficient

    data_cache_file_name = directory_dictionary["data"] + os.sep + "supplying_entity_bids" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "bids" + ".json"
    serialization_deserialization_object.set_serialization_file_name(data_cache_file_name)
    file_exists = serialization_deserialization_object.check_file_exists()

    if file_exists and recompute_fiscal_year_dictionary[fiscal_year_id] == False:
        fiscal_year_supplying_entity_bid_dictionary[fiscal_year_id] = json.loads(serialization_deserialization_object.deserialize_from_json())
    else:
        for supplying_entity_id in specific_fiscal_year_supplying_entity_dictionary:
            # supplying_entity_id = ext_tin
            specific_supplying_entity_bid_dictionary = get_specific_fiscal_year_supplying_entity_bids(selection_object, query_executor, fiscal_year_id, supplying_entity_id)
            fiscal_year_supplying_entity_bid_dictionary[fiscal_year_id][supplying_entity_id] = specific_supplying_entity_bid_dictionary
        if len(fiscal_year_supplying_entity_bid_dictionary[fiscal_year_id]) > 0:
            serialization_deserialization_object.set_serialization_data(fiscal_year_supplying_entity_bid_dictionary[fiscal_year_id])
            serialization_deserialization_object.serialize_in_json()

time_difference = time_benchmark_object.get_time_difference()
time_benchmark_object.print_time_taken()
print(" ")



# Get a specific fiscal year awards
print("Fiscal year Awards")
time_benchmark_object.set_task_name("Retrieving " + str(num_fiscal_year_check) + " fiscal years' awards in the system")
time_benchmark_object.take_start_time()

fiscal_year_award_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:

    data_cache_file_name = directory_dictionary["data"] + os.sep + "awards_all" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "awards" + ".json"
    serialization_deserialization_object.set_serialization_file_name(data_cache_file_name)
    file_exists = serialization_deserialization_object.check_file_exists()

    if file_exists and recompute_fiscal_year_dictionary[fiscal_year_id] == False:
        fiscal_year_award_dictionary[fiscal_year_id] = json.loads(serialization_deserialization_object.deserialize_from_json())
    else:
        fiscal_year_award_dictionary[fiscal_year_id] = get_specific_fiscal_year_awards(selection_object, query_executor, fiscal_year_id)
        if len(fiscal_year_award_dictionary[fiscal_year_id]) > 0:
            serialization_deserialization_object.set_serialization_data(fiscal_year_award_dictionary[fiscal_year_id])
            serialization_deserialization_object.serialize_in_json()

time_difference = time_benchmark_object.get_time_difference()
time_benchmark_object.print_time_taken()
print(" ")


# Get a fiscal year supplying entity awards
print("Fiscal year suppling entities' awards")
time_benchmark_object.set_task_name("Retrieving " + str(num_fiscal_year_check) + " fiscal years' supplying entities' awards in the system")
time_benchmark_object.take_start_time()

fiscal_year_supplying_entity_award_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    fiscal_year_supplying_entity_award_dictionary[fiscal_year_id] = {}
    if fiscal_year_id not in fiscal_year_supplying_entity_dictionary:
        continue

    data_cache_file_name = directory_dictionary["data"] + os.sep + "awards_supplying_entity" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "awards" + ".json"
    serialization_deserialization_object.set_serialization_file_name(data_cache_file_name)
    file_exists = serialization_deserialization_object.check_file_exists()

    if file_exists and recompute_fiscal_year_dictionary[fiscal_year_id] == False:
        fiscal_year_supplying_entity_award_dictionary[fiscal_year_id] = json.loads(serialization_deserialization_object.deserialize_from_json())
    else:
        for supplying_entity_id in fiscal_year_supplying_entity_dictionary[fiscal_year_id]:
            specific_supplying_entity_awards = get_fiscal_year_supplying_entity_awards(selection_object, query_executor, fiscal_year_id, supplying_entity_id)
            fiscal_year_supplying_entity_award_dictionary[fiscal_year_id][supplying_entity_id] = specific_supplying_entity_awards
        if len(fiscal_year_award_dictionary[fiscal_year_id]) > 0:
            serialization_deserialization_object.set_serialization_data(fiscal_year_supplying_entity_award_dictionary[fiscal_year_id])
            serialization_deserialization_object.serialize_in_json()

time_difference = time_benchmark_object.get_time_difference()
time_benchmark_object.print_time_taken()
print(" ")

# Get fiscal year procuring entity award
print("Fiscal year procuring entities' awards")
time_benchmark_object.set_task_name("Retrieving " + str(num_fiscal_year_check) + " fiscal years' procuring entities' awards in the system")
time_benchmark_object.take_start_time()

fiscal_year_procuring_entity_award_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    fiscal_year_procuring_entity_award_dictionary[fiscal_year_id] = {}

    data_cache_file_name = directory_dictionary["data"] + os.sep + "awards_procuring_entity" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "awards" + ".json"
    serialization_deserialization_object.set_serialization_file_name(data_cache_file_name)
    file_exists = serialization_deserialization_object.check_file_exists()

    if file_exists and recompute_fiscal_year_dictionary[fiscal_year_id] == False:
        fiscal_year_procuring_entity_award_dictionary[fiscal_year_id] = json.loads(serialization_deserialization_object.deserialize_from_json())
    else:
        for procuring_entity_id in fiscal_year_procuring_entity_dictionary[fiscal_year_id]:
            ext_pe_code = fiscal_year_procuring_entity_dictionary[fiscal_year_id][procuring_entity_id]['legacy_id']
            fiscal_year_procuring_entity_award_dictionary[fiscal_year_id][procuring_entity_id] = get_fiscal_year_procuring_entity_awards(selection_object, query_executor, fiscal_year_id, ext_pe_code)
        if len(fiscal_year_award_dictionary[fiscal_year_id]) > 0:
            serialization_deserialization_object.set_serialization_data(fiscal_year_procuring_entity_award_dictionary[fiscal_year_id])
            serialization_deserialization_object.serialize_in_json()

time_difference = time_benchmark_object.get_time_difference()
time_benchmark_object.print_time_taken()
print(" ")


# Get the fiscal year procuring entity supplying entity awards, awards given by procuring entities to given certain supplying entities in the selected fiscal years
# Since the only end goal for this code block/algorithm is to calculate red flag 9, we will only display serialize the calculated red flag result and depend upon it
# to avoid repeating the same time intensive calculation

print("Fiscal year procuring entities' awards to corresponding supplying entities")
time_benchmark_object.set_task_name("Retrieving " + str(num_fiscal_year_check) + " fiscal years' procuring entities' awards to suppliers in the system")
time_benchmark_object.take_start_time()

configuration_number_of_direct_contracts = 2;
cndc = configuration_number_of_direct_contracts
red_flag_9_dictionary = {}
fiscal_year_procuring_entity_supplying_entity_award_dictionary = {}
for fiscal_year_id in fiscal_year_procuring_entity_award_dictionary:
    fiscal_year_procuring_entity_supplying_entity_award_dictionary[fiscal_year_id] = {}
    red_flag_9_dictionary[fiscal_year_id] = {"count": 0, "set": set()}

    data_cache_file_name = directory_dictionary["calculations_data"] + os.sep + "red_flag_9" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "data" + ".json"
    serialization_deserialization_object.set_serialization_file_name(data_cache_file_name)
    file_exists = serialization_deserialization_object.check_file_exists()

    if file_exists and recompute_fiscal_year_dictionary[fiscal_year_id] == False:
        red_flag_9_dictionary[fiscal_year_id] = json.loads(serialization_deserialization_object.deserialize_from_json())
        continue


    for procuring_entity_id in fiscal_year_procuring_entity_award_dictionary[fiscal_year_id]:
        fiscal_year_procuring_entity_supplying_entity_award_dictionary[fiscal_year_id][procuring_entity_id] = {}
        specific_procuring_entity_awards = fiscal_year_procuring_entity_award_dictionary[fiscal_year_id][procuring_entity_id]
        if len(specific_procuring_entity_awards) == 0:
            continue

        for award_id in specific_procuring_entity_awards:
            award_ext_tender_method_code = specific_procuring_entity_awards[award_id]['ext_tender_method_code']
            award_ext_pe_code = specific_procuring_entity_awards[award_id]['ext_pe_code']
            award_legacy_id = specific_procuring_entity_awards[award_id]['legacy_id']
            supplier_award_tuple = (award_legacy_id, award_ext_tender_method_code, award_ext_pe_code)
            specific_award_supplying_entities = get_specific_award_supplying_entities(selection_object, query_executor, award_legacy_id)

            direct_count_dictionary = {}
            for supplying_entity_id in specific_award_supplying_entities:

                if supplying_entity_id in fiscal_year_procuring_entity_supplying_entity_award_dictionary[fiscal_year_id][procuring_entity_id]:
                    fiscal_year_procuring_entity_supplying_entity_award_dictionary[fiscal_year_id][procuring_entity_id][supplying_entity_id].add(supplier_award_tuple)
                    supplier_awards_tuple_list = fiscal_year_procuring_entity_supplying_entity_award_dictionary[fiscal_year_id][procuring_entity_id][supplying_entity_id]

                    for _ , method , buyer in supplier_awards_tuple_list:
                        if buyer not in direct_count_dictionary:
                            direct_count_dictionary[buyer] = 0
                        if method.lower() == "direct":
                            direct_count_dictionary[buyer] += 1
                        else:
                            continue

                        direct_contract_count = direct_count_dictionary[buyer]

                        if direct_count_dictionary[buyer] >= cndc:
                            red_flag_9_dictionary[fiscal_year_id]["count"] += 1
                            procuring_entity_tin = fiscal_year_procuring_entity_dictionary[fiscal_year_id][procuring_entity_id]['ext_tin']
                            red_flag_9_dictionary[fiscal_year_id]["set"].add((procuring_entity_id, procuring_entity_tin, supplying_entity_id))

                else:
                    fiscal_year_procuring_entity_supplying_entity_award_dictionary[fiscal_year_id][procuring_entity_id][supplying_entity_id] = set()
                    fiscal_year_procuring_entity_supplying_entity_award_dictionary[fiscal_year_id][procuring_entity_id][supplying_entity_id].add(supplier_award_tuple)

    if len(red_flag_9_dictionary[fiscal_year_id]) > 0:
        serialization_deserialization_object.set_serialization_data(red_flag_9_dictionary[fiscal_year_id])
        serialization_deserialization_object.serialize_in_json()

time_difference = time_benchmark_object.get_time_difference()
time_benchmark_object.print_time_taken()
print(" ")


# No information on appeals and payments is available yet
# Get the F fiscal year award appeals, this should help in calculating red flag 5
print("Fiscal year appeals for awards")
time_benchmark_object.set_task_name("Retrieving " + str(num_fiscal_year_check) + " fiscal years' appeals for awards in the system")
time_benchmark_object.take_start_time()

fiscal_year_award_appeal_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    fiscal_year_award_appeal_dictionary[fiscal_year_id] = {}

    data_cache_file_name = directory_dictionary["data"] + os.sep + "awards_tenders" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "awards" + ".json"
    serialization_deserialization_object.set_serialization_file_name(data_cache_file_name)
    file_exists = serialization_deserialization_object.check_file_exists()

    if file_exists and recompute_fiscal_year_dictionary[fiscal_year_id] == False:
        fiscal_year_award_appeal_dictionary[fiscal_year_id] = json.loads(serialization_deserialization_object.deserialize_from_json())
        continue

    specific_fiscal_year_awards = fiscal_year_award_dictionary[fiscal_year_id]
    for award_id in specific_fiscal_year_awards:
        specific_award_appeals = {}#get_specific_award_appeals(selection_object, query_executor, award_id) # no data is available yet
        if len(specific_award_appeals) == 0: # one can as well use both of them, instead of one
            specific_award_tenders = get_specific_award_tenders(selection_object, query_executor, award_id)
            appeal_dictionary = {}
            for tender_id in specific_award_tenders:
                specific_tender_appeals = {} # get_specific_tender_appeals(selection_object, query_executor, tender_id)
                for appeal_id in specific_tender_appeals:
                    appeal_dictionary[appeal_id] = specific_tender_appeals[appeal_id]
            fiscal_year_award_appeal_dictionary[fiscal_year_id][award_id] = appeal_dictionary
        else:
            fiscal_year_award_appeal_dictionary[fiscal_year_id][award_id] = specific_award_appeals

    if len(fiscal_year_award_appeal_dictionary[fiscal_year_id]) > 0:
        serialization_deserialization_object.set_serialization_data(fiscal_year_award_appeal_dictionary[fiscal_year_id])
        serialization_deserialization_object.serialize_in_json()

time_difference = time_benchmark_object.get_time_difference()
time_benchmark_object.print_time_taken()
print(" ")


# Get a specific fiscal year tender award(s)
print("Fiscal year tender for awards")
time_benchmark_object.set_task_name("Retrieving " + str(num_fiscal_year_check) + " fiscal years' tender awards in the system")
time_benchmark_object.take_start_time()

fiscal_year_tender_award_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    fiscal_year_tender_award_dictionary[fiscal_year_id] = {}

    data_cache_file_name = directory_dictionary["data"] + os.sep + "tender_awards" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "tender_awards" + ".json"
    serialization_deserialization_object.set_serialization_file_name(data_cache_file_name)
    file_exists = serialization_deserialization_object.check_file_exists()

    if file_exists and recompute_fiscal_year_dictionary[fiscal_year_id] == False:
        fiscal_year_tender_award_dictionary[fiscal_year_id] = json.loads(serialization_deserialization_object.deserialize_from_json())
    else:
        for tender_id in fiscal_year_tender_dictionary[fiscal_year_id]:
            tender_reference_number = fiscal_year_tender_dictionary[fiscal_year_id][tender_id]['legacy_id']
            specific_tender_awards = get_specific_tender_awards(selection_object, query_executor, tender_reference_number)
            fiscal_year_tender_award_dictionary[fiscal_year_id][tender_id] = specific_tender_awards
        if len(fiscal_year_tender_award_dictionary[fiscal_year_id]) > 0:
            serialization_deserialization_object.set_serialization_data(fiscal_year_tender_award_dictionary[fiscal_year_id])
            serialization_deserialization_object.serialize_in_json()

time_difference = time_benchmark_object.get_time_difference()
time_benchmark_object.print_time_taken()
print(" ")








#########################################################################################################
#  Start work on the different red flags in some construct, a class module perhaps or function module   #
#########################################################################################################








field_list_creator_object = FieldListCreator()
red_flag_list = list()
visualization_dictionary = {}
fiscal_year_list = []
fiscal_year_red_flag_dictionary = {}
visualization_markup_object = NonImageVisualizationMarkup()






# Red flag 1: Procuring entities that did not submit their procurement plans
#             get the procurement stages of every fiscal year, and then pick out the planning stage
#             get the procuring entities' procurement stages and select out the planning stage (model re-adjusted)

red_flag_1_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:

    calculated_data_file = "data" + os.sep + "calculated_red_flag_data" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "red_flag_1.json"
    serialization_deserialization_object.set_serialization_file_name(calculated_data_file)
    file_exists = serialization_deserialization_object.check_file_exists()

    if file_exists and recompute_fiscal_year_dictionary[fiscal_year_id] == False:
        red_flag_1_dictionary[fiscal_year_id] = json.loads(serialization_deserialization_object.deserialize_from_json())
    else:
        red_flag_1_dictionary[fiscal_year_id] = {"without_a_plan":0, "with_a_plan":0, "without_a_plan_set":set(), "with_a_plan_set":set()}
        specific_fiscal_year_procuring_entity_dictionary = fiscal_year_procuring_entity_dictionary[fiscal_year_id]
        for procuring_entity_id in specific_fiscal_year_procuring_entity_dictionary:
            legacy_id = specific_fiscal_year_procuring_entity_dictionary[procuring_entity_id]['legacy_id']
            if len(fiscal_year_procuring_entity_plan_dictionary[fiscal_year_id][legacy_id]) == 0:
                red_flag_1_dictionary[fiscal_year_id]["without_a_plan"] += 1
                red_flag_1_dictionary[fiscal_year_id]["without_a_plan_set"].add(legacy_id)
            else:
                red_flag_1_dictionary[fiscal_year_id]["with_a_plan"] += 1
                #red_flag_1_dictionary[fiscal_year_id]["with_a_plan_set"].add(procuring_entity_id) # not of interest for now
        # serialize the calculated data
        if len(red_flag_1_dictionary[fiscal_year_id]) > 0:
            serialization_deserialization_object.set_serialization_data(red_flag_1_dictionary[fiscal_year_id])
            serialization_deserialization_object.serialize_in_json()

    red_flag_id = fiscal_year_id.replace("/", "") + "red_flag_1"
    red_flag_dictionary = {"id": red_flag_id, "name": "Procuring entity without a procurement plan"}
    red_flag_list.append(red_flag_dictionary)
    visualization_dictionary[red_flag_id] = {}
    visualization_dictionary[red_flag_id]['is_image'] = True
    if fiscal_year_id not in fiscal_year_list:
        fiscal_year_list.append(fiscal_year_id)
    if fiscal_year_id not in fiscal_year_red_flag_dictionary:
        fiscal_year_red_flag_dictionary[fiscal_year_id] = list()
        fiscal_year_red_flag_dictionary[fiscal_year_id].append(red_flag_dictionary)
    else:
        fiscal_year_red_flag_dictionary[fiscal_year_id].append(red_flag_dictionary)


for fiscal_year_id in red_flag_1_dictionary:

    visualization_file_name = "data" + os.sep + "cached_generated_multimedia" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "red_flag_1.jpg"
    spreadsheet_file_name = "data" + os.sep + "cached_generated_reports" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "red_flag_1.xlsx"
    red_flag_id = fiscal_year_id.replace("/", "") + "red_flag_1"
    visualization_dictionary[red_flag_id]["visualization_link"] = visualization_file_name
    visualization_dictionary[red_flag_id]["report_link"] = spreadsheet_file_name

    # Check the computed visualization and/or report files are already in existence
    serialization_deserialization_object.set_serialization_file_name(visualization_file_name)
    visualization_file_exists = serialization_deserialization_object.check_file_exists()
    serialization_deserialization_object.set_serialization_file_name(spreadsheet_file_name)
    spreadsheet_file_exists = serialization_deserialization_object.check_file_exists()
    files_exist = (visualization_file_exists and spreadsheet_file_exists)

    if files_exist and recompute_fiscal_year_dictionary[fiscal_year_id] == False:
        continue

    # visualizing red flag 1 using a pie chart. This is 1/2 of the most important tasks of calculating this red flag
    title = fiscal_year_id.replace("/", "-")  + " fiscal year plan submissions"
    value_list = [red_flag_1_dictionary[fiscal_year_id]["with_a_plan"], red_flag_1_dictionary[fiscal_year_id]["without_a_plan"]]
    color_list = ['green', 'orange']
    label_list = ["Submitted plan", "Did not submit plans"]
    width = 8
    height = 3
    pie_chart_drawer_object = PieChartDrawer(value_list, color_list, label_list, width, height, visualization_file_name, title)
    pie_chart_drawer_object.draw_pie_chart()

    # Reporting on red flag 1 using a spreadsheet. This is 2/2 of the most important tasks of calculating this red flag
    data = list()
    data.append(field_list_creator_object.get_procurement_party_field_list([]))

    for entity_id in fiscal_year_procuring_entity_dictionary[fiscal_year_id]:
        entity_dictionary = fiscal_year_procuring_entity_dictionary[fiscal_year_id][entity_id]
        legacy_id = entity_dictionary['legacy_id']
        if legacy_id in red_flag_1_dictionary[fiscal_year_id]['without_a_plan_set']:
            data_list = field_list_creator_object.get_party_data_list(entity_dictionary, [])
            data.append(data_list)

    spreadsheet_creator_object = SpreadsheetCreator(spreadsheet_file_name, data)
    spreadsheet_creator_object.create_spreadsheet()




# Red flag 2: Tender has less than three bids (not a closed tender)
#             Get the particular fiscal year tenders
#             Get the fiscal year tender bids


red_flag_2_dictionary = {}

for fiscal_year_id in fiscal_year_dictionary:

    calculated_data_file = "data" + os.sep + "calculated_red_flag_data" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "red_flag_2.json"
    serialization_deserialization_object.set_serialization_file_name(calculated_data_file)
    file_exists = serialization_deserialization_object.check_file_exists()

    if file_exists and recompute_fiscal_year_dictionary[fiscal_year_id] == False:
        red_flag_2_dictionary[fiscal_year_id] = json.loads(serialization_deserialization_object.deserialize_from_json())
    else:
        red_flag_2_dictionary[fiscal_year_id] = {"less_than_x_bids":0, "more_than_x_bids":0, "less_than_x_bids_histogram":dict(), "less_than_x_bids_count_histogram":dict(), "more_than_x_bids_histogram":dict()}
        with_less_than_x_bids_count_dictionary = {x:0 for x in range(1, 13)}
        with_less_than_x_bids_set = set()
        specific_fiscal_year_tender_dictionary = fiscal_year_tender_dictionary[fiscal_year_id]

        for tender_id in specific_fiscal_year_tender_dictionary:
            if len(fiscal_year_tender_bid_dictionary[fiscal_year_id][tender_id]) < 3:
                red_flag_2_dictionary[fiscal_year_id]["less_than_x_bids"] += 1
                creation_date = specific_fiscal_year_tender_dictionary[tender_id]["tender_period_start_date"]

                if isinstance(creation_date, str) and len(creation_date) > 0:
                    date_string = creation_date.replace("T", " ").split(".")[0]
                    creation_date_object = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
                    month_key = creation_date_object.strftime("%m")
                    with_less_than_x_bids_count_dictionary[int(month_key)] += 1
                    with_less_than_x_bids_set.add(tender_id)

            else:
                red_flag_2_dictionary[fiscal_year_id]["more_than_x_bids"] += 1
                #red_flag_2_dictionary[fiscal_year_id]["more_than_x_bids_histogram"].add(tender_id) # not of interest for now
        red_flag_2_dictionary[fiscal_year_id]["less_than_x_bids_count_histogram"] = with_less_than_x_bids_count_dictionary
        red_flag_2_dictionary[fiscal_year_id]["less_than_x_bids_set"] = with_less_than_x_bids_set

    red_flag_id = fiscal_year_id.replace("/", "") + "red_flag_2"
    red_flag_dictionary = {"id": red_flag_id, "name": "Tenders with less than X(=3) bids"}
    red_flag_list.append(red_flag_dictionary)
    visualization_dictionary[red_flag_id] = {}
    visualization_dictionary[red_flag_id]['is_image'] = True
    if fiscal_year_id not in fiscal_year_list:
        fiscal_year_list.append(fiscal_year_id)
    if fiscal_year_id not in fiscal_year_red_flag_dictionary:
        fiscal_year_red_flag_dictionary[fiscal_year_id] = list()
        fiscal_year_red_flag_dictionary[fiscal_year_id].append(red_flag_dictionary)
    else:
        fiscal_year_red_flag_dictionary[fiscal_year_id].append(red_flag_dictionary)

    if len(red_flag_2_dictionary[fiscal_year_id]) > 0:
        serialization_deserialization_object.set_serialization_data(red_flag_2_dictionary[fiscal_year_id])
        serialization_deserialization_object.serialize_in_json()




for fiscal_year_id in red_flag_2_dictionary:

    visualization_file_name = "data" + os.sep + "cached_generated_multimedia" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "red_flag_2.jpg"
    spreadsheet_file_name = "data" + os.sep + "cached_generated_reports" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "red_flag_2.xlsx"
    red_flag_id = fiscal_year_id.replace("/", "") + "red_flag_2"
    visualization_dictionary[red_flag_id]["visualization_link"] = visualization_file_name
    visualization_dictionary[red_flag_id]["report_link"] = spreadsheet_file_name

    # Check the computed visualization and/or report files are already in existence
    serialization_deserialization_object.set_serialization_file_name(visualization_file_name)
    visualization_file_exists = serialization_deserialization_object.check_file_exists()
    serialization_deserialization_object.set_serialization_file_name(spreadsheet_file_name)
    spreadsheet_file_exists = serialization_deserialization_object.check_file_exists()
    files_exist = (visualization_file_exists and spreadsheet_file_exists)

    if files_exist and recompute_fiscal_year_dictionary[fiscal_year_id] == False:
        continue

    # visualizing red flag 2,  using a bar graph. This is 1/2 of the most important tasks of calculating this red flag
    title = fiscal_year_id.replace("/", "-")  + " fiscal year tenders with less than 3 bids"
    value_dict = red_flag_2_dictionary[fiscal_year_id]["less_than_x_bids_count_histogram"]
    bar_color = "#007700"
    edge_color = "white"
    x_axis_label = "Month"
    y_axis_label = "Tenders"
    width = 15
    height = 8
    save_path_and_name = visualization_file_name

    bargraph_drawer_object = BarGraphDrawer(value_dict, bar_color, edge_color, x_axis_label, y_axis_label, title, width, height, save_path_and_name)
    bargraph_drawer_object.draw_bar_graph()

    # Reporting on red flag 2 using a spreadsheet. This is 2/2 of the most important tasks of calculating this red flag
    data = list()
    data.append(field_list_creator_object.get_tender_field_list([]))

    for tender_id in red_flag_2_dictionary[fiscal_year_id]["less_than_x_bids_set"]:
        tender_dictionary = fiscal_year_tender_dictionary[fiscal_year_id][tender_id]
        data_list = field_list_creator_object.get_tender_data_list(tender_dictionary, [])
        data.append(data_list)

    spreadsheet_creator_object = SpreadsheetCreator(spreadsheet_file_name, data)
    spreadsheet_creator_object.create_spreadsheet()






# Red flag 3: The tenders where bidders who paid a tender participation fees is way less than the number of bidders who submitted their bids
#             Get the particular fiscal year tenders
#             Get the bid counts per tender

configuration_payment_bid_number_difference = 1
cpbnd = configuration_payment_bid_number_difference
red_flag_3_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    red_flag_3_dictionary[fiscal_year_id] = {}
    for tender_id in fiscal_year_tender_dictionary[fiscal_year_id]:
        payment_count = len(fiscal_year_tender_payment_dictionary[fiscal_year_id][tender_id])
        bid_count = len(fiscal_year_tender_bid_dictionary[fiscal_year_id][tender_id])
        if (payment_count - bid_count) >= cpbnd:
            red_flag_3_dictionary[fiscal_year_id][tender_id] = {"payment_count":payment_count, "bid_count":bid_count}



# Red flag 4: Check the suppliers who share the same number or email
#             Get particular fiscal year suppliers
#             Get each supplier's contacts and compare each and every supplier's contacts with the other

red_flag_4_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:

    calculated_data_file = "data" + os.sep + "calculated_red_flag_data" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "red_flag_4.json"
    serialization_deserialization_object.set_serialization_file_name(calculated_data_file)
    file_exists = serialization_deserialization_object.check_file_exists()

    if file_exists and recompute_fiscal_year_dictionary[fiscal_year_id] == False:
        red_flag_4_dictionary[fiscal_year_id] = json.loads(serialization_deserialization_object.deserialize_from_json())
    else:
        red_flag_4_dictionary[fiscal_year_id] = {"same_email_count":0, "same_phone_count":0, "same_email_pair_set": set(), "same_phone_pair_set": set()}
        specific_supplying_entities = fiscal_year_supplying_entity_contact_dictionary[fiscal_year_id]
        for supplying_entity_id in specific_supplying_entities:
            for another_supplying_entity_id in specific_supplying_entities:
                if supplying_entity_id == another_supplying_entity_id:
                    continue;
                supplying_entity_contacts = fiscal_year_supplying_entity_contact_dictionary[fiscal_year_id][supplying_entity_id]
                another_supplying_entity_contacts = fiscal_year_supplying_entity_contact_dictionary[fiscal_year_id][another_supplying_entity_id]
                email_address = ""
                phone = ""
                another_email_address = ""
                another_phone = ""
                for contact_key in supplying_entity_contacts:
                    contact_name = supplying_entity_contacts[contact_key]["name"]
                    if contact_name.lower()[:5] == "email":
                        email_address = supplying_entity_contacts[contact_key]["value"]
                    if contact_name.lower() == "phone":
                        phone = supplying_entity_contacts[contact_key]["value"]
                for contact_key in another_supplying_entity_contacts:
                    contact_name = another_supplying_entity_contacts[contact_key]["name"]
                    if contact_name.lower()[:5] == "email":
                        another_email_address = another_supplying_entity_contacts[contact_key]["value"]
                    if contact_name.lower() == "phone":
                        another_phone = another_supplying_entity_contacts[contact_key]["value"]

                if len(email_address) > 0 and email_address.strip() == another_email_address.strip():
                    red_flag_4_dictionary[fiscal_year_id]["same_email_count"] += 1
                    red_flag_4_dictionary[fiscal_year_id]["same_email_pair_set"].add((supplying_entity_id, another_supplying_entity_id)) # set of tuples
                if len(phone) > 0 and phone.strip() == another_phone.strip():
                    red_flag_4_dictionary[fiscal_year_id]["same_phone_count"] += 1
                    red_flag_4_dictionary[fiscal_year_id]["same_phone_pair_set"].add((supplying_entity_id, another_supplying_entity_id))

        if len(red_flag_4_dictionary[fiscal_year_id]) > 0:
            serialization_deserialization_object.set_serialization_data(red_flag_4_dictionary[fiscal_year_id])
            serialization_deserialization_object.serialize_in_json()

    red_flag_id = fiscal_year_id.replace("/", "") + "red_flag_4"
    red_flag_dictionary = {"id": red_flag_id, "name": "Supplying entities with a shared contact"}
    red_flag_list.append(red_flag_dictionary)
    visualization_dictionary[red_flag_id] = {}

    if fiscal_year_id not in fiscal_year_list:
        fiscal_year_list.append(fiscal_year_id)
    if fiscal_year_id not in fiscal_year_red_flag_dictionary:
        fiscal_year_red_flag_dictionary[fiscal_year_id] = list()
        fiscal_year_red_flag_dictionary[fiscal_year_id].append(red_flag_dictionary)
    else:
        fiscal_year_red_flag_dictionary[fiscal_year_id].append(red_flag_dictionary)





for fiscal_year_id in red_flag_4_dictionary:

    visualization_file_name = "data" + os.sep + "cached_generated_multimedia" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "red_flag_4.html"
    spreadsheet_file_name = "data" + os.sep + "cached_generated_reports" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "red_flag_4.xlsx"
    red_flag_id = fiscal_year_id.replace("/", "") + "red_flag_4"
    visualization_dictionary[red_flag_id]["visualization_link"] = visualization_file_name
    visualization_dictionary[red_flag_id]["report_link"] = spreadsheet_file_name
    visualization_dictionary[red_flag_id]['is_image'] = False

    # Check the computed visualization and/or report files are already in existence
    serialization_deserialization_object.set_serialization_file_name(visualization_file_name)
    visualization_file_exists = serialization_deserialization_object.check_file_exists()
    serialization_deserialization_object.set_serialization_file_name(spreadsheet_file_name)
    spreadsheet_file_exists = serialization_deserialization_object.check_file_exists()
    files_exist = (visualization_file_exists and spreadsheet_file_exists)

    if files_exist and recompute_fiscal_year_dictionary[fiscal_year_id] == False:
        continue

    # Reporting on red flag 2 using a spreadsheet
    data = list()
    data.append(field_list_creator_object.get_procurement_party_field_list([]))
    duplicate_email_tracking_set = set() # duplicates emails are being tracked based on the TIN
    duplicate_phone_tracking_set = set() # duplicate phones are also tracked here based on the TIN

    for entity_id in fiscal_year_supplying_entity_dictionary[fiscal_year_id]:
        entity_dictionary = fiscal_year_supplying_entity_dictionary[fiscal_year_id][entity_id]
        same_email_tuple_list = red_flag_4_dictionary[fiscal_year_id]['same_email_pair_set']
        same_phone_tuple_list = red_flag_4_dictionary[fiscal_year_id]['same_phone_pair_set']

        for supplying_entity_tuple in same_email_tuple_list:
            if entity_id in supplying_entity_tuple:
                another_entity_id = supplying_entity_tuple[1] if supplying_entity_tuple.index(entity_id) == 0 else supplying_entity_tuple[0]
                entity_dictionary = fiscal_year_supplying_entity_dictionary[fiscal_year_id][entity_id]
                entity_ext_tin = entity_dictionary['ext_tin']
                another_entity_dictionary = fiscal_year_supplying_entity_dictionary[fiscal_year_id][another_entity_id]
                another_ext_tin = another_entity_dictionary['ext_tin']
                if entity_ext_tin not in duplicate_email_tracking_set:
                    data_list_1 = field_list_creator_object.get_party_data_list(entity_dictionary, [])
                    data.append(data_list_1)
                    duplicate_email_tracking_set.add(entity_ext_tin)
                if another_ext_tin not in duplicate_email_tracking_set:
                    data_list_2 = field_list_creator_object.get_party_data_list(another_entity_dictionary, [])
                    data.append(data_list_2)
                    duplicate_email_tracking_set.add(another_ext_tin)

        for supplying_entity_tuple in same_phone_tuple_list:
            if entity_id in supplying_entity_tuple:
                another_entity_id = supplying_entity_tuple[1] if supplying_entity_tuple.index(entity_id) == 0 else supplying_entity_tuple[0]
                entity_dictionary = fiscal_year_supplying_entity_dictionary[fiscal_year_id][entity_id]
                entity_ext_tin = entity_dictionary['ext_tin']
                another_entity_dictionary = fiscal_year_supplying_entity_dictionary[fiscal_year_id][another_entity_id]
                another_ext_tin = another_entity_dictionary['ext_tin']
                if entity_ext_tin not in duplicate_phone_tracking_set and entity_ext_tin not in duplicate_email_tracking_set:
                    data_list_1 = field_list_creator_object.get_party_data_list(entity_dictionary, [])
                    data.append(data_list_1)
                    duplicate_phone_tracking_set.add(entity_ext_tin)
                if another_ext_tin not in duplicate_phone_tracking_set and another_ext_tin not in duplicate_email_tracking_set:
                    data_list_2 = field_list_creator_object.get_party_data_list(another_entity_dictionary, [])
                    data.append(data_list_2)
                    duplicate_phone_tracking_set.add(another_ext_tin)

    spreadsheet_creator_object = SpreadsheetCreator(spreadsheet_file_name, data)
    spreadsheet_creator_object.create_spreadsheet()

    visualization_markup_object.set_file_name(visualization_file_name)
    visualization_markup_object.get_red_flag_4_visual_markup(red_flag_4_dictionary[fiscal_year_id])
    table_title = "Supplying entities with a shared contact"
    visualization_markup_object.tabulate_red_flag_data(table_title, data)




# Red flag 5: to see tenders with one or more appeals (Requires changes to the schema, add the appeals/Issue/Complaint entity) - handled
#             Get particular fiscal year tenders
#             For every tender, get the appeals and count them

red_flag_5_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    red_flag_5_dictionary[fiscal_year_id] = {"with_x_or_more_appeals":0, "with_x_or_more_appeals_set":set()}
    specific_fiscal_year_award_appeals = fiscal_year_award_appeal_dictionary[fiscal_year_id]
    for award_id in specific_fiscal_year_award_appeals:
        specific_award_appeals = specific_fiscal_year_award_appeals[award_id]
        if len(specific_award_appeals) > 0:
            specific_award_tenders = get_specific_award_tenders(selection_object, query_executor, award_id)
            for tender_id in specific_award_tenders:
                red_flag_5_dictionary[fiscal_year_id]["with_x_or_more_appeals"] += 1
                red_flag_5_dictionary[fiscal_year_id]["with_x_or_more_appeals_set"].add(tender_id)




# Red flag 6: To see tenders with only one bid (Looks like a repeatition of red flag number 2)
#             Get a particular fiscal year tenders
#             for each and every tender bids and count them



red_flag_6_dictionary = {}

for fiscal_year_id in fiscal_year_dictionary:

    calculated_data_file = "data" + os.sep + "calculated_red_flag_data" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "red_flag_6.json"
    serialization_deserialization_object.set_serialization_file_name(calculated_data_file)
    file_exists = serialization_deserialization_object.check_file_exists()

    if file_exists and recompute_fiscal_year_dictionary[fiscal_year_id] == False:
        red_flag_2_dictionary[fiscal_year_id] = json.loads(serialization_deserialization_object.deserialize_from_json())
    else:
        red_flag_6_dictionary[fiscal_year_id] = {"less_than_x_bids":0, "more_than_x_bids":0, "less_than_x_bids_histogram":dict(), "less_than_x_bids_count_histogram":dict(), "more_than_x_bids_histogram":dict()}
        with_less_than_x_bids_count_dictionary = {x:0 for x in range(1, 13)}
        with_less_than_x_bids_set = set()
        specific_fiscal_year_tender_dictionary = fiscal_year_tender_dictionary[fiscal_year_id]

        for tender_id in specific_fiscal_year_tender_dictionary:
            if len(fiscal_year_tender_bid_dictionary[fiscal_year_id][tender_id]) == 1:
                red_flag_6_dictionary[fiscal_year_id]["less_than_x_bids"] += 1
                creation_date = specific_fiscal_year_tender_dictionary[tender_id]["tender_period_start_date"]

                if isinstance(creation_date, str) and len(creation_date) > 0:
                    date_string = creation_date.replace("T", " ").split(".")[0]
                    creation_date_object = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
                    month_key = creation_date_object.strftime("%m")
                    with_less_than_x_bids_count_dictionary[int(month_key)] += 1
                    with_less_than_x_bids_set.add(tender_id)

            else:
                red_flag_6_dictionary[fiscal_year_id]["more_than_x_bids"] += 1
                #red_flag_2_dictionary[fiscal_year_id]["more_than_x_bids_histogram"].add(tender_id) # not of interest for now

        red_flag_6_dictionary[fiscal_year_id]["less_than_x_bids_count_histogram"] = with_less_than_x_bids_count_dictionary
        red_flag_6_dictionary[fiscal_year_id]["less_than_x_bids_set"] = with_less_than_x_bids_set


    red_flag_id = fiscal_year_id.replace("/", "") + "red_flag_6"
    red_flag_dictionary = {"id": red_flag_id, "name": "Tenders with one bid"}
    red_flag_list.append(red_flag_dictionary)
    visualization_dictionary[red_flag_id] = {}
    visualization_dictionary[red_flag_id]['is_image'] = True
    if fiscal_year_id not in fiscal_year_list:
        fiscal_year_list.append(fiscal_year_id)
    if fiscal_year_id not in fiscal_year_red_flag_dictionary:
        fiscal_year_red_flag_dictionary[fiscal_year_id] = list()
        fiscal_year_red_flag_dictionary[fiscal_year_id].append(red_flag_dictionary)
    else:
        fiscal_year_red_flag_dictionary[fiscal_year_id].append(red_flag_dictionary)

    if len(red_flag_6_dictionary[fiscal_year_id]) > 0:
        serialization_deserialization_object.set_serialization_data(red_flag_6_dictionary[fiscal_year_id])
        serialization_deserialization_object.serialize_in_json()


for fiscal_year_id in red_flag_6_dictionary:

    visualization_file_name = "data" + os.sep + "cached_generated_multimedia" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "red_flag_6.jpg"
    spreadsheet_file_name = "data" + os.sep + "cached_generated_reports" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "red_flag_6.xlsx"
    red_flag_id = fiscal_year_id.replace("/", "") + "red_flag_6"
    visualization_dictionary[red_flag_id]["visualization_link"] = visualization_file_name
    visualization_dictionary[red_flag_id]["report_link"] = spreadsheet_file_name

    # visualizing red flag 2,  using a bar graph
    title = fiscal_year_id.replace("/", "-")  + " fiscal year tenders with one bid"
    value_dict = red_flag_6_dictionary[fiscal_year_id]["less_than_x_bids_count_histogram"]
    bar_color = "#007700"
    edge_color = "white"
    x_axis_label = "Month"
    y_axis_label = "Tenders"
    width = 14
    height = 7
    save_path_and_name = visualization_file_name

    bargraph_drawer_object = BarGraphDrawer(value_dict, bar_color, edge_color, x_axis_label, y_axis_label, title, width, height, save_path_and_name)
    bargraph_drawer_object.draw_bar_graph()

    # Reporting on red flag 2 using a spreadsheet
    data = list()
    data.append(field_list_creator_object.get_tender_field_list([]))

    for tender_id in red_flag_6_dictionary[fiscal_year_id]["less_than_x_bids_set"]:
        tender_dictionary = fiscal_year_tender_dictionary[fiscal_year_id][tender_id]
        data_list = field_list_creator_object.get_tender_data_list(tender_dictionary, [])
        data.append(data_list)

    spreadsheet_creator_object = SpreadsheetCreator(spreadsheet_file_name, data)
    spreadsheet_creator_object.create_spreadsheet()



# Red flag 7: To see the top 10 suppliers who are repeatedly the most awarded over 5 years
#             Get the fiscal year suppliers
#             Get the fiscal year awards
#             For each and every supplier, get their awards and count them

red_flag_7_dictionary = {}
fiscal_year_supplying_entity_award_count_dictionary = {}
top_x_winners_configuration = 10
top_x_winners_in_y_years_configuration = 5

for fiscal_year_id in fiscal_year_dictionary:
    fiscal_year_supplying_entity_award_count_dictionary[fiscal_year_id] = {}
    specific_supplying_entity_awards = fiscal_year_supplying_entity_award_dictionary[fiscal_year_id]
    for supplying_entity_id in specific_supplying_entity_awards:
        fiscal_year_supplying_entity_award_count_dictionary[fiscal_year_id][supplying_entity_id] = len(fiscal_year_supplying_entity_award_dictionary[fiscal_year_id][supplying_entity_id])

    red_flag_id = fiscal_year_id.replace("/", "") + "red_flag_7"
    red_flag_dictionary = {"id": red_flag_id, "name": "Top " + str(top_x_winners_configuration) + " supplying entities with the most awards in the last " + str(top_x_winners_in_y_years_configuration) + " years"}
    red_flag_list.append(red_flag_dictionary)
    visualization_dictionary[red_flag_id] = {}
    if fiscal_year_id not in fiscal_year_list:
        fiscal_year_list.append(fiscal_year_id)
    if fiscal_year_id not in fiscal_year_red_flag_dictionary:
        fiscal_year_red_flag_dictionary[fiscal_year_id] = list()
        fiscal_year_red_flag_dictionary[fiscal_year_id].append(red_flag_dictionary)
    else:
        fiscal_year_red_flag_dictionary[fiscal_year_id].append(red_flag_dictionary)

for fiscal_year_id in fiscal_year_dictionary:
    year_supplying_entity_award_count_dictionary = fiscal_year_supplying_entity_award_count_dictionary[fiscal_year_id]
    red_flag_7_dictionary[fiscal_year_id] = dict(sorted(year_supplying_entity_award_count_dictionary.items(), key=lambda item: item[1], reverse=True)) # sorting by value in desc order


for fiscal_year_id in red_flag_7_dictionary:

    visualization_file_name = "data" + os.sep + "cached_generated_multimedia" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "red_flag_7.jpg"
    spreadsheet_file_name = "data" + os.sep + "cached_generated_reports" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "red_flag_7.xlsx"
    red_flag_id = fiscal_year_id.replace("/", "") + "red_flag_7"
    visualization_dictionary[red_flag_id]["visualization_link"] = visualization_file_name
    visualization_dictionary[red_flag_id]["report_link"] = spreadsheet_file_name
    visualization_dictionary[red_flag_id]['is_image'] = True

    top = 10
    count = 0
    y_data_seq = []
    x_data_seq = []
    for k in red_flag_7_dictionary[fiscal_year_id]:
        if count == top:
            break
        supplying_entity_name = fiscal_year_supplying_entity_dictionary[fiscal_year_id][k]['name'].strip()
        name = (supplying_entity_name[:20] + "...") if (len(supplying_entity_name) > 20) else supplying_entity_name
        name = name + " (" + fiscal_year_supplying_entity_dictionary[fiscal_year_id][k]['ext_tin'] + ")"
        y_data_seq.append(name)
        x_data_seq.append(red_flag_7_dictionary[fiscal_year_id][k])
        count += 1
    y_data_seq.reverse()
    x_data_seq.reverse()


    y_label = "Procuring entities"
    x_label = "Tenders"
    title = ""
    horizontal_bar_graph = HorizontalBarGraph(y_data_seq, x_data_seq, y_label, x_label, title, visualization_file_name)
    horizontal_bar_graph.draw_horizontal_bar_graph()

    data = list()
    data.append(field_list_creator_object.get_procurement_party_field_list(["bids won"]))

    count = 0
    for entity_id in red_flag_7_dictionary[fiscal_year_id]:
        if count >= top_x_winners_configuration:
            break
        entity_dictionary = fiscal_year_supplying_entity_dictionary[fiscal_year_id][entity_id]
        award_count = red_flag_7_dictionary[fiscal_year_id][entity_id]
        data_list = field_list_creator_object.get_party_data_list(entity_dictionary, [award_count])
        data.append(data_list)
        count += 1

    spreadsheet_creator_object = SpreadsheetCreator(spreadsheet_file_name, data)
    spreadsheet_creator_object.create_spreadsheet()



# Red flag 8: to see bidders that have never bid before that win a tender
#             Get the fiscal year suppliers (A mapping has been added to the data model fiscal year and suppling entity)
#             Get the supplier bids
#             For each and every supplier, get their awards and count them, if successful awards are equal to bids (sound the alarm)

red_flag_8_set = set()
supplying_entity_exclusion_set = set()
for fiscal_year_id in fiscal_year_dictionary:
    specific_fiscal_year_supplying_entity_bids = fiscal_year_supplying_entity_bid_dictionary[fiscal_year_id]
    specific_fiscal_year_supplying_entity_awards = fiscal_year_supplying_entity_award_dictionary[fiscal_year_id]
    for supplying_entity_id in specific_fiscal_year_supplying_entity_bids:
        bid_count = len(specific_fiscal_year_supplying_entity_bids[supplying_entity_id])
        award_count = len(specific_fiscal_year_supplying_entity_awards[supplying_entity_id])
        if bid_count == award_count and bid_count == 1:
            if supplying_entity_id in red_flag_8_set:
                red_flag_8_set.remove(supplying_entity_id)
                supplying_entity_exclusion_set.add(supplying_entity_id)
            else:
                if supplying_entity_id not in supplying_entity_exclusion_set:
                    red_flag_8_set.add(supplying_entity_id)

red_flag_id = fiscal_year_id.replace("/", "") + "red_flag_8"
red_flag_dictionary = {"id": red_flag_id, "name": "Supplying entities that have never bid before that win a tender"}
red_flag_list.append(red_flag_dictionary)
visualization_dictionary[red_flag_id] = {}
if fiscal_year_id not in fiscal_year_list:
    fiscal_year_list.append(fiscal_year_id)
if fiscal_year_id not in fiscal_year_red_flag_dictionary:
    fiscal_year_red_flag_dictionary[fiscal_year_id] = list()
    fiscal_year_red_flag_dictionary[fiscal_year_id].append(red_flag_dictionary)
else:
    fiscal_year_red_flag_dictionary[fiscal_year_id].append(red_flag_dictionary)

visualization_file_name = "data" + os.sep + "cached_generated_multimedia" + os.sep + "all_time" + os.sep + "red_flag_8.jpg"
spreadsheet_file_name = "data" + os.sep + "cached_generated_reports" + os.sep + "all_time" + os.sep + "red_flag_8.xlsx"
red_flag_id = fiscal_year_id.replace("/", "") + "red_flag_8"
visualization_dictionary[red_flag_id]["visualization_link"] = visualization_file_name
visualization_dictionary[red_flag_id]["report_link"] = spreadsheet_file_name
visualization_dictionary[red_flag_id]['is_image'] = False

data = list()
data.append(field_list_creator_object.get_procurement_party_field_list([]))

for supplying_entity_id in red_flag_8_set:
    if supplying_entity_id in fiscal_year_supplying_entity_dictionary[fiscal_year_id]:
        entity_dictionary = fiscal_year_supplying_entity_dictionary[fiscal_year_id][supplying_entity_id]
        data_list = field_list_creator_object.get_party_data_list(entity_dictionary, [])
        data.append(data_list)

spreadsheet_creator_object = SpreadsheetCreator(spreadsheet_file_name, data)
spreadsheet_creator_object.create_spreadsheet()

visualization_markup_object.set_file_name(visualization_file_name)
visualization_markup_object.get_red_flag_9_visual_markup({"Had never bid before but win a tender": len(red_flag_8_set)})
if len(data) > 0:
    table_title = "Supplying entities that had never bid before but win a tender"
    visualization_markup_object.tabulate_red_flag_data(table_title, data)



# Red flag 9: to see bidders who have received more than two direct bidding contracts from one procuring entity in a single fiscal year
#             Get the fiscal year suppliers
#             Get each and every procuring entity's "direct contract awards"
#             For each and every supplier, get their direct contracts and count them, check if direct contracts exceed the configuration of 2 (sound the alarm if yes)

for fiscal_year_id in fiscal_year_dictionary:
    red_flag_id = fiscal_year_id.replace("/", "") + "red_flag_9"
    red_flag_dictionary = {"id": red_flag_id, "name": "Bidders who have received more than two direct bidding contracts from one procuring entity"}
    red_flag_list.append(red_flag_dictionary)
    visualization_dictionary[red_flag_id] = {}
    if fiscal_year_id not in fiscal_year_list:
        fiscal_year_list.append(fiscal_year_id)
    if fiscal_year_id not in fiscal_year_red_flag_dictionary:
        fiscal_year_red_flag_dictionary[fiscal_year_id] = list()
        fiscal_year_red_flag_dictionary[fiscal_year_id].append(red_flag_dictionary)
    else:
        fiscal_year_red_flag_dictionary[fiscal_year_id].append(red_flag_dictionary)


red_flag_9_label_count_dictionary = {}
red_flag_9_report_data_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    red_flag_9_dictionary[fiscal_year_id] = {"count": 0, "set": set()}
    fiscal_year_label = fiscal_year_dictionary[fiscal_year_id]["start_date"][:4] + " - " + fiscal_year_dictionary[fiscal_year_id]["end_date"][:4]
    red_flag_9_label_count_dictionary[fiscal_year_label] = red_flag_9_dictionary[fiscal_year_id]["count"]
    red_flag_9_report_data_dictionary[fiscal_year_label] = red_flag_9_dictionary[fiscal_year_id]["set"]

    visualization_file_name = "data" + os.sep + "cached_generated_multimedia" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "red_flag_9.html"
    spreadsheet_file_name = "data" + os.sep + "cached_generated_reports" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "red_flag_9.xlsx"
    red_flag_id = fiscal_year_id.replace("/", "") + "red_flag_9"
    visualization_dictionary[red_flag_id]["visualization_link"] = visualization_file_name
    visualization_dictionary[red_flag_id]["report_link"] = spreadsheet_file_name
    visualization_dictionary[red_flag_id]['is_image'] = False

    data = list()
    data.append(field_list_creator_object.get_procurement_party_field_list(["Procuring entity tin", "Procuring entity name"]))

    for procuring_entity_id, procuring_entity_tin, supplying_entity_tin in red_flag_9_dictionary[fiscal_year_id]["set"]:
        supplying_entity_dictionary = fiscal_year_supplying_entity_dictionary[fiscal_year_id][supplying_entity_tin]
        procuring_entity_dictionary = fiscal_year_procuring_entity_dictionary[fiscal_year_id][procuring_entity_id]
        procuring_entity_name = procuring_entity_dictionary['name']
        data_list = field_list_creator_object.get_party_data_list(supplying_entity_dictionary, [procuring_entity_tin, procuring_entity_name])
        data.append(data_list)

    spreadsheet_creator_object = SpreadsheetCreator(spreadsheet_file_name, data)
    spreadsheet_creator_object.create_spreadsheet()

    visualization_markup_object.set_file_name(visualization_file_name)
    visualization_markup_object.get_red_flag_9_visual_markup({"more than two direct contracts": red_flag_9_dictionary[fiscal_year_id]["count"]})
    if len(data) > 0:
        table_title = "Supplying entities with more than two direct contracts"
        visualization_markup_object.tabulate_red_flag_data(table_title, data)







# Red flag 10: to see bidders who always bid and win
#              Get the fiscal year suppliers
#              Get the supplier bids
#              For each and every supplier, get their awards and count them, if awards are equal to bids, this time can be more than one (sound the alarm)

red_flag_10_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    red_flag_10_dictionary[fiscal_year_id] = set()
    specific_fiscal_year_supplying_entity_bids = fiscal_year_supplying_entity_bid_dictionary[fiscal_year_id]
    specific_fiscal_year_supplying_entity_awards = fiscal_year_supplying_entity_award_dictionary[fiscal_year_id]
    for supplying_entity_id in specific_fiscal_year_supplying_entity_bids:
        bid_count = len(specific_fiscal_year_supplying_entity_bids[supplying_entity_id])
        award_count = len(specific_fiscal_year_supplying_entity_awards[supplying_entity_id])
        if bid_count == award_count and award_count > 1:
            red_flag_10_dictionary[fiscal_year_id].add(supplying_entity_id)

    red_flag_id = fiscal_year_id.replace("/", "") + "red_flag_10"
    red_flag_dictionary = {"id": red_flag_id, "name": "Supplying entities which always bid and win"}
    red_flag_list.append(red_flag_dictionary)
    visualization_dictionary[red_flag_id] = {}
    if fiscal_year_id not in fiscal_year_list:
        fiscal_year_list.append(fiscal_year_id)
    if fiscal_year_id not in fiscal_year_red_flag_dictionary:
        fiscal_year_red_flag_dictionary[fiscal_year_id] = list()
        fiscal_year_red_flag_dictionary[fiscal_year_id].append(red_flag_dictionary)
    else:
        fiscal_year_red_flag_dictionary[fiscal_year_id].append(red_flag_dictionary)

for fiscal_year_id in red_flag_10_dictionary:

    visualization_file_name = "data" + os.sep + "cached_generated_multimedia" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "red_flag_10.jpg"
    spreadsheet_file_name = "data" + os.sep + "cached_generated_reports" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "red_flag_10.xlsx"
    red_flag_id = fiscal_year_id.replace("/", "") + "red_flag_10"
    visualization_dictionary[red_flag_id]["visualization_link"] = visualization_file_name
    visualization_dictionary[red_flag_id]["report_link"] = spreadsheet_file_name
    visualization_dictionary[red_flag_id]['is_image'] = False

    data = list()
    data.append(field_list_creator_object.get_procurement_party_field_list([]))

    for entity_id in red_flag_10_dictionary[fiscal_year_id]:
        entity_dictionary = fiscal_year_supplying_entity_dictionary[fiscal_year_id][entity_id]
        data_list = field_list_creator_object.get_party_data_list(entity_dictionary, [])
        data.append(data_list)

    spreadsheet_creator_object = SpreadsheetCreator(spreadsheet_file_name, data)
    spreadsheet_creator_object.create_spreadsheet()

    visualization_markup_object.set_file_name(visualization_file_name)
    visualization_markup_object.get_red_flag_9_visual_markup({"Always bid and win": len(red_flag_10_dictionary[fiscal_year_id])})
    if len(data) > 0:
        table_title = "Supplying entities which always bid and win"
        visualization_markup_object.tabulate_red_flag_data(table_title, data)


# Red flag 11: to see procuring entities whose plan submissions have a late submission date (Plan submissions need to be handled in the model)
#              Get every procuring entity's fiscal year plan submission mapped to the plan procurement stage
#              for every procuring entity, check for any late submissions

submission_delay_configuration = 0 # configuration stored in the database with a special name
red_flag_11_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    fiscal_year_start_date = fiscal_year_dictionary[fiscal_year_id]["start_date"]
    fiscal_year_start_date_and_time = fiscal_year_start_date + " " + "00:00:00"
    red_flag_11_dictionary[fiscal_year_id] = {"late_submission_count":0, "on_time_submission":0, "late_submission_set": set()}
    year_procuring_entity_plans = fiscal_year_procuring_entity_plan_dictionary[fiscal_year_id]
    for procuring_entity_id in year_procuring_entity_plans:
        plan_dictionary = year_procuring_entity_plans[procuring_entity_id]
        for plan_id in plan_dictionary:
            submission_date_and_time = plan_dictionary[plan_id]["submission_date_and_time"]
            formated_submission_date_and_time = str(submission_date_and_time).split("T")[0].split(" ")[0]

            time_delta = (datetime.strptime(fiscal_year_start_date.replace("-", "/"), "%Y/%m/%d") - datetime.strptime(formated_submission_date_and_time.replace("-", "/"), "%Y/%m/%d")) / 86400
            day_difference = (((time_delta.days * 24) + (time_delta.total_seconds()/3600)) / 24)

            if day_difference > submission_delay_configuration:
                red_flag_11_dictionary[fiscal_year_id]["late_submission_count"] += 1
                red_flag_11_dictionary[fiscal_year_id]["late_submission_set"].add(procuring_entity_id)
            else:
                red_flag_11_dictionary[fiscal_year_id]["on_time_submission"] += 1

    red_flag_id = fiscal_year_id.replace("/", "") + "red_flag_11"
    red_flag_dictionary = {"id": red_flag_id, "name": "Procuring entities with late plan submissions"}
    red_flag_list.append(red_flag_dictionary)
    visualization_dictionary[red_flag_id] = {}
    if fiscal_year_id not in fiscal_year_list:
        fiscal_year_list.append(fiscal_year_id)
    if fiscal_year_id not in fiscal_year_red_flag_dictionary:
        fiscal_year_red_flag_dictionary[fiscal_year_id] = list()
        fiscal_year_red_flag_dictionary[fiscal_year_id].append(red_flag_dictionary)
    else:
        fiscal_year_red_flag_dictionary[fiscal_year_id].append(red_flag_dictionary)


for fiscal_year_id in red_flag_11_dictionary:

    visualization_file_name = "data" + os.sep + "cached_generated_multimedia" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "red_flag_11.jpg"
    spreadsheet_file_name = "data" + os.sep + "cached_generated_reports" + os.sep + fiscal_year_id.replace("/", "-") + os.sep + "red_flag_11.xlsx"
    red_flag_id = fiscal_year_id.replace("/", "") + "red_flag_11"
    visualization_dictionary[red_flag_id]["visualization_link"] = visualization_file_name
    visualization_dictionary[red_flag_id]["report_link"] = spreadsheet_file_name
    visualization_dictionary[red_flag_id]['is_image'] = False

    data = list()
    data.append(field_list_creator_object.get_procurement_party_field_list([]))

    for entity_id in fiscal_year_procuring_entity_dictionary[fiscal_year_id]:
        if red_flag_11_dictionary[fiscal_year_id]["late_submission_count"] == 0:
            break
        if entity_id not in red_flag_11_dictionary[fiscal_year_id]["late_submission_set"]:
            continue
        entity_dictionary = fiscal_year_procuring_entity_dictionary[fiscal_year_id][entity_id]
        data_list = field_list_creator_object.get_party_data_list(entity_dictionary, [])
        data.append(data_list)

    spreadsheet_creator_object = SpreadsheetCreator(spreadsheet_file_name, data)
    spreadsheet_creator_object.create_spreadsheet()

    visualization_markup_object.set_file_name(visualization_file_name)
    visualization_markup_object.get_red_flag_9_visual_markup({"Have a late submission plan": red_flag_11_dictionary[fiscal_year_id]["late_submission_count"]})
    if len(data) > 0:
        table_title = "Procuring entities with late plan submissions"
        visualization_markup_object.tabulate_red_flag_data(table_title, data)




# This part of the source coede is responsble for the creattion of the user UI, and the issues of the UI creation have been eparated from the issues of the application logic
# With this is the use of the dashboard markup object shown below
dashboard_markup = DashboardMarkup("dashboard.html")
dashboard_markup.set_fiscal_year_list(fiscal_year_list)
dashboard_markup.set_red_flag_list(red_flag_list)
dashboard_markup.set_fiscal_year_red_flag_map(fiscal_year_red_flag_dictionary)
dashboard_markup.set_visualization_dictionary(visualization_dictionary)
dashboard_html_page = dashboard_markup.get_dahsboard_html_page("Red flags dashboard")
