from GeneralSystem.models import Player
from django.db import models

# Create your models here.

class Rarity(models.Model):
	created         	= models.DateTimeField(auto_now_add=True)
	updated_at      	= models.DateTimeField(auto_now=True)

	name 				= models.CharField(max_length=100, blank=True, null=True)
	description 		= models.TextField(max_length=500, blank=True, null=True)
	image 				= models.ImageField(upload_to='element/rarity/', blank=True, null=True)

	def __str__(self):
		return str(self.name)

class Element(models.Model):
	created         	= models.DateTimeField(auto_now_add=True)
	updated_at      	= models.DateTimeField(auto_now=True)

	name_id 			= models.CharField(max_length=100, blank=True, null=True)
	name 				= models.CharField(max_length=100, blank=True, null=True)
	description 		= models.TextField(max_length=500, blank=True, null=True)
	rarity 				= models.ForeignKey(Rarity, on_delete=models.SET_NULL, blank=True, null=True)
	image 				= models.ImageField(upload_to='element/representation/', blank=True, null=True)

	def __str__(self):
		return str(self.name_id)

class Ore(models.Model):
	created         	= models.DateTimeField(auto_now_add=True)
	updated_at      	= models.DateTimeField(auto_now=True)

	element 			= models.ForeignKey(Element, on_delete=models.CASCADE)
	refined 			= models.BooleanField(default=False)

	def __str__(self):
		return str(self.element)

class Item(models.Model):
	created         	= models.DateTimeField(auto_now_add=True)
	updated_at      	= models.DateTimeField(auto_now=True)

	element 			= models.ForeignKey(Element, on_delete=models.CASCADE)
	duration 			= models.FloatField(default=0)

	def __str__(self):
		return str(self.element)

class ElementRefination(models.Model):
	created         	= models.DateTimeField(auto_now_add=True)
	updated_at      	= models.DateTimeField(auto_now=True)

	tax 				= models.FloatField(default=0)
	amount  		 	= models.FloatField(default=0)
	before  			= models.ForeignKey(Element, on_delete=models.SET_NULL, blank=True, null=True, related_name='%(class)sbefore')
	after 				= models.ForeignKey(Element, on_delete=models.SET_NULL, blank=True, null=True, related_name='%(class)safter')
	
class ElementSpawn(models.Model):
	created         	= models.DateTimeField(auto_now_add=True)
	updated_at      	= models.DateTimeField(auto_now=True)

	element 			= models.ForeignKey(Element, on_delete=models.CASCADE)
	default_size 		= models.FloatField(default=0)
	variation_size 		= models.FloatField(default=0)
	probability 		= models.FloatField(default=0)

	def __str__(self):
		return str(self.element)

class ElementOwner(models.Model):
	created         	= models.DateTimeField(auto_now_add=True)
	updated_at      	= models.DateTimeField(auto_now=True)

	element 			= models.ForeignKey(Element, on_delete=models.CASCADE)
	player 				= models.ForeignKey(Player, on_delete=models.CASCADE)
	amount 				= models.FloatField(default=0)

	def __str__(self):
		return str(self.element)

class ElementActivation(models.Model):
	created         	= models.DateTimeField(auto_now_add=True)
	updated_at      	= models.DateTimeField(auto_now=True)

	element 			= models.ForeignKey(Element, on_delete=models.CASCADE)
	player 				= models.ForeignKey(Player, on_delete=models.CASCADE)
	expiration         	= models.DateTimeField()

	def __str__(self):
		return str(self.element)