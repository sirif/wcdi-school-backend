from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['last_login', 'username', 'first_name', 'last_name', 'groups']

