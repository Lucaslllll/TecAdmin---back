from django.urls import include
from django.urls import path

from .api import LoginTechayAPI, LoginClientAPI, VerifyTechayAPI, VerifyClientAPI

from rest_framework import routers
router = routers.DefaultRouter()


urlpatterns = [
	# techay
	path('login_techay', LoginTechayAPI.as_view(), name='login_techay'),
	path('verify_techay', VerifyTechayAPI.as_view(), name='verify_techay'),

	# client
	path('login', LoginClientAPI.as_view(), name='login'),
	path('verify_client', VerifyClientAPI.as_view(), name='verify_client'),
]