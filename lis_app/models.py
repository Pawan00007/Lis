from django.db import models

#Machine Informations
class MachineInfo(models.Model):
    name = models.CharField(max_length=100)
    protocol = models.CharField(max_length=20, choices=[('HL7', 'HL7'), ('ASTM', 'ASTM'),('DICOM','DICOM'),('NCPDP','NCPDP'),('FHIR','FHIR'),('X12','X12'),('CDA','CDA')])
    port = models.CharField(max_length=30, choices=[('serial_port','Serial_Port'), ('socket','Socket')])
    communication_direction = models.CharField(max_length=50, choices=[('unidirectional', 'Unidirectional'), ('bidirectional', 'Bidirectional')], blank=True)

    def __str__(self):
        return self.name
# PID FIELD
class Patient(models.Model):
    Set_ID = models.IntegerField(primary_key=True)
    Patient_ID = models.CharField(max_length=50)
    Patient_Identifier_List = models.CharField(max_length=200, blank=True)
    Alternate_Patient_ID = models.CharField(max_length=50, blank=True)
    Patient_Name = models.CharField(max_length=100)
    Mother_Maiden_Name = models.CharField(max_length=100, blank=True)
    Date_of_Birth = models.DateField()
    SEX_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]
    Sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    Patient_Alias = models.CharField(max_length=30, blank=True)
    Race = models.CharField(max_length=50, blank=True)
    Patient_Address = models.CharField(max_length=200)
    County_Code = models.CharField(max_length=5, blank=True)
    Phone_Number_Home = models.CharField(max_length=20, blank=True)
    Phone_Number_Business = models.CharField(max_length=20, blank=True)
    Primary_Language = models.CharField(max_length=50, blank=True)
    MARITIAL_CHOICES = [
        ("S", "SINGLE"),
        ("M", "MARRIED"),
        ("D", "DIVORCED"),
        ("O", "OTHERS"),
    ]
    Marital_Status = models.CharField(max_length=20, choices=MARITIAL_CHOICES)
    Religion = models.CharField(max_length=50, blank=True)
    Patient_Account_Number = models.CharField(max_length=50, blank=True)
    SSN_Number_Patient = models.CharField(max_length=9, blank=True)
    Driver_License_Number = models.CharField(max_length=20, blank=True)
    Mother_Identier = models.CharField(max_length=30, blank=True)
    Ethnic_Group = models.CharField(max_length=50, blank=True)
    Birth_Place = models.CharField(max_length=50, default="unknown", blank=True)
    Multiple_Birth_Indicator = models.BooleanField()
    Birth_Order = models.PositiveIntegerField(blank=True, null=True)
    Citizenship = models.CharField(max_length=50, blank=True)
    Veterans_Military_Status = models.CharField(max_length=50, blank=True)
    Nationality_Code = models.CharField(max_length=5, blank=True)
    PatientDeath_Date_and_Time = models.DateTimeField(blank=True, null=True)
    Patient_Death_Indicator = models.BooleanField(default=False)

    def __str__(self):
        return self.Patient_Name


# MESSAGE HEADERS FIELD(MSH)
class Message_headers(models.Model):
    sending_application = models.CharField(max_length=255)
    sending_facility = models.CharField(max_length=255)
    receiving_application = models.CharField(max_length=255)
    receiving_facility = models.CharField(max_length=255)
    date_time_of_message = models.DateTimeField()
    security = models.CharField(max_length=255)
    message_type = models.CharField(max_length=255)
    message_control_id = models.CharField(max_length=255)
    processing_id = models.CharField(max_length=255)
    version_id = models.CharField(max_length=255)
    sequence_number = models.IntegerField()
    continuation_pointer = models.CharField(max_length=255)
    accept_acknowledgment_type = models.CharField(max_length=255)
    application_acknowledgment_type = models.CharField(max_length=255)
    country_code = models.CharField(max_length=255)
    character_set = models.CharField(max_length=255)
    principal_language_of_message = models.CharField(max_length=255)
    alternate_character_set_handling_scheme = models.CharField(max_length=255)
    message_profile_identifier = models.CharField(max_length=255)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="messagesHeaders"
    )


