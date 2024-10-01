import os

from includes.database_connection import DatabaseConnection
from crud.ddl import DDL
from crud.selection import Select
#from crud.insert import Insert
#from crud.update import Update
#from crud.delete import Delete
from includes.date_time import DateTimeProvider
from includes.country import Country
from includes.country_phone_code import Country
from includes.business_logic_functions import *
from datetime import datetime
from includes.visualization.matplotlib_bar_graph import *
from includes.visualization.matplotlib_pie_chart import *
from includes.report_generation.spreadsheet_creator import *


# Create CRUD ops objects
# insert_object = Insert("Umucyo insertion object 1")
selection_object = Select("Umucyo selection object 1")
#deletion_object = Delete("Umucyo deletion object 1")
#update_object = Update("Umucyo update object 1")

# Client continent
client_continent = "Africa"

# Client country name
client_country_name = "Rwanda"

# Client capital city
client_capital_city = "Kigali"

# Date and timezone relative to a particular country
timezone_string = client_continent + os.sep + client_capital_city
date_and_time_object = DateTimeProvider(timezone_string)



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
number_of_fiscal_years = 4

# Get all available fiscal years.
fiscal_year_dictionary = get_fiscal_years(selection_object, query_executor) # ops: select distinct fiscal years from the planning table and all the other tables in which the fiscal year field appears
print("Retrieving Fiscal year list\n")
for fiscal_year_key in fiscal_year_dictionary:
    print(fiscal_year_key)
print("\n")

# Get a specific fiscal year procuring entities
fiscal_year_procuring_entity_dictionary = {}
procuring_entity_dictionary = procurement_actor(selection_object, query_executor, "{buyer}")
for fiscal_year_id in fiscal_year_dictionary:
    fiscal_year_procuring_entity_dictionary[fiscal_year_id] = procuring_entity_dictionary
    # Ops: you actually just select all procuring entities and assume that they appear every fiscal year in this case

print()
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



# Get a specific fiscal year supplying entities
fiscal_year_supplying_entity_dictionary = {}
supplying_entity_dictionary = procurement_actor(selection_object, query_executor, "{supplier}")
for fiscal_year_id in fiscal_year_dictionary:
    fiscal_year_supplying_entity_dictionary[fiscal_year_id] = supplying_entity_dictionary
    #print()
    # ops: check them by whether they have atleast a single bid every fiscal year to qualify them to appear in this dictionary's entries

print()
print("\nSupplying entity list\n")
count = 0
for fiscal_year_id in fiscal_year_dictionary:
    for supplying_entity_id in fiscal_year_supplying_entity_dictionary[fiscal_year_id]:
        print(fiscal_year_supplying_entity_dictionary[fiscal_year_id][supplying_entity_id]['name'])
        if count == 14:
            break;
        count += 1
    if count == 14:
        break;



# (important for red flag 1)
# Get a specific fiscal year's procuring entities' procuring plans, this is sufficient to calculate red flag 1
# The dictionary on the next line is sufficient to handle the information needed to calculate red flag 1 and consequently visualize it
fiscal_year_procuring_entity_plan_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    fiscal_year_procuring_entity_plan_dictionary[fiscal_year_id] = {}
    procuring_entity_dictionary = fiscal_year_procuring_entity_dictionary[fiscal_year_id]
    print(fiscal_year_id + ": " + str(len(fiscal_year_procuring_entity_dictionary[fiscal_year_id])))
    for procuring_entity_id in procuring_entity_dictionary:
        legacy_id = procuring_entity_dictionary[procuring_entity_id]['legacy_id']
        party_id = legacy_id
        procuring_entity_id = legacy_id
        # The legacy id is used to reference the procuring enttty id in the planning table, so use use it to key a particular entity's plans. In the planning rable, it's called ext_pe_code
        fiscal_year_procuring_entity_plan_dictionary[fiscal_year_id][procuring_entity_id] = specific_party_fiscal_year_plans(selection_object, query_executor, fiscal_year_id, party_id)

