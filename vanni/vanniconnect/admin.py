from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Request

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'request_type', 'severity', 'submitted_at')
    list_filter = ('severity', 'submitted_at')