# SPECIMEN FIELD(SPM)
class Specimen(models.Model):
    Set_ID = models.IntegerField(primary_key=True)
    Specimen_ID = models.CharField(max_length=50)
    Specimen_Parent_ID = models.CharField(max_length=50, blank=True)
    Specimen_Type = models.CharField(max_length=50)
    Specimen_Type_Modifier = models.CharField(max_length=50, blank=True)
    Specimen_Additives = models.CharField(max_length=50, blank=True)
    Specimen_Collection_Method = models.CharField(max_length=50, blank=True)
    Specimen_SourceSite = models.CharField(max_length=50, blank=True)
    Specimen_Source_Site_Modifier = models.CharField(max_length=50, blank=True)
    Specimen_Collection_Site = models.CharField(max_length=50, blank=True)
    Specimen_Role = models.CharField(max_length=50, blank=True)
    Specimen_Collection_Amount = models.CharField(max_length=50, blank=True)
    Grouped_Specimen_Count = models.PositiveIntegerField(blank=True, null=True)
    Specimen_Description = models.CharField(max_length=200, blank=True)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="specimens"
    )


# OBR FIELD
class LabOrder(models.Model):
    set_id = models.IntegerField(primary_key=True)
    Placer_order_number = models.CharField(max_length=50)
    Filler_order_number = models.CharField(max_length=50)
    Universal_service_identifier = models.CharField(max_length=50)
    Priority = models.CharField(max_length=50, blank=True)
    Requested_ordered_date_time = models.DateTimeField()
    Observation_date_time = models.DateTimeField(blank=True, null=True)
    Observation_end_date_time = models.DateTimeField(blank=True, null=True)
    Collection_volume = models.CharField(max_length=50, blank=True)
    Collector_identifier = models.CharField(max_length=50, blank=True)
    Specimen_action_code = models.CharField(max_length=50, blank=True)
    Dnger_code = models.CharField(max_length=50, blank=True)
    Relevant_clinical_information = models.CharField(max_length=200, blank=True)
    Specimen_received_date_time = models.DateTimeField(blank=True, null=True)
    Specimen_source = models.CharField(max_length=50, blank=True)
    Ordering_provider = models.CharField(max_length=50, blank=True)
    Order_callback_phone_number = models.CharField(max_length=50, blank=True)
    Placer_field_1 = models.CharField(max_length=50, blank=True)
    Placer_field_2 = models.CharField(max_length=50, blank=True)
    Filler_field_1 = models.CharField(max_length=50, blank=True)
    Filler_field_2 = models.CharField(max_length=50, blank=True)
    Results_rpt_status_change_date_time = models.DateTimeField(blank=True, null=True)
    Charge_to_practice = models.CharField(max_length=50, blank=True)
    Diagnostic_serv_sect_id = models.CharField(max_length=50, blank=True)
    Result_status = models.CharField(max_length=50, blank=True)
    Parent_result = models.CharField(max_length=50, blank=True)
    Quantity_timing = models.CharField(max_length=50, blank=True)
    Result_copies_to = models.CharField(max_length=50, blank=True)
    Parent = models.CharField(max_length=50, blank=True)
    Transportation_mode = models.CharField(max_length=50, blank=True)
    Reason_for_study = models.CharField(max_length=200, blank=True)
    Principal_result_interpreter = models.CharField(max_length=50, blank=True)
    Assistant_result_interpreter = models.CharField(max_length=50, blank=True)
    Technician = models.CharField(max_length=50, blank=True)
    Transcriptionist = models.CharField(max_length=50, blank=True)
    Scheduled_date_time = models.DateTimeField(blank=True, null=True)
    Number_of_sample_containers = models.IntegerField(blank=True, null=True)
    Transport_logistics_of_collected_sample = models.CharField(
        max_length=200, blank=True
    )
    Collectors_comment = models.CharField(max_length=200, blank=True)
    Transport_arrangement_responsibility = models.CharField(max_length=50, blank=True)
    Transport_arranged = models.CharField(max_length=50, blank=True)
    Escort_required = models.CharField(max_length=50, blank=True)
    Planned_patient_transport_comment = models.CharField(max_length=200, blank=True)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="laborders"
    )


# OBX FIELD
class Observation(models.Model):
    Set_id = models.IntegerField(primary_key=True)
    Value_type = models.CharField(max_length=2)
    Observation_identifier = models.CharField(max_length=250)
    Observation_sub_id = models.CharField(max_length=20)
    Observation_value = models.CharField(max_length=250)
    Units = models.CharField(max_length=20)
    Reference_range = models.CharField(max_length=250)
    Abnormal_flags = models.CharField(max_length=5)
    Probability = models.DecimalField(max_digits=4, decimal_places=2)
    Nature_of_abnormal_test = models.CharField(max_length=250)
    Observation_result_status = models.CharField(max_length=1)
    Effective_date_of_reference_range = models.DateField()
    User_defined_access_checks = models.CharField(max_length=20)
    Observation_date_time = models.DateTimeField()
    Producers_id = models.CharField(max_length=250)
    Responsible_observer = models.CharField(max_length=250)
    Observation_method = models.CharField(max_length=250)
    Equipment_instance_identifier = models.CharField(max_length=250)
    Analysis_date_time = models.DateTimeField()
    Observation_site = models.CharField(max_length=250)
    Observation_instance_identifier = models.CharField(max_length=250)
    Mood_code = models.CharField(max_length=3)
    Performing_organization_name = models.CharField(max_length=250)
    Performing_organization_address = models.CharField(max_length=250)
    Performing_organization_medical_director = models.CharField(max_length=250)
    Patient_results_release_category = models.CharField(max_length=20)
    Root_cause_of_delay = models.CharField(max_length=250)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="observations"
    )


