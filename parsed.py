
with open(
    r"C:\Users\paban\OneDrive\Desktop\machines\MS - Fast\payloads\BA200.txt", "r"
) as file:
    data = file.read()
    message = data.split("\n")
# MSH FIELDS NAME
MSH_field_name = [
    # "FieldSeparator",
    # "EncodingCharacters",
    "Sending_Application","Sending_Facility","Receiving_Application","Receiving_Facility ","Date-Time_of_Message",
    "Security","Message_Type","Message_Control_ID","Processing_ID ","Version_D ","Sequence_Number","Continuation_Pointer",
    "Accept_Acknowledgment_Type","Application_Acknowledgment_Type","Country_Code ","Character_Set ",
    "Principal_Language_Of_Message","Alternate_Character_Set_Handling_Scheme","Message_Profile_Identifier",]
# PID FIELDS NAME
PID_field_name = [
    "Set_ID","Patient_ID","Patient_Identifier_List","Alternate_Patient_ID","Patient_Name","Mother_Maiden_Name",
    "Date_of_Birth","Sex","Patient_Alias","Race","Patient_Address","County_Code","Phone_Number_Home","Phone_Number_Business",
    "Primary_Language","Marital_Status","Religion","Patient_Account_Number","SSN_Number_Patient","Driver_License_Number",
    "Mother_Identier","Ethnic_Group","Birth_Place","Multiple_Birth_Indicator","Birth_Order","Citizenship",
    "Veterans_Military_Status","Nationality_Code","PatientDeath_Date_and_Time","Patient_Death_Indicator",]
# SPM FIELDS NAME
SPM_field_name = [
    "Set_ID","Specimen_ID","Specimen_Parent_ID","Specimen_Type","Specimen_Type_Modifier","Specimen_Additives",
    "Specimen_Collection_Method","SSpecimen_SourceSite","Specimen_Source_Site_Modifier","Specimen_Collection_Site",
    "Specimen_Role","Specimen_Collection_Amount","Grouped_Specimen_Count","Specimen_Description",]
# OBR FIELDS NAME
OBR_field_name = [
    "Set_ID","Placer_Order_Number","Filler_Order_Number","Universal Service Identifier","Priority",
    "Requested_ordered_date_time","Observation_date_time","Observation_end_date_time","Collection_volume",
    "Collector_identifier","Specimen_action_code","Dnger_code","Relevant_clinical_information",
    "Specimen_received_date_time","Specimen_source","Ordering_provider","Order_callback_phone_number","Placer_field_1",
    "Placer_field_2","Filler_field_1","Filler_field_2","Results_rpt_status_change_date_time","Charge_to_practice",
    "Diagnostic_serv_sect_id","Result_status","Parent_result","Quantity_timing","Result_copies_to","Parent",
    "Transportation_mode","Reason_for_study","Principal_result_interpreter","Assistant_result_interpreter","Technician",
    "Transcriptionist","Scheduled_date_time","Number_of_sample_containers","Transport_logistics_of_collected_sample",
    "Collectors_comment","Transport_arrangement_responsibility","Transport_arranged","Escort_required",
    "Planned_patient_transport_comment",]
# OBX FIELDS NAME
OBX_field_name = [
    "Set_id","Value_type","Observation_identifier","Observation_sub_id","Observation_value","Units",
    "Reference_range","Abnormal_flag","Probability","Nature_of_abnormal_test","Observation_result_status",
    "Effective_date_of_reference_range","User_defined_access_checks","Observation_date_time","Producers_id",
    "Responsible_observer","Observation_method","Equipment_instance_identifier","Analysis_date_time",
    "Observation_site","Observation_instance_identifier","Mood_code","Performing_organization_name",
    "Performing_organization_address","Performing_organization_medical_director","Patient_results_release_category",
    "Root_cause_of_delay",]
# ORC FIELDS NAME
ORC_field_name = [
    "Order_control","Placer_order_number","Filler_order_number","Placer_group_number","Order_status",
    "Response_flag","Quantity_timing","Parent","Date_time_transaction","Entered_by","Verified_by",
    "Ordering_provider","Enterers_location","Call_back_phone_number","Order_effective_datetime",
    "Order_control_code_reason","Entering_organization","Entering_device","Action_by","Advanced_beneficiary_notice_code",
    "Ordering_facility_name","Ordering_facility_address","Ordering_facility_phone_number","Ordering_provider_address",
    "Order_status_modifier","Advanced_beneficiary_notice_override_reason","Fillers_expected_availability_datetime",
    "Confidentiality_code","Order_type",]
DPD_field_name = [
    "Order_sequence_number_(NM)","Dispense_sequence_number_(NM)","Compound_code_(CE)","Dispense_to_location_(LA2)",
    "Dispense_to_address_(XAD)","Pharmacy_order_type_(CE)","Original_order_date_time_(TS)","Give_per_time_unit_(ST)",
    "Give_rate_amount_(ST)","Give_rate_units_(CE)","Give_strength_(NM)","Give_strength_units_(CE)",
    "Substance_lot_number_(ST)","Substance_expiration_date_(TS)","Substance_manufacturer_name_(CE)",
    "Indication_for_use_(CE)","Dispense_package_size_(NM)","Dispense_package_size_unit_of_measure_(CE)",
    "Dispense_package_method_(CE)","Supplementary_code_(CE)","Initiating_location_(LA2)",
    "Packaging_assembly_location_(LA2)","Actual_drug_strength_volume_(NM)","Actual_drug_strength_volume_units_(CE)",
    "Dispense_to_pharmacy_phone_number_(TN)","Dispense_to_pharmacy_contact_name_(XPN)","Prescription_number_(ST)",
    "Number_of_refills_remaining_(NM)","Dispense_notes_(ST)","Dispensing_provider_(XCN)",]


# def maping_segments():
#     mapped_messages = []
#     for segment in message:
#         segments = segment.split("|")
#         if "MSH" in segments[0]:
#             MSH_pairs = dict(zip(MSH_field_name, segments[2:]))
#             # print(MSH_pairs)
#             mapped_messages.append(MSH_pairs)
#             # print(MSH_pairs)
#         if segments[0] == "PID":
#             PID_pairs = dict(zip(PID_field_name, segments[1:]))
#             mapped_messages.append(PID_pairs)
#         if segments[0] == "OBR":
#             OBR_paris = dict(zip(OBR_field_name, segments[1:]))
#             # print(OBR_paris)
#             # mapped_messages.append(OBR_paris)
#         if segments[0] == "ORC":
#             ORC_pairs = dict(zip(ORC_field_name, segments[1:]))
#             mapped_messages.append(ORC_pairs)
#         if segments[0] == "OBX":
#             OBX_pairs = dict(zip(OBX_field_name, segments[1:]))
#             mapped_messages.append(OBX_pairs)
#         if segments[0] == "SPM":
#             SPM_pairs = dict(zip(SPM_field_name, segments[1:]))
#             mapped_messages.append(SPM_pairs)
#     return mapped_messages