count = 0
print()
print("\n%-70s  %-s\n" % ("Procuring actor legacy id", "Plan"))
for fiscal_year_id in fiscal_year_dictionary:
    procuring_entity_dictionary = fiscal_year_procuring_entity_dictionary[fiscal_year_id]
    for procuring_entity_id in procuring_entity_dictionary:
        legacy_id = procuring_entity_dictionary[procuring_entity_id]['legacy_id']
        plan_dictionary = fiscal_year_procuring_entity_plan_dictionary[fiscal_year_id][legacy_id]
        for plan_id in plan_dictionary:
            ext_pe_code = plan_dictionary[plan_id]['ext_pe_code']
            plan_count = len(plan_dictionary)
            print(" %-70s %-3s" % (ext_pe_code, str(plan_count)))
            break;
        if count == 14:
            break;
        count += 1
    if count == 1:
        break;


# (Important for red flag 4)
# Get fiscal year supplying entities contacts
fiscal_year_supplying_entity_contact_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    fiscal_year_supplying_entity_contact_dictionary[fiscal_year_id] = {}
    specific_fiscal_year_supplying_entities = fiscal_year_supplying_entity_dictionary[fiscal_year_id]
    for supplying_entity_id in specific_fiscal_year_supplying_entities:
        fiscal_year_supplying_entity_contact_dictionary[fiscal_year_id][supplying_entity_id] = {}



# Get a specific fiscal year tenders, for the last y number of years
# Get a specific tender's bids
fiscal_year_tender_dictionary = {}
tender_bid_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    fiscal_year_tender_dictionary[fiscal_year_id] = {}
    # This has sufficient information to calculate red flag number two
    for tender_id in fiscal_year_tender_dictionary[fiscal_year_id]:
        tender_bid_dictionary[tender_id] = {}


tender_bid_dictionary = {}
for procuring_entity_id in procuring_entity_tender_dictionary:
    for tender_id in procuring_entity_tender_dictionary[procuring_entity_id]:
        tender_bid_dictionary[tender_id] = {}


# Get a specific fiscal year bids
fiscal_year_bid_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    fiscal_year_bid_dictionary[fiscal_year_id] = {}



# Get a specific fiscal year tenders' bids
# This has sufficient information to calculate red flag number 2, 6, 8 (in conjunction with awards) and all such variants
fiscal_year_tender_bid_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    fiscal_year_tender_bid_dictionary[fiscal_year_id] = {}
    for tender_id in fiscal_year_tender_dictionary[fiscal_year_id]:
        specific_tender_bid_dictionary = {}
        new_specific_tender_bid_dictionary = {}
        for bid_id in specific_tender_bid_dictionary:
            if bid_id in fiscal_year_bid_dictionary[fiscal_year_id]:
                new_specific_tender_bid_dictionary[bid] = fiscal_year_bid_dictionary[fiscal_year_id][bid_id]
        fiscal_year_tender_bid_dictionary[fiscal_year_id][tender_id] = new_specific_tender_bid_dictionary

# Get a specific fiscal year tender fee payments
# This is intended to help in the calculation of the third red flag
fiscal_year_tender_payment_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    fiscal_year_tender_payment_dictionary[fiscal_year_id] = {}
    for tender_id in fiscal_year_tender_dictionary[fiscal_year_id]:
        specific_tender_payment = {}
        fiscal_year_tender_payment_dictionary[fiscal_year_id][tender_id] = specific_tender_payment


# Get a specific procuring entity's tenders for a given fiscal year
procuring_entity_tender_dictionary = {}
for procuring_entity_id in procuring_entity_dictionary:
    procuring_entity_tender_dictionary[procuring_entity_id] = {}


# Get a specific fiscal year supplying entitys' bids
fiscal_year_supplying_entity_bid_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    fiscal_year_supplying_entity_bid_dictionary[fiscal_year_id] = {}
    specific_fiscal_year_supplying_entity_dictionary = fiscal_year_supplying_entity_dictionary[fiscal_year_id] # Maybe use all the supplying entities if the year mappings are not sufficient

    for supplying_entity_id in specific_fiscal_year_supplying_entity_dictionary: # Maybe loop through all the supplying entities if the year mappings are not sufficient/available
        specific_supplying_entity_bid_dictionary = get_specific_supplying_entity_bids(selection_object, query_executor, supplying_entity_id)
        new_specific_supplying_entity_bid_dictionary = {}
        for bid_id in specific_supplying_entity_bid_dictionary:
            if bid_id in fiscal_year_bid_dictionary[fiscal_year_id]:
                new_specific_supplying_entity_bid_dictionary[bid_id] = fiscal_year_bid_dictionary[fiscal_year_id][bid_id]
        fiscal_year_supplying_entity_bid_dictionary[fiscal_year_id][supplying_entity_id] = new_specific_supplying_entity_bid_dictionary


