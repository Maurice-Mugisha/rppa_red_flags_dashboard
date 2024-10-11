# This cless rewuired some prior understending of the inderlying entity fields list and should be modified accordingly

class FieldListCreator:




    def get_procurement_party_field_list(self, append_item_list):
        field_list = ['Procuring entity id', 'name', 'identifier_scheme', 'identifier_legal_name', 'address_street', 'address_locality', 'address_region',
                      'address_postal_code', 'address_country_name', 'contact_point_email', 'contact_point_telephone', 'contact_point_fax_number', 'contact_point_url',
                      'contact_person_nat_id', 'contact_person_nationality', 'ext_bank_name', 'ext_tin'
                     ]
        field_list = self.append_to_list(field_list, append_item_list)
        return field_list



    def get_party_data_list(self, entity_dictionary, append_item_list):

        name = entity_dictionary['name']
        identifier_scheme = entity_dictionary['identifier_scheme']
        identifier_legal_name = entity_dictionary['identifier_legal_name']
        address_street = entity_dictionary['address_street']
        address_locality = entity_dictionary['address_locality']
        address_region = entity_dictionary['address_region']
        address_postal_code = entity_dictionary['address_postal_code']
        address_country_name = entity_dictionary['address_country_name']
        contact_point_name = entity_dictionary['contact_point_name']
        contact_point_email = entity_dictionary['contact_point_email']
        contact_point_telephone = entity_dictionary['contact_point_telephone']
        contact_point_fax_number = entity_dictionary['contact_point_fax_number']
        contact_point_url = entity_dictionary['contact_point_url']
        contact_person_nat_id = entity_dictionary['contact_person_nat_id']
        contact_person_nationality = entity_dictionary['contact_person_nationality']
        ext_bank_name = entity_dictionary['ext_bank_name']
        ext_bank_code = entity_dictionary['ext_bank_code']
        ext_tin = entity_dictionary['ext_tin']
        legacy_id = entity_dictionary['legacy_id']

        data_list = [legacy_id, name, identifier_scheme, identifier_legal_name, address_street, address_locality, address_region,
                     address_postal_code, address_country_name, contact_point_email, contact_point_telephone, contact_point_fax_number, contact_point_url,
                     contact_person_nat_id, contact_person_nationality, ext_bank_name, ext_tin
                    ]
        data_list = self.append_to_list(data_list, append_item_list)
        return data_list




    def get_tender_field_list(self, append_item_list):
        field_list = ['id', 'language', 'title', 'description', 'main_procurement_category', 'tender_status', 'min_value_amount', 'min_value_currency', 'value_amount',
                      'value_currency', 'procurement_method', 'procurement_method_details', 'procurement_method_rationale', 'award_criteria', 'award_criteria_details', 'submission_method',
                      'has_enquiries', 'tender_period_start_date', 'tender_period_end_date', 'tender_period_duration_in_days', 'enquiry_period_start_date', 'enquiry_period_end_date',
                      'enquiry_period_duration_in_days', 'participation_fees_id', 'participation_fees_value_amount', 'participation_fees_value_currency', 'ext_tender_fee_amount',
                      'ext_total_tender_security_amount', 'ext_simpld_yn', 'ext_jv_yn', 'ext_consult_selt_mthod', 'ext_tender_estimated_value', 'ext_tender_estimated_currency',
                      'ext_planning_reference_number', 'ext_pe_code', 'ext_fiscal_year', 'ext_tender_type_code', 'ext_tender_method_code', 'ext_mod_date', 'ext_rgt_type_code', 'ext_tender_stage_code',
                      'legacy_id', 'is_test_data', 'version', 'hash', 'created_at', 'deleted_at', 'updated_at', 'status'
                     ]
        field_list = self.append_to_list(field_list, append_item_list)
        return field_list



    def get_tender_data_list(self, tender_dictionary, append_item_list):
        id = tender_dictionary['id']
        language = tender_dictionary['language']
        title = tender_dictionary['title']
        description = tender_dictionary['description']
        main_procurement_category = tender_dictionary['main_procurement_category']
        tender_status = tender_dictionary['tender_status']
        min_value_amount = tender_dictionary['min_value_amount']
        min_value_currency = tender_dictionary['min_value_currency']
        value_amount = tender_dictionary['value_amount']
        value_currency = tender_dictionary['value_currency']
        procurement_method = tender_dictionary['procurement_method']
        procurement_method_details = tender_dictionary['procurement_method_details']
        procurement_method_rationale = tender_dictionary['procurement_method_rationale']
        award_criteria = tender_dictionary['award_criteria']
        award_criteria_details = tender_dictionary['award_criteria_details']
        submission_method = tender_dictionary['submission_method']
        has_enquiries = tender_dictionary['has_enquiries']
        tender_period_start_date = tender_dictionary['tender_period_start_date']
        tender_period_end_date = tender_dictionary['tender_period_end_date']
        tender_period_duration_in_days = tender_dictionary['tender_period_duration_in_days']
        enquiry_period_start_date = tender_dictionary['enquiry_period_start_date']
        enquiry_period_end_date = tender_dictionary['enquiry_period_end_date']
        enquiry_period_duration_in_days = tender_dictionary['enquiry_period_duration_in_days'] # Almost a useless field to maintain (derivable field from start and end inquiry dates)
        participation_fees_id = tender_dictionary['participation_fees_id']
        participation_fees_value_amount = tender_dictionary['participation_fees_value_amount']
        participation_fees_value_currency = tender_dictionary['participation_fees_value_currency']
        ext_tender_fee_amount = tender_dictionary['ext_tender_fee_amount']
        ext_total_tender_security_amount = tender_dictionary['ext_total_tender_security_amount']
        ext_simpld_yn = tender_dictionary['ext_simpld_yn']
        ext_jv_yn = tender_dictionary['ext_jv_yn']
        ext_consult_selt_mthod = tender_dictionary['ext_consult_selt_mthod']
        ext_tender_estimated_value = tender_dictionary['ext_tender_estimated_value']
        ext_tender_estimated_currency = tender_dictionary['ext_tender_estimated_currency']
        ext_planning_reference_number = tender_dictionary['ext_planning_reference_number']
        ext_pe_code = tender_dictionary['ext_pe_code']
        ext_fiscal_year = tender_dictionary['ext_fiscal_year']
        ext_tender_type_code = tender_dictionary['ext_tender_type_code']
        ext_tender_method_code = tender_dictionary['ext_tender_method_code']
        ext_mod_date = tender_dictionary['ext_mod_date']
        ext_rgt_type_code = tender_dictionary['ext_rgt_type_code']
        ext_tender_stage_code = tender_dictionary['ext_tender_stage_code']
        legacy_id = tender_dictionary['legacy_id']
        is_test_data = tender_dictionary['is_test_data']
        version = tender_dictionary['version']
        hash = tender_dictionary['hash']
        created_at = tender_dictionary['created_at']
        deleted_at = tender_dictionary['deleted_at']
        updated_at = tender_dictionary['updated_at']
        status = tender_dictionary['status']

        data_list = [id, language, title, description, main_procurement_category, tender_status, min_value_amount, min_value_currency, value_amount,
                     value_currency, procurement_method, procurement_method_details, procurement_method_rationale, award_criteria, award_criteria_details, submission_method,
                     has_enquiries, tender_period_start_date, tender_period_end_date, tender_period_duration_in_days, enquiry_period_start_date, enquiry_period_end_date,
                     enquiry_period_duration_in_days, participation_fees_id, participation_fees_value_amount, participation_fees_value_currency, ext_tender_fee_amount,
                     ext_total_tender_security_amount, ext_simpld_yn, ext_jv_yn, ext_consult_selt_mthod, ext_tender_estimated_value, ext_tender_estimated_currency,
                     ext_planning_reference_number, ext_pe_code, ext_fiscal_year, ext_tender_type_code, ext_tender_method_code, ext_mod_date, ext_rgt_type_code, ext_tender_stage_code,
                     legacy_id, is_test_data, version, hash, created_at, deleted_at, updated_at, status
                    ]
        data_list = self.append_to_list(data_list, append_item_list)
        return data_list




    def append_to_list(self, item_list, append_item_list):
        for item in append_item_list:
            item_list.append(item)
        return item_list
