from rest_framework import serializers
from .models import (
    Patient,
    Message_headers,
    Specimen,
    LabOrder,
    Observation,
    Order,
    Dispense,
)


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class MessageHeadersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message_headers
        fields = "__all__"


class SpecimenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specimen
        fields = "__all__"


class LabOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabOrder
        fields = "__all__"


class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class DpdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispense
        fields = "__all__"
