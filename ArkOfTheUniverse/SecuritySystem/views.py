from SecuritySystem.models import CommunicationAPI, ActiveSession
from SecuritySystem.functions import GenerateRandomKey, CheckHashAuth, CheckStatusSession
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from BlockchainSystem.models import MoralisAPI, MoralisAuth

from GeneralSystem.models import Player
from GameAPI.models import SpaceShip

from datetime import datetime
import json

# Create your views here.

@csrf_exempt
def GenerateConnection(request):
	try:
		auth = request.POST.get('auth')
		if (CheckHashAuth(auth)):
			now = datetime.utcnow()
			expirationSessions = datetime.fromtimestamp(
				datetime.timestamp(
					datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
					)
				+86400
				)

			connection  	= GenerateRandomKey(100)
			confirmation 	= GenerateRandomKey(100)
			access  		= GenerateRandomKey(100)
			sessionCreation = ActiveSession(
				key_connection 		= connection,
				key_confirmation 	= confirmation,
				key_access 			= access,
				expiration 			= expirationSessions
			)
			sessionCreation.save()
			response = {
				'connection'	: connection,
				'confirmation' 	: confirmation,
			}
			return JsonResponse(response)
	except:
		pass
	raise PermissionDenied()

@csrf_exempt
def CheckConnection(request):
	try:
		auth = request.POST.get('auth')
		if (CheckHashAuth(auth)):
			key_confirmation = request.POST.get('confirmation')
			CurrentSession = ActiveSession.objects.get(key_confirmation=key_confirmation, player__isnull=False, spaceship__isnull=False, pending=True)
			CurrentSession.pending = False
			CurrentSession.save()
			response = {
				'address': CurrentSession.player.address,
				'access': CurrentSession.key_access
			}
			return JsonResponse(response)
	except Exception as err:
		print(err)
	raise PermissionDenied()

@csrf_exempt
def CheckStatus(request):
	try:
		Player = CheckStatusSession(request)
		if (Player):
			response = {
				'nickname': Player.nickname,
				'address' : Player.address
			}
			return JsonResponse(response)
	except:
		pass
	raise PermissionDenied()

@login_required(login_url='login')
def ConnectWallet(request, key_connection):
	try:
		CurrentSession = ActiveSession.objects.get(key_connection=key_connection, player__isnull=True, pending=True)
		try:
			PlayerLogged = Player.objects.get(user=request.user)
			OldSession = ActiveSession.objects.filter(player=PlayerLogged).delete()
			CurrentSession.player = PlayerLogged
			CurrentSession.save()
			return redirect('ShipSelection')
		except:
			pass
	except:
		pass
	return HttpResponse('Chave Invalida, ou ja conectado.')
	#raise PermissionDenied()

@login_required(login_url='login')
def ShipSelection(request):
	with open("shipBackup.json","r") as file:
		shipList = json.loads(file.read())[request.user.username.lower()]
	context = {
		"shipList": shipList
	}
	return render(request, 'page/shipSelection.html', context)

@login_required(login_url='login')
def ShipConfirmation(request, ShipID):
	try:
		with open("shipBackup.json","r") as file:
			shipList = json.loads(file.read())[request.user.username.lower()]

		SpaceShipSelected = SpaceShip.objects.get(ShipID=ShipID)
		print(SpaceShipSelected)
		for ship in shipList:
			if (int(ship['id'])==int(ShipID)):
				PlayerLogged   = Player.objects.get(user=request.user)
				CurrentSession = ActiveSession.objects.get(player=PlayerLogged, spaceship__isnull=True)
				CurrentSession.spaceship = SpaceShipSelected
				CurrentSession.save()
	except:
		return redirect('ShipSelection')
	return redirect('dashboard')

"""
# Exemplo Python Game

from datetime import datetime
import hashlib, requests, time, os

API_KEY = 'XUExx4d0iKZrcI2k3ldHFRVLU1u8mIRB64mnaHNihtrlUy5pofsQ9yHqadRNHxMO0z4d8aNXJt9Az4hkvLhg1NSCI6DK8f3scTTS'

def GetCurrentTime():
	now = datetime.utcnow()
	now = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
	return now.strftime("%Y%m%d%H%M%S")

def StartSession():
	now = GetCurrentTime()
	key_now = API_KEY + now
	auth = hashlib.sha256(key_now.encode('utf-8')).hexdigest()
	return requests.post('http://127.0.0.1:8000/server/generate_connection/', data={'auth':auth}).json()

def CheckSession(confirmation):
	for x in range(120):
		try:
			now = GetCurrentTime()
			key_now = API_KEY + now
			auth = hashlib.sha256(key_now.encode('utf-8')).hexdigest()

			response = requests.post('http://127.0.0.1:8000/server/check_connection/', data={'auth':auth,'confirmation':confirmation})
			if (response.status_code==200):
				return response.json()
			else:
				print("Usuario ainda nao conectou")
		except Exception as err:
			print(err)
		time.sleep(1)

def CheckStatus(confirmation, access):
	now = GetCurrentTime()
	key_now = API_KEY + now
	key_session = access + now
	auth = hashlib.sha256(key_now.encode('utf-8')).hexdigest()
	authSession = hashlib.sha256(key_session.encode('utf-8')).hexdigest()
	
	return requests.post('http://127.0.0.1:8000/server/status/', data={'auth':auth,'confirmation':confirmation,'authSession':authSession}).json()

newSession = StartSession()
print('Sessao criada')
print('Key de Conexao coletada')
print('Key de Confirmacao coletada')

os.system('start http://127.0.0.1:8000/server/connect/{}'.format(newSession['connection']))

access = CheckSession(newSession['confirmation'])['access']
print('Key de Acesso coletada')

print(CheckStatus(newSession['confirmation'],access))
"""