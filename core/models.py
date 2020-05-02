from django.db import models
import calendar

# Create your models here.
class Techay_User(models.Model):
	photo = models.ImageField(upload_to="photo_users_techay")
	name = models.CharField(max_length=124)
	cpf = models.CharField(max_length=14)
	email = models.EmailField()
	password = models.CharField(max_length=100)
	score = models.IntegerField()
	responsibility = models.TextField()
	biography = models.TextField()
	linkedIn = models.CharField(max_length=200)
	Music = models.FileField(upload_to="music")


class Social_Networking(models.Model):
	link = models.CharField(max_length=200)
	techay_user = models.ForeignKey(Techay_User, on_delete=models.CASCADE)


class Plan(models.Model):
	name = models.CharField(max_length=100)
	details = models.TextField()

class User_Client(models.Model):
	name = models.CharField(max_length=124)
	whatsapp = models.CharField(max_length=20)
	email = models.EmailField()
	password = models.CharField(max_length=100)
	cpf_cnpj = models.CharField(max_length=30)
	link_site = models.CharField(max_length=200)

class Address(models.Model):
	client = models.OneToOneField(User_Client, on_delete=models.CASCADE)
	postal_code = models.CharField(max_length=100)
	street = models.CharField(max_length=100)
	number = models.IntegerField()
	district = models.CharField(max_length=200)
	complement = models.CharField(max_length=300)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)

class Graph_Site(models.Model):
	JAN = "Janeiro";FEB = "Fevereiro";MAR = "Março"
	ABR = "Abril";MAI = "Maio";JUN = "Junho"
	JUL = "Julho";AGO = "Agosto";SET="Setembro"
	OUT = "Outubro";NOV = "Novembro"; DEZ = "Dezembro"

	MONTH_CHOICES = (
	    (JAN, "Janeiro"),
	    (FEV, "Fevereiro"),
	    (MAR, "Março"),
	    (ABR, "Abril"),
	    (MAI, "Maio"),
	    (JUN, "Junho"),
	    (JUL, "Julho"),
	    (AGO, "Agosto"),
	    (SET, "Setembro"),
	    (OUT, "Outubro"),
	    (NOV, "Novembro"),
	    (DEZ, "Dezembro"),
	)
	month = models.CharField(max_length=9, choices=MONTH_CHOICES, default=JAN)
	visits = models.IntegerField()