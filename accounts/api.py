from core.models import Techay_User, User_Client
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data

        user = User_Client.objects.create(email=*args)
        
        
        return Response({

            "user": UserClientSerializer(user_, context=self.get_serializer_context()).data,
            
        })