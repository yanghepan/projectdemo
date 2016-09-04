from django.contrib import admin
from .models import ActivateCode
class ActivateCodeAdmin(admin.ModelAdmin):
    list_display=("owner","code","expire_timestamp")
admin.site.register(ActivateCode,ActivateCodeAdmin)
# Register your models here.
