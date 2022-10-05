from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(ResultLog)
class ResultLogAdmin(admin.ModelAdmin):
    list_display = ('country','state','created_at')
    def country(self,obj):
        return f"{'USA'}"
    def state(self,obj):
        return f"{'California'}"