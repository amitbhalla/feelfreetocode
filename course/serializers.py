from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Course, Category, Tag


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