# Get a specific fiscal year awards
fiscal_year_award_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    fiscal_year_award_dictionary[fiscal_year_id] = get_specific_fiscal_year_awards(selection_object, query_executor, fiscal_year_id)

# Get a fiscal year supplying entity awards
fiscal_year_supplying_entity_award_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    fiscal_year_supplying_entity_award_dictionary[fiscal_year_id] = {}
    for supplying_entity_id in fiscal_year_supplying_entity_dictionary[fiscal_year_id]:
        specific_supplying_entity_awards = get_specific_supplying_entity_awards(selection_object, query_executor, supplying_entity_id)
        new_specific_supplying_entity_awards = {}
        for award_id in specific_supplying_entity_awards:
            if award_id in fiscal_year_award_dictionary[fiscal_year_id]:
                new_specific_supplying_entity_awards[award_id] = fiscal_year_award_dictionary[fiscal_year_id][award_id]
        fiscal_year_supplying_entity_award_dictionary[fiscal_year_id][supplying_entity_id] = new_specific_supplying_entity_awards


# Get fiscal year procuring entity award
fiscal_year_procuring_entity_award_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    fiscal_year_procuring_entity_award_dictionary[fiscal_year_id] = {}
    for procuring_entity_id in fiscal_year_procuring_entity_dictionary[fiscal_year_id]:
        specific_procuring_entity_awards = get_specific_procuring_entity_awards(selection_object, query_executor, procuring_entity_id)
        new_specific_procuring_entity_awards = {}
        for award_id in specific_procuring_entity_awards:
            if award_id in fiscal_year_award_dictionary[fiscal_year_id]:
                new_specific_procuring_entity_awards[award_id] = fiscal_year_award_dictionary[fiscal_year_id][award_id]
        fiscal_year_procuring_entity_award_dictionary[fiscal_year_id][procuring_entity_id] = new_specific_procuring_entity_awards


# Get the fiscal year procuring entity supplying entity awards, awards given by procuring entities to given certain supplying entities in the selected fiscal years
configuration_number_of_direct_contracts = 2;
cndc = configuration_number_of_direct_contracts
red_flag_9_dictionary = {}
fiscal_year_procuring_entity_supplying_entity_award_dictionary = {}
for fiscal_year_id in fiscal_year_procuring_entity_award_dictionary:
    fiscal_year_procuring_entity_supplying_entity_award_dictionary[fiscal_year_id] = {}
    red_flag_9_dictionary[fiscal_year_id] = {"count": 0, "set": set()}
    for procuring_entity_id in fiscal_year_procuring_entity_award_dictionary[fiscal_year_id]:
        fiscal_year_procuring_entity_supplying_entity_award_dictionary[fiscal_year_id][procuring_entity_id] = {}
        specific_procuring_entity_awards = fiscal_year_procuring_entity_award_dictionary[fiscal_year_id][procuring_entity_id]
        for award_id in specific_procuring_entity_awards:
            specific_award_supplying_entities = get_specific_award_supplying_entities(selection_object, query_executor, award_id)
            for supplying_entity_id in specific_award_supplying_entities:
                if supplying_entity_id in fiscal_year_procuring_entity_supplying_entity_award_dictionary[fiscal_year_id][procuring_entity_id]:
                    fiscal_year_procuring_entity_supplying_entity_award_dictionary[fiscal_year_id][procuring_entity_id][supplying_entity_id].add(award_id)
                    direct_contract_count = len(fiscal_year_procuring_entity_supplying_entity_award_dictionary[fiscal_year_id][procuring_entity_id][supplying_entity_id])

                    if direct_contract_count > cndc and direct_contract_count < (cndc + 2):
                        red_flag_9_dictionary[fiscal_year_id]["count"] += 1
                        red_flag_9_dictionary[fiscal_year_id]["set"].add((procuring_entity_id, supplying_entity_id))
                else:
                    fiscal_year_procuring_entity_supplying_entity_award_dictionary[fiscal_year_id][procuring_entity_id][supplying_entity_id] = set()
                    fiscal_year_procuring_entity_supplying_entity_award_dictionary[fiscal_year_id][procuring_entity_id][supplying_entity_id].add(award_id)



