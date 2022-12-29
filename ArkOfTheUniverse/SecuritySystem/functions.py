from SecuritySystem.models import CommunicationAPI, ActiveSession
from datetime import datetime 
import hashlib, random

charList = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789"

def GenerateRandomKey(length):
	key = ''
	for x in range(length):
		key += random.choice(charList)
	return key

def CheckHashAuth(AuthHash):
	try:
		API_KEY = CommunicationAPI.objects.get(active=True).key
	except:
		return False

	now = datetime.utcnow()
	now = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)

	now_timestamp = datetime.timestamp(now)

	valid_time = []
	before = datetime.fromtimestamp(now_timestamp - 1)
	after = datetime.fromtimestamp(now_timestamp + 1)

	#valid_time.append(before.strftime("%Y%m%d%H%M%S"))
	#valid_time.append(now.strftime("%Y%m%d%H%M%S"))
	#valid_time.append(after.strftime("%Y%m%d%H%M%S"))

	valid_time.append(before.strftime("%Y%m%d%H%M"))
	valid_time.append(now.strftime("%Y%m%d%H%M"))
	valid_time.append(after.strftime("%Y%m%d%H%M"))

	for time in valid_time:
		key = API_KEY+time
		hash_check = hashlib.sha256(key.encode('utf-8')).hexdigest()
		if (AuthHash==hash_check):
			return True

	return False

def CheckHashSession(confirmation,AuthSessionHash):
	try:
		CurrentSession = ActiveSession.objects.get(key_confirmation=confirmation, player__isnull=False, pending=False)
	except:
		return False

	now = datetime.utcnow()
	now = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)

	now_timestamp = datetime.timestamp(now)
	expiration_timestamp = datetime.timestamp(CurrentSession.expiration)

	if (now_timestamp>expiration_timestamp):
		return False

	before = datetime.fromtimestamp(now_timestamp - 1)
	after = datetime.fromtimestamp(now_timestamp + 1)

	valid_time = []
	#valid_time.append(before.strftime("%Y%m%d%H%M%S"))
	#valid_time.append(now.strftime("%Y%m%d%H%M%S"))
	#valid_time.append(after.strftime("%Y%m%d%H%M%S"))

	valid_time.append(before.strftime("%Y%m%d%H%M"))
	valid_time.append(now.strftime("%Y%m%d%H%M"))
	valid_time.append(after.strftime("%Y%m%d%H%M"))

	for time in valid_time:
		key = CurrentSession.key_access+time
		hash_check = hashlib.sha256(key.encode('utf-8')).hexdigest()
		if (AuthSessionHash==hash_check):
			return True 

	return False

def CheckStatusSession(request):
	if (CheckHashAuth(request.POST.get('auth'))) and (CheckHashSession(request.POST.get('confirmation'),request.POST.get('authSession'))):
		Player = GetPlayer(request.POST.get('confirmation'))
		if (Player.banned==False):
			return Player
		else:
			return False
	else:
		return False

def GetPlayer(Confirmation):
	return ActiveSession.objects.get(key_confirmation=Confirmation, player__isnull=False, spaceship__isnull=False, pending=False).player