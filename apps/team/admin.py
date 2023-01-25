from django.contrib import admin

from .models import Team

admin.site.unregister(Team)
admin.site.register(Team)