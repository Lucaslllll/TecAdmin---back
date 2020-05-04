from rest_framework import serializers
from rest_framework.response import Response
from rest_auth.serializers import UserDetailsSerializer

from rest_framework.authtoken.models import Token
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password

from .backends import EmailAuthBackend
from core.models import Techay_User, User_Client


class LoginTechaySerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        email = data['email']

        try:
            techay = Techay_User.objects.get(email=email)
        except Techay_User.DoesNotExist:
            techay = None

        if techay != None:
            if techay.password == password:
                return techay.email

            raise serializers.ValidationError("Senha errada")
        else:
            raise serializers.ValidationError("Email errado")

# after finish the first continues with login of client | LEMBRETE |