from django.contrib import admin

from .models import Invoice, Item, Team

admin.site.register(Invoice)
admin.site.register(Item)
admin.site.register(Team)