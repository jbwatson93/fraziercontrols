from django.contrib import admin
from aquarium_app.models import Actuator


@admin.register(Actuator)
class ActuatorAdmin(admin.ModelAdmin):
    pass
