
from django import forms
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver

# Create your models here.

# we're going to need tables for rooms, courses, professors, and...?

class User(models.Model):
	uname = models.CharField(max_length = 128)
	hashed_pass = models.CharField(max_length = 128)
	action = models.CharField(max_length=64)
    ip = models.GenericIPAddressField(null=True)
	
	def __unicode__(self):
		return '{0} - {1} - {2}'.format(self.action, self.uname, self.ip)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.action, self.uname, self.ip)


@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):  
    ip = request.META.get('REMOTE_ADDR')
    AuditEntry.objects.create(action='user_logged_in', ip=ip, uname=user.uname)


@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):  
    ip = request.META.get('REMOTE_ADDR')
    AuditEntry.objects.create(action='user_logged_out', ip=ip, uname=user.uname)


@receiver(user_login_failed)
def user_login_failed_callback(sender, credentials, **kwargs):
    AuditEntry.objects.create(action='user_login_failed', uname=credentials.get('username', None))


