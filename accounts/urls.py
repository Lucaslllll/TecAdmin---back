from django.urls import include
from django.urls import path

from .api import LoginTechayAPI

from rest_framework import routers
router = routers.DefaultRouter()


urlpatterns = [
	path('login_techay', LoginTechayAPI, name='login_techay'),
]