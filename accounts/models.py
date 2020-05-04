from django.db import models
from core.models import Techay_User, User_Client

class Token_Techay(models.Model):
	value = models.CharField(max_length=20, help_text=('Máximo de 20 caracteres'))
	techay_user = models.OneToOneField(Techay_User, on_delete=models.CASCADE)
	posting_date = models.DateTimeField(auto_now_add=True)


class Token_Client(models.Model):
	value = models.CharField(max_length=20, help_text=('Máximo de 20 caracteres'))
	client = models.OneToOneField(User_Client, on_delete=models.CASCADE)
	posting_date = models.DateTimeField(auto_now_add=True)
