from django.contrib import admin
from aquarium_app.models import CategorySub


@admin.register(CategorySub)
class CategorySubAdmin(admin.ModelAdmin):
    pass
