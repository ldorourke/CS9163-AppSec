from django.contrib import admin
from .models import PerformSpellCheck, LoginAttempt

admin.site.register(PerformSpellCheck)

@admin.register(LoginAttempt)
class LoginAttemptAdmin(admin.ModelAdmin):
    list_display = ['action', 'uname', 'timestamp', 'ip',]