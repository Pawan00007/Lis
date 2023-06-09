from rest_framework import viewsets
from .models import Patient, Message_headers, Specimen, LabOrder, Observation, Order,Dispense,MachineInfo
from .serializers import (
    MessageHeadersSerializer,
    PatientSerializer,
    SpecimenSerializer,
    LabOrderSerializer,
    ObservationSerializer,
    OrderSerializer,
    DpdSerializer,
    MachineInfoSerializer,
)

class MachineinfoViewset(viewsets.ModelViewSet):
    queryset=MachineInfo.objects.all()
    serializer_class=MachineInfoSerializer
    
class MessageHeadersViewset(viewsets.ModelViewSet):
    queryset = Message_headers.objects.all()
    serializer_class = MessageHeadersSerializer


class PatientViewset(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class SpecimenViewset(viewsets.ModelViewSet):
    queryset = Specimen.objects.all()
    serializer_class = SpecimenSerializer


class LabOrderViewset(viewsets.ModelViewSet):
    queryset = LabOrder.objects.all()
    serializer_class = LabOrderSerializer


class ObservationViewset(viewsets.ModelViewSet):
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer


class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
class DpdViewset(viewsets.ModelViewSet):
    queryset=Dispense.objects.all()
    serializer_class=DpdSerializer
