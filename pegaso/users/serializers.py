from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['saram', 'username', 'email', 'groups', 'full_name', 'name', 'cpf', 'telephone', 'projects']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    pass