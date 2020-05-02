from django.contrib import admin
from .models import Techay_User, Social_Networking, Plan, User_Client, Address, Graph_Site, Graph_Team
from .models import Notification, Vote, Video, Collect

admin.site.register(Graph_Site)
admin.site.register(Techay_User)
admin.site.register(Social_Networking)
admin.site.register(Plan)
admin.site.register(User_Client)
admin.site.register(Address)
admin.site.register(Graph_Team)
admin.site.register(Notification)
admin.site.register(Vote)
admin.site.register(Collect)
admin.site.register(Video)