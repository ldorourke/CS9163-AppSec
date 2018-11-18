from django.contrib import admin
from models import AuditEntr
# Register your models here.
from .models import User

admin.site.register(User)

@admin.register(AuditEntry)
class AuditEntryAdmin(admin.ModelAdmin):
    list_display = ['action', 'username', 'ip',]
    list_filter = ['action',]