# ORDER FIELD(ORC)
class Order(models.Model):
    Order_control = models.CharField(max_length=2)
    Placer_order_number = models.CharField(max_length=22)
    Filler_order_number = models.CharField(max_length=22, blank=True)
    Placer_group_number = models.CharField(max_length=22, blank=True)
    Order_status = models.CharField(max_length=2)
    Response_flag = models.CharField(max_length=1, blank=True)
    Quantity_timing = models.CharField(max_length=200, blank=True)
    Parent = models.CharField(max_length=22, blank=True)
    Date_time_transaction = models.DateTimeField()
    Entered_by = models.CharField(max_length=60)
    Verified_by = models.CharField(max_length=60, blank=True)
    Ordering_provider = models.CharField(max_length=120, blank=True)
    Enterers_location = models.CharField(max_length=60, blank=True)
    Call_back_phone_number = models.CharField(max_length=40, blank=True)
    Order_effective_datetime = models.DateTimeField(blank=True, null=True)
    Order_control_code_reason = models.CharField(max_length=200, blank=True)
    Entering_organization = models.CharField(max_length=200, blank=True)
    Entering_device = models.CharField(max_length=200, blank=True)
    Action_by = models.CharField(max_length=120, blank=True)
    Advanced_beneficiary_notice_code = models.CharField(max_length=2, blank=True)
    Ordering_facility_name = models.CharField(max_length=200, blank=True)
    Ordering_facility_address = models.CharField(max_length=200, blank=True)
    Ordering_facility_phone_number = models.CharField(max_length=40, blank=True)
    Ordering_provider_address = models.CharField(max_length=200, blank=True)
    Order_status_modifier = models.CharField(max_length=1, blank=True)
    Advanced_beneficiary_notice_override_reason = models.CharField(
        max_length=200, blank=True
    )
    Fillers_expected_availability_datetime = models.DateTimeField(blank=True, null=True)
    Confidentiality_code = models.CharField(max_length=4, blank=True)
    Order_type = models.CharField(max_length=2, blank=True)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="orders"
    )


class Dispense(models.Model):
    order_sequence_number = models.IntegerField()
    dispense_sequence_number = models.IntegerField()
    compound_code = models.CharField(max_length=100)
    dispense_to_location = models.CharField(max_length=100)
    dispense_to_address = models.CharField(max_length=100)
    pharmacy_order_type = models.CharField(max_length=100)
    original_order_date_time = models.DateTimeField()
    give_per_time_unit = models.CharField(max_length=100)
    give_rate_amount = models.CharField(max_length=100)
    give_rate_units = models.CharField(max_length=100)
    give_strength = models.IntegerField()
    give_strength_units = models.CharField(max_length=100)
    substance_lot_number = models.CharField(max_length=100)
    substance_expiration_date = models.DateTimeField()
    substance_manufacturer_name = models.CharField(max_length=100)
    indication_for_use = models.CharField(max_length=100)
    dispense_package_size = models.IntegerField()
    dispense_package_size_unit_of_measure = models.CharField(max_length=100)
    dispense_package_method = models.CharField(max_length=100)
    supplementary_code = models.CharField(max_length=100)
    initiating_location = models.CharField(max_length=100)
    packaging_assembly_location = models.CharField(max_length=100)
    actual_drug_strength_volume = models.IntegerField()
    actual_drug_strength_volume_units = models.CharField(max_length=100)
    dispense_to_pharmacy_phone_number = models.CharField(max_length=100)
    dispense_to_pharmacy_contact_name = models.CharField(max_length=100)
    prescription_number = models.CharField(max_length=100)
    number_of_refills_remaining = models.IntegerField()
    dispense_notes = models.CharField(max_length=100)
    dispensing_provider = models.CharField(max_length=100)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="dispenses"
    )
