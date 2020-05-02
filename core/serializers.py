from rest_framework import serializers
from .models import Graph_Site, Techay_User, Social_Networking, Plan, User_Client, Address, Graph_Team
from .models import Notification, Vote, Video, Collect

 GraphSiteSerializer, TechayUserSerializer, 
 SocialNetworkingSerializer, PlanSerializer UserClientSerializer AddressSerializer GraphTeamSerializer 
 NotificationSerializer,  VoteSerializer, VideoSerializer, CollectSerializer

class GraphSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Graph_Site
        fields = '__all__'

class TechayUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Techay_User
        fields = '__all__'

class SocialNetworkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social_Networking
        fields = '__all__'

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class UserClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Client
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class GraphTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Graph_Team
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class CollectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collect
        fields = '__all__'
