from ElementSystem.models import Rarity, Element, Ore, Item, ElementRefination, ElementSpawn, ElementOwner, ElementActivation
from django.contrib import admin

# Register your models here.

admin.site.register(Rarity)
admin.site.register(Element)
admin.site.register(Ore)
admin.site.register(Item)
admin.site.register(ElementRefination)
admin.site.register(ElementSpawn)
admin.site.register(ElementOwner)
admin.site.register(ElementActivation)