from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Player(models.Model):
	created         = models.DateTimeField(auto_now_add=True)
	updated_at      = models.DateTimeField(auto_now=True)

	user			= models.ForeignKey(User, on_delete=models.CASCADE)

	address         = models.CharField(max_length=50)
	nickname        = models.CharField(max_length=100, blank=True, null=True)
	status          = models.CharField(max_length=100, blank=True, null=True)
	image			= models.ImageField(upload_to='player/picture/', blank=True, null=True)

	space 			= models.FloatField(default=0)

	banned 			= models.BooleanField(default=False)

	def __str__(self):
		return str(self.nickname)