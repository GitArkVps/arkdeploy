from SecuritySystem.models import ActiveSession
from SecuritySystem.functions import CheckStatusSession

from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, JsonResponse

from ElementSystem.models import Element, ElementActivation, ElementSpawn, ElementOwner, Ore, Item
from GeneralSystem.models import Player
from GameAPI.models import ElementAvailable, SpaceShip

from datetime import datetime
from random import choices, randint

# Create your views here.

@csrf_exempt
def MiningGenerate(request):
	try:
		Player = CheckStatusSession(request)
		if (Player):
			AvailableList = ElementAvailable.objects.filter(player=Player)
			if (AvailableList):
				now = datetime.utcnow()
				exp = AvailableList[0].expiration
				if (now>exp):
					AvailableList.delete()
				else:
					response = {}
					for available in AvailableList:
						response[available.element.name_id] = available.amount
					return JsonResponse(response)
			ElementList = ElementSpawn.objects.all()
			Probability = []
			for element in ElementList:
				Probability.append(element.probability)
			response = {}
			for x in range(50):
				element = choices(ElementList,Probability)[0].element
				try:
					response[element.name_id] += 1
				except:
					response[element.name_id] = 1
			for key in response:
				element = Element.objects.get(name_id=key)
				now = datetime.utcnow()
				now = datetime.timestamp(now)
				now = datetime.fromtimestamp(now+3600)
				ElementAvailable(element=element,player=Player,amount=response[key],expiration=now).save()
			return JsonResponse(response)

	except:
		pass
	raise PermissionDenied()

@csrf_exempt
def MiningClaim(request):
	try:
		Player = CheckStatusSession(request)
		if (Player):
			AvailableList = ElementAvailable.objects.filter(player=Player)
			if (AvailableList):
				now = datetime.utcnow()
				exp = AvailableList[0].expiration
				if (now>exp):
					raise PermissionDenied()
			element_id = request.POST.get('name_id')
			element_amount = int(request.POST.get('amount'))
			element = Element.objects.get(name_id=element_id)
			AvailableUpdate = AvailableList.get(element=element)

			if (element_amount>AvailableUpdate.amount):
				raise PermissionDenied()
			if (AvailableUpdate.amount>0):
				AvailableUpdate.amount -= element_amount
				AvailableUpdate.save()
			else:
				raise PermissionDenied()


			try:
				Ownership = ElementOwner.objects.get(player=Player,element=element)
				Ownership.amount += element_amount
				Ownership.save()
			except:
				Ownership = ElementOwner(player=Player,element=element)
				Ownership.amount += element_amount
				Ownership.save()

			response = {'status':'success'}
			return JsonResponse(response)
	except Exception as err:
		pass
	raise PermissionDenied()

@csrf_exempt
def PlayerElements(request):
	try:
		Player = CheckStatusSession(request)
		if (Player):
			ItemList = Item.objects.all()
			OreList  =  Ore.objects.all()
			now = datetime.utcnow()

			response = {
				'ore'         : [],
				'item'        : [],
				'active_item' : [],
				'space'       : Player.space
			}

			for ore in OreList:
				try:
					result = ElementOwner.objects.get(player=Player, element=ore.element)
					if (result.amount>0):
						response['ore'].append({
							'name_id'     : ore.element.name_id,
							'name'        : ore.element.name,
							'description' : ore.element.description,
							'rarity'      : ore.element.rarity.name,
							'refined'     : ore.refined,
							'amount'      : result.amount
						})
				except:
					pass

			for item in ItemList:
				try:
					result = ElementOwner.objects.get(player=Player, element=item.element)
					if (result.amount>0):
						response['item'].append({
							'name_id'     : item.element.name_id,
							'name'        : item.element.name,
							'description' : item.element.description,
							'rarity'      : item.element.rarity.name,
							'duration'    : item.duration,
							'amount'      : result.amount
						})
				except Exception as err:
					pass 

				try:
					result = ElementActivation.objects.get(player=Player, element=item.element)
					if (result.expiration > now):
						response['active_item'].append({
							'name_id'     : item.element.name_id,
							'name'        : item.element.name,
							'description' : item.element.description,
							'rarity'      : item.element.rarity.name,
							'expiration'  : result.expiration,
						})
				except:
					pass

			return JsonResponse(response)
	except:
		pass
	raise PermissionDenied()

@csrf_exempt
def ShipDetails(request):
	try:
		Player = CheckStatusSession(request)
		CurrentSession = ActiveSession.objects.get(player=Player, spaceship__isnull=False)
		if (Player):
			response = {
				"ship_id": CurrentSession.spaceship.ShipID
			}
			return JsonResponse(response)
	except:
		pass
	raise PermissionDenied()

@csrf_exempt
def RefineElement(request):
	try:
		Player = CheckStatusSession(request)
		if (Player):
			# Comeca aqui
			response = {'status':'success'}
			return JsonResponse(response)
	except Exception as err:
		pass
	raise PermissionDenied()