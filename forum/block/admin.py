from django.contrib import admin
from .models import Block

class BlockAdmin(admin.ModelAdmin):
    list_display=("name","desc","manager")
admin.site.register(Block,BlockAdmin)
# Register your models here.
