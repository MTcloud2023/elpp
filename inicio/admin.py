from django.contrib import admin

# Register your models here.
from .models import UserSurvey

@admin.register(UserSurvey)
class UserSurveyAdmin(admin.ModelAdmin):
    list_display = ("nombre", "opcion_principal", "fecha_registro")
    search_fields = ("nombre",)
    list_filter = ("opcion_principal", "fecha_registro")
