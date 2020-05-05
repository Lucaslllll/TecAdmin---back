from rest_framework import serializers
from rest_framework.response import Response
from rest_auth.serializers import UserDetailsSerializer

from rest_framework.authtoken.models import Token
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password

from .backends import EmailAuthBackend
from core.models import Techay_User, User_Client
from .models import Token_Techay, Token_Client


class LoginTechaySerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        email = data['email']
        password = data['password']

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


class LoginClientSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        email = data['email']
        password = data['password']

        try:
            client = User_Client.objects.get(email=email)
        except User_Client.DoesNotExist:
            client = None

        if client != None:
            if client.password == password:
                return client.email

            raise serializers.ValidationError("Senha errada")
        else:
            raise serializers.ValidationError("Email errado")

class VerifyTechaySerializer(serializers.Serializer):
    pk = serializers.CharField(help_text=('Primary Key do usuário TecHAY.'))
    token = serializers.CharField(help_text=('suposto Token do Usuário da TecHAY que está em login.'))
    
    def validate(self, data):
        pk = data['pk']
        token = data['token']

        try:
            techay = Techay_User.objects.get(pk=pk)
        except Techay_User.DoesNotExist:
            techay = None

        if techay == None:
            raise serializers.ValidationError("Membro não existe")
        else:
            try:
                get_token = Token_Techay.objects.get(techay_user=techay.pk)
            except Token_Techay.DoesNotExist:
                get_token = None

            if get_token == None:
                raise serializers.ValidationError("Não está logado")
            else:
                return get_token.value

class VerifyClientSerializer(serializers.Serializer):
    pk = serializers.CharField(help_text=('Primary Key do cliente.'))
    token = serializers.CharField(help_text=('suposto Token do cliente que está em login.'))
    
    def validate(self, data):
        pk = data['pk']
        token = data['token']

        try:
            client = User_Client.objects.get(pk=pk)
        except User_Client.DoesNotExist:
            client = None

        if client == None:
            raise serializers.ValidationError("Cliente não existe")
        else:
            try:
                get_token = Token_Client.objects.get(client=client.pk)
            except Token_Client.DoesNotExist:
                get_token = None

            if get_token == None:
                raise serializers.ValidationError("Não está logado")
            else:
                return get_token.value