from django.urls import include
from django.urls import path

from .api import LoginTechayAPI, LoginClientAPI

from rest_framework import routers
router = routers.DefaultRouter()


urlpatterns = [
	path('login_techay', LoginTechayAPI.as_view(), name='login_techay'),
	path('login', LoginClientAPI.as_view(), name='login'),
]