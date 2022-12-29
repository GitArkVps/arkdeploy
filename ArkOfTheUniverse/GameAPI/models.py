from ElementSystem.models import Element, Rarity
from GeneralSystem.models import Player
from django.db import models

# Create your models here.

class ElementAvailable(models.Model):
	created         	= models.DateTimeField(auto_now_add=True)
	updated_at      	= models.DateTimeField(auto_now=True)

	element  			= models.ForeignKey(Element, on_delete=models.CASCADE)
	player 				= models.ForeignKey(Player, on_delete=models.CASCADE)

	amount 				= models.IntegerField(default=0)

	expiration         	= models.DateTimeField()

class SpaceShip(models.Model):
	created         	= models.DateTimeField(auto_now_add=True)
	updated_at      	= models.DateTimeField(auto_now=True)

	ShipID 				= models.CharField(max_length=10)
	name 	         	= models.CharField(max_length=100)
	rarity 				= models.ForeignKey(Rarity , on_delete=models.SET_NULL, blank=True, null=True)
	element  			= models.ForeignKey(Element, on_delete=models.SET_NULL, blank=True, null=True)

	image			 	= models.ImageField(upload_to='spaceship/picture/', blank=True, null=True)