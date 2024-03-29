from core.models import Techay_User, User_Client
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response

from rest_framework.authtoken.models import Token

# coloco essa importanção como tupla para facilitar depois ;)
from .serializers import (LoginTechaySerializer, LoginClientSerializer, VerifyTechaySerializer, VerifyClientSerializer)
from .utils import create_token
from .tokens import account_activation_token
from .models import Token_Techay, Token_Client

# make and after compare 


class LoginTechayAPI(generics.GenericAPIView):
    serializer_class = LoginTechaySerializer   

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data

        techay = Techay_User.objects.get(email=email)
        value = create_token()

        try: 
            token = Token_Techay.objects.create(techay_user=techay, value=value)
        except: 
            token = None


        if token != None:
            return Response({

                "user": LoginTechaySerializer(techay, context=self.get_serializer_context()).data,
                "token": token.value,
                "estado": True
            })
        else:
            token = Token_Techay.objects.get(techay_user=techay)
            return Response({
                "id": techay.id,
                "estado": False,
                "token": token.value,
                "justificativa": "Login do Membro já foi realizado!"
            })

class LoginClientAPI(generics.GenericAPIView):
    serializer_class = LoginClientSerializer   

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data

        client = User_Client.objects.get(email=email)
        value = create_token()

        try: 
            token = Token_Client.objects.create(client=client, value=value)
        except: 
            token = None


        if token != None:
            return Response({

                "user": LoginTechaySerializer(client, context=self.get_serializer_context()).data,
                "token": token.value,
                "estado": True
            })
        else:
            token = Token_Client.objects.get(client=client)
            return Response({
                "id": client.id,
                "estado": False,
                "token": token.value,
                "justificativa": "Login já realizado!"
            })


class VerifyTechayAPI(generics.GenericAPIView):
    serializer_class = VerifyTechaySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        # token dado
        token = request.data['token']

        # token do usuário pego pelo chave primária
        get_token = serializer.validated_data

        if get_token == token:
            return Response(True,)
        else:
            return Response(False,)


class VerifyClientAPI(generics.GenericAPIView):
    serializer_class = VerifyClientSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        # token dado
        token = request.data['token']

        # token do usuário pego pelo chave primária
        get_token = serializer.validated_data

        if get_token == token:
            return Response(True,)
        else:
            return Response(False,)


# lembrete: logout