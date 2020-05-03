from django.db import models
import calendar
from cloudinary.models import CloudinaryField



JAN = "Janeiro";FEV = "Fevereiro";MAR = "Março";
ABR = "Abril";MAI = "Maio";JUN = "Junho";
JUL = "Julho";AGO = "Agosto";SET="Setembro";
OUT = "Outubro";NOV = "Novembro"; DEZ = "Dezembro";

MONTH_CHOICES = (
    (JAN, "Janeiro"), (FEV, "Fevereiro"), (MAR, "Março"), (ABR, "Abril"),
    (MAI, "Maio"), (JUN, "Junho"), (JUL, "Julho"), (AGO, "Agosto"),
    (SET, "Setembro"), (OUT, "Outubro"), (NOV, "Novembro"), (DEZ, "Dezembro"),
)
# Create your models here.
class Techay_User(models.Model):
	photo =CloudinaryField('foto', null=True, 
        overwrite=True,
        resource_type="image",
        transformation={"quality": "auto:good", "width": 350, "height": 150},
        format="png",
    )
	name = models.CharField(max_length=124)
	cpf = models.CharField(max_length=14)
	email = models.EmailField()
	password = models.CharField(max_length=100)
	score = models.IntegerField()
	responsibility = models.TextField()
	biography = models.TextField()
	linkedIn = models.CharField(max_length=200)
	music = models.FileField(upload_to="music")

 #  def save(self, *args, **kwargs):
 #        do_something()
 #        super().save(*args, **kwargs)  # Call the "real" save() method.
 #        do_something_else()


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
	link_site = models.CharField(max_length=200, blank=True)

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
	month = models.CharField(max_length=20, choices=MONTH_CHOICES, default=JAN)
	visits = models.IntegerField()


class Graph_Team(models.Model):
	pontos = models.IntegerField()
	month = models.CharField(max_length=20, choices=MONTH_CHOICES, default=JAN)


class Vote(models.Model):
	SIM = 'Sim'; NÃO = 'Não'; BRANCO = 'Branco'
	CHOICES = ((SIM, 'Sim'), (NÃO, 'Não'), (BRANCO, 'Branco'))
	
	images = CloudinaryField('foto', null=True, 
        overwrite=True,
        resource_type="image",
        transformation={"quality": "auto:good", "width": 350, "height": 150},
        format="png",
    )
	details = models.TextField()
	Vote = models.CharField(max_length=9, choices=CHOICES, default=BRANCO)


class Notification(models.Model):
	VOCÊ = 'Você'; EQUIPE = 'Equipe'; FINANÇAS = 'Finanças'
	CHOICES_CLIENTE = ((VOCÊ, 'Você'), (EQUIPE, 'Equipe'), (FINANÇAS, 'Finanças'))

	types = models.CharField(max_length=9, choices=CHOICES_CLIENTE, default=VOCÊ)
	photo = CloudinaryField('foto', null=True, 
        overwrite=True,
        resource_type="image",
        transformation={"quality": "auto:good", "width": 350, "height": 150},
        format="png",
    )
	details = models.TextField()
	date = models.DateTimeField()
	iink_notification = models.CharField(max_length=200, null=True, blank=True, help_text=('Se houver. '))

class Video(models.Model):
	REUNIÃO = 'Reunião'; ACADEMIA = 'Academia';
	CHOICES_TYPE = ((REUNIÃO, 'Reunião'), (ACADEMIA, 'Academia'))
	
	title = models.CharField(max_length=200)
	date = models.DateField()
	link_youtube = models.CharField(max_length=200)
	types = models.CharField(max_length=20, choices=CHOICES_TYPE, default=REUNIÃO)

class Collect(models.Model):
	cod = models.IntegerField()
	client = models.ForeignKey(User_Client, on_delete=models.CASCADE)
	date = models.DateTimeField()
	billet = models.CharField(max_length=200, help_text=('Link do boleto.'))