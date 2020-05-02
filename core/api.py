from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response

from .models import Techay_User, Social_Networking, Plan, User_Client, Address, Graph_Site, Graph_Team
from .models import Notification, Vote, Video, Collect

from .serializers import GraphSiteSerializer, TechayUserSerializer, SocialNetworkingSerializer, PlanSerializer 
from .serializers import UserClientSerializer, AddressSerializer, GraphTeamSerializer 
from .serializers import NotificationSerializer,  VoteSerializer, VideoSerializer, CollectSerializer


class TechayUserViewSet(viewsets.ModelViewSet):
    queryset = Techay_User.objects.all()
    serializer_class = UsuarioSerializer