# Get the F fiscal year award appeals, this should help in calculating red flag 5
fiscal_year_award_appeal_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    specific_fiscal_year_awards = fiscal_year_award_dictionary[fiscal_year_id]
    for award_id in specific_fiscal_year_awards:
        specific_award_appeals = get_specific_award_appeals(selection_object, query_executor, award_id)
        if len(specific_award_appeals) == 0: # one can as well use both of them, instead of one
            specific_award_tenders = get_specific_award_tenders(selection_object, query_executor, award_id)
            appeal_dictionary = {}
            for tender_id in specific_award_tenders:
                specific_tender_appeals = get_specific_tender_appeals(selection_object, query_executor, tender_id)
                for appeal_id in specific_tender_appeals:
                    appeal_dictionary[appeal_id] = specific_tender_appeals[appeal_id]
            fiscal_year_award_appeal_dictionary[award_id] = appeal_dictionary
        else:
            fiscal_year_award_appeal_dictionary[award_id] = specific_award_appeals


# Get a specific fiscal year tender award(s)
fiscal_year_tender_award_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    fiscal_year_tender_award_dictionary[fiscal_year_id] = {}
    for tender_id in fiscal_year_tender_dictionary[fiscal_year_id]:
        specific_tender_awards = get_specific_tender_awards(selection_object, query_executor, tender_id)
        new_specific_tender_awards = {}
        for award_id in specific_tender_awards:
            if award_id in fiscal_year_award_dictionary[fiscal_year_id]:
                new_specific_tender_awards[award_id] = fiscal_year_award_dictionary[fiscal_year_id][award_id]
        fiscal_year_tender_award_dictionary[fiscal_year_id][tender_id] = new_specific_tender_awards





# sprint tasks -
# Developing a data migration facility to the corresponding tables (7 days),
# developing each red flag's logic (3 days),
# changing the visualization library to python (4), or react
# visualizing each red flag and adding the corresponding report generation logic (3 days)
# Develop and add alerts into the system 7 days
# System technical report writing (run along everything)  2 days


#########################################################################################################
#  Start work on the different red flags in some construct, a class module perhaps or function module   #
#########################################################################################################



# Red flag 1: Procuring entities that did not submit their procurement plans
#             get the procurement stages of every fiscal year, and then pick out the planning stage
#             get the procuring entities' procurement stages and select out the planning stage (model re-adjusted)

red_flag_1_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    red_flag_1_dictionary[fiscal_year_id] = {"without_a_paln":0, "with_a_plan":0, "without_a_plan_set":set(), "with_a_plan_set":set()}
    specific_fiscal_year_procuring_entity_dictionary = fiscal_year_procuring_entity_dictionary[fiscal_year_id]
    for procuring_entity_id in specific_fiscal_year_procuring_entity_dictionary:
        if len(fiscal_year_procuring_entity_plan_dictionary[fiscal_year_id][procuring_entity_id]) == 0:
            red_flag_1_dictionary[fiscal_year_id]["without_a_paln"] += 1
            red_flag_1_dictionary[fiscal_year_id]["without_a_plan_set"].add(procuring_entity_id)
        else:
            red_flag_1_dictionary[fiscal_year_id]["with_a_plan"] += 1
            #red_flag_1_dictionary[fiscal_year_id]["with_a_plan_set"].add(procuring_entity_id) # not of interest for now



# Red flag 2: Tender has less than three bids (not a closed tender)
#             Get the particular fiscal year tenders
#             Get the fiscal year tender bids

