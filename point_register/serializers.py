from dataclasses import field
from statistics import mode
from rest_framework.serializers import ModelSerializer
from .models import UserPoint
from django.contrib.auth.models import User

class UserPointSerializer(ModelSerializer):
    class Meta:
        model = UserPoint
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
