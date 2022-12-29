from GeneralSystem.models import Player
from GameAPI.models import SpaceShip
from django.db import models

# Create your models here.

class CommunicationAPI(models.Model):
	created         	= models.DateTimeField(auto_now_add=True)
	updated_at      	= models.DateTimeField(auto_now=True)

	key 	 			= models.CharField(max_length=100)
	active 	 			= models.BooleanField(default=False)

class ActiveSession(models.Model):
	created         	= models.DateTimeField(auto_now_add=True)
	updated_at      	= models.DateTimeField(auto_now=True)

	player 				= models.ForeignKey(Player, on_delete=models.CASCADE, blank=True, null=True)
	spaceship 			= models.ForeignKey(SpaceShip, on_delete=models.SET_NULL, blank=True, null=True)

	pending 			= models.BooleanField(default=True)

	key_connection 		= models.CharField(max_length=100)
	key_confirmation 	= models.CharField(max_length=100)
	key_access 		 	= models.CharField(max_length=100)

	expiration         	= models.DateTimeField()