red_flag_2_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    red_flag_2_dictionary[fiscal_year_id] = {"less_than_three_bids":0, "more_than_three_bids":0, "less_than_three_bids_set":set(), "more_than_three_bids_sets":set()}
    specific_fiscal_year_tender_dictionary = fiscal_year_tender_dictionary[fiscal_year_id]
    for tender_id in specific_fiscal_year_tender_dictionary:
        if len(fiscal_year_tender_bid_dictionary[fiscal_year_id][tender_id]) < 3:
            red_flag_2_dictionary[fiscal_year_id]["less_than_three_bids"] += 1
            red_flag_2_dictionary[fiscal_year_id]["less_than_three_bids_set"].add(tender_id)
        else:
            red_flag_2_dictionary[fiscal_year_id]["more_than_three_bids"] += 1
            #red_flag_2_dictionary[fiscal_year_id]["more_than_three_bids_sets"].add(tender_id) # not of interest for now



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

red_flag_2_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    red_flag_2_dictionary[fiscal_year_id] = {"same_email":0, "same_phone":0, "same_email_pair_set": set(), "same_phone_pair_set": set()}
    specific_supplying_entities = fiscal_year_supplying_entity_contact_dictionary[fiscal_year_id]
    for supplying_entity_id in specific_supplying_entities:
        for another_supplying_entity_id in specific_supplying_entities:
            if supplying_entity_id == specific_supplying_entities:
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
                    phone_number = supplying_entity_contacts[contact_key]["value"]
            for contact_key in another_supplying_entity_contacts:
                contact_name = another_supplying_entity_contacts[contact_key]["name"]
                if contact_name.lower()[:5] == "email":
                    another_email_address = another_supplying_entity_contacts[contact_key]["value"]
                if contact_name.lower() == "phone":
                    another_phone_number = another_supplying_entity_contacts[contact_key]["value"]

            if len(email_address) > 0 and email_address.strip() == another_email_address.strip():
                red_flag_2_dictionary[fiscal_year_id]["same_email"] += 1
                red_flag_2_dictionary[fiscal_year_id]["same_email"].add(zip(supplying_entity_id, another_supplying_entity_id)) # set of tuples
            if len(phone) > 0 and phone.strip() == another_phone.strip():
                red_flag_2_dictionary[fiscal_year_id]["same_phone"] += 1
                red_flag_2_dictionary[fiscal_year_id]["same_phone"].add(zip(supplying_entity_id, another_supplying_entity_id))




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
    red_flag_6_dictionary[fiscal_year_id] = {"with_one_bid":0, "more_than_one_bid":0, "with_one_bid_set":set(), "more_than_one_bids_set":set()}
    specific_fiscal_year_tender_dictionary = fiscal_year_tender_dictionary[fiscal_year_id]
    for tender_id in specific_fiscal_year_tender_dictionary:
        if len(fiscal_year_tender_bid_dictionary[fiscal_year_id][tender_id]) == 1:
            red_flag_6_dictionary[fiscal_year_id]["with_one_bid"] += 1
            red_flag_6_dictionary[fiscal_year_id]["with_one_bid_set"].add(tender_id)
        else:
            red_flag_6_dictionary[fiscal_year_id]["more_than_one_bid"] += 1
            #red_flag_6_dictionary[fiscal_year_id]["more_than_one_bids_set"].add(tender_id) # not of interest for now



# Red flag 7: To see the top 10 suppliers who have are repeatedly the most awarded over 5 years
#             Get the fiscal year suppliers
#             Get the fiscal year awards
#             For each and every supplier, get their awards and count them

red_flag_7_dictionary = {}
fiscal_year_supplying_entity_award_count_dicitionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    fiscal_year_supplying_entity_award_count_dicitionary[fiscal_year_id] = {}
    specific_supplying_entity_awards = fiscal_year_supplying_entity_award_dictionary[fiscal_year_id]
    for supplying_entity_id in specific_supplying_entity_awards:
        fiscal_year_supplying_entity_award_count_dicitionary[fiscal_year_id][supplying_entity_id] = len(fiscal_year_supplying_entity_award_dictionary[fiscal_year_id][supplying_entity_id])
for fiscal_year_id in fiscal_year_dictionary:
    year_supplying_entity_award_count_dictionary = fiscal_year_supplying_entity_award_count_dicitionary[fiscal_year_id]
    red_flag_7_dictionary[fiscal_year_id] = dict(sorted(year_supplying_entity_award_count_dictionary.items(), key=lambda item: item[1], reverse=True)) # sorting by value in desc order



