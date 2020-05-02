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
    serializer_class = TechayUserSerializer

class GraphSiteViewSet(viewsets.ModelViewSet):
    queryset = Graph_Site.objects.all()
    serializer_class = GraphSiteSerializer



class SocialNetworkingViewSet(viewsets.ModelViewSet):
    queryset = Social_Networking.objects.all()
    serializer_class = SocialNetworkingSerializer

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class UserClientViewSet(viewsets.ModelViewSet):
    queryset = User_Client.objects.all()
    serializer_class = UserClientSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class GraphTeamViewSet(viewsets.ModelViewSet):
    queryset = Graph_Team.objects.all()
    serializer_class = GraphTeamSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class CollectViewSet(viewsets.ModelViewSet):
    queryset = Collect.objects.all()
    serializer_class = CollectSerializer