from rest_framework import viewsets
from rest_framework import permissions
from App.models import *
from App.serializers import *


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = [permissions.AllowAny]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]


class MistakeRecordViewSet(viewsets.ModelViewSet):
    queryset = MistakeRecord.objects.all()
    serializer_class = MistakeRecordSerializer
    permission_classes = [permissions.AllowAny]


class WandViewSet(viewsets.ModelViewSet):
    queryset = Wand.objects.all()
    serializer_class = WandSerializer
    permission_classes = [permissions.AllowAny]


class MagicViewSet(viewsets.ModelViewSet):
    queryset = Magic.objects.all()
    serializer_class = MagicSerializer
    permission_classes = [permissions.AllowAny]