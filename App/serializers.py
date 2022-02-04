from rest_framework import serializers
from App.models import *


class HouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = House
        fields = '__all__'


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class MistakeRecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MistakeRecord
        fields = '__all__'


class WandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wand
        fields = '__all__'


class MagicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Magic
        fields = '__all__'