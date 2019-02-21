from django.contrib import admin
from aquarium_app.models import Cabinet


@admin.register(Cabinet)
class CabinetAdmin(admin.ModelAdmin):
    pass