# Red flag 8: to see bidders that have never bid before that win a tender
#             Get the fiscal year suppliers (A mapping has been added to the data model fiscal year and suppling entity)
#             Get the supplier bids
#             For each and every supplier, get their awards and count them, if successful awards are equal to bids (sound the alarm)

red_flag_10_set = set()
supplying_entity_exclusion_set = set()
for fiscal_year_id in fiscal_year_dictionary:
    specific_fiscal_year_supplying_entity_bids = fiscal_year_supplying_entity_bid_dictionary[fiscal_year_id]
    specific_fiscal_year_supplying_entity_awards = fiscal_year_supplying_entity_award_dictionary[fiscal_year_id]
    for supplying_entity_id in specific_fiscal_year_supplying_entity_bids:
        bid_count = len(specific_fiscal_year_supplying_entity_bids[supplying_entity_id])
        award_count = len(specific_fiscal_year_supplying_entity_awards[supplying_entity_id])
        if bid_count == award_count and bid_count == 1:
            if supplying_entity_id in red_flag_10_set:
                red_flag_10_set.pop(supplying_entity_id)
                supplying_entity_exclusion_set.add(supplying_entity_id)
            else:
                if supplying_entity_id not in supplying_entity_exclusion_set:
                    red_flag_10_set.add(supplying_entity_id)



# Red flag 9: to see bidders who have received more than two direct bidding contracts from one procuring entity in a single fiscal year
#             Get the fiscal year suppliers
#             Get each and every procuring entity's "direct contract awards"
#             For each and every supplier, get their direct contracts and count them, check if direct contracts exceed the configuration of 2 (sound the alarm if yes)

red_flag_9_label_count_dictionary = {}
red_flag_9_report_data_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    red_flag_9_dictionary[fiscal_year_id] = {"count": 0, "set": set()}
    fiscal_year_label = fiscal_year_dictionary[fiscal_year_id]["start_date"][:4] + " - " + fiscal_year_dictionary[fiscal_year_id]["end_date"][:4]
    red_flag_9_label_count_dictionary[fiscal_year_label] = red_flag_9_dictionary[fiscal_year_id]["count"]
    red_flag_9_report_data_dictionary[fiscal_year_label] = red_flag_9_dictionary[fiscal_year_id]["set"]



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
        if bid_count == award_count:
            red_flag_10_dictionary[fiscal_year_id].add(supplying_entity_id)



# Red flag 11: to see procuring entities whose plan submissions have a late submission date (Plan submissions need to be handled in the model)
#              Get every procuring entity's fiscal year plan submission mapped to the plan procurement stage
#              for every procuring entity, check for any late submissions

submission_delay_configuration = 0 # configuration stored in the database with a special name
red_flag_11_dictionary = {}
for fiscal_year_id in fiscal_year_dictionary:
    fiscal_year_start_date = fiscal_year_dictionary[fiscal_year_id]["start_date"]
    fiscal_year_start_date_and_time = str(fiscal_year_start) + " " + "00:00:00"
    red_flag_11_dictionary[fiscal_year_id] = {"late_submission":0, "on_time_submission":0, "late_submission_set": set()}
    year_procuring_entity_plans = fiscal_year_procuring_entity_plan_dictionary[fiscal_year_id]
    for procuring_entity_id in year_procuring_entity_plans:
        plan_dictionary = year_procuring_entity_plans[procuring_entity_id]
        for plan_id in plan_dictionary:
            submission_date_and_time = plan_dictionary[plan_id]["submission_date_and_time"]
            day_difference = date.strptime(fiscal_year_start_date_and_time, "%Y/%m/%d") - date.strptime(submission_date_and_time, "%Y/%m/%d")
            if day_difference > submission_delay_configuration:
                red_flag_11_dictionary[fiscal_year_id]["late_submission"] += 1
                red_flag_11_dictionary[fiscal_year_id]["late_submission_set"].add(procuring_entity_id)
            else:
                red_flag_11_dictionary[fiscal_year_id]["on_time_submission"] += 1
