from core.models import Techay_User, User_Client
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response

from rest_framework.authtoken.models import Token

from .serializers import LoginTechaySerializer
from .utils import create_token
from .tokens import account_activation_token
from .models import Token_Techay, Token_Client

# make and after compare 
def do(techay):
	value = create_token()
	token = Token_Techay.objects.create(techay_user=techay, value=value)
	# in the future I can use to compare
	account_activation_token.make_token(value)

	return token

class LoginTechayAPI(generics.GenericAPIView):
    serializer_class = LoginTechaySerializer   

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data

        techay = Techay_User.objects.get(email=email)
        
        try: 
            token = do(techay)
        except: 
            return Response({
                "id": techay.id,
                "estado": False
            })

        return Response({

            "user": LoginTechaySerializer(techay, context=self.get_serializer_context()).data,
            "token": token.value,
            "estado": True
        })

