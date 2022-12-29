from django.db import models

# Create your models here.

class MoralisAPI(models.Model):
	created         = models.DateTimeField(auto_now_add=True)
	updated_at      = models.DateTimeField(auto_now=True)

	name            = models.CharField(max_length=100,blank=True, null=True)
	description     = models.TextField(blank=True, null=True)
	active          = models.BooleanField(default=False)

	API_KEY         = models.CharField(max_length=100)
	DAPP_URL        = models.CharField(max_length=100)
	APP_ID          = models.CharField(max_length=100)
	MASTER_KEY      = models.CharField(max_length=100)

	def __str__(self):
		return str(self.name)

class MoralisAuth(models.Model):
	created         = models.DateTimeField(auto_now_add=True)
	updated_at      = models.DateTimeField(auto_now=True)

	name            = models.CharField(max_length=100,blank=True, null=True)
	description     = models.TextField(blank=True, null=True)
	active          = models.BooleanField(default=False)

	DOMAIN          = models.CharField(max_length=100)
	CHAIN_ID        = models.DecimalField(max_digits=10,decimal_places=0,default=56)
	STATEMENT       = models.CharField(max_length=100,default="Please confirm")
	URI             = models.CharField(max_length=100)
	EXPIRATION_TIME = models.DecimalField(max_digits=10,decimal_places=0,default=604800)
	TIMEOUT         = models.DecimalField(max_digits=10,decimal_places=0,default=15)

	def __str__(self):
		return str(self.name)

class BlockchainNetwork(models.Model):
	created         = models.DateTimeField(auto_now_add=True)
	updated_at      = models.DateTimeField(auto_now=True)

	name            = models.CharField(max_length=100,blank=True, null=True)
	description     = models.TextField(blank=True, null=True)
	default         = models.BooleanField(default=False)
	active          = models.BooleanField(default=False)

	NETWORK_NAME     = models.CharField(max_length=100,default="Smart Chain")
	RPC_URL          = models.CharField(max_length=100,default="https://bsc-dataseed.binance.org/")
	CHAIN_ID         = models.DecimalField(max_digits=10,decimal_places=0,default=56)
	SYMBOL           = models.CharField(max_length=100,default="BNB")
	EXPLORER_URL     = models.CharField(max_length=100,default="https://bscscan.com")
 
	def __str__(self):
		return str(self.name)