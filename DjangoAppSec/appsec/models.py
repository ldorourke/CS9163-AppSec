from django import forms
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from django.utils import timezone


# Create your models here.

# we're going to need tables for rooms, courses, professors, and...?

class PerformSpellCheck(models.Model):
	uname = models.CharField(max_length = 128)
	created_at = models.CharField(max_length = 128)
	file_preview = models.CharField(max_length = 1024)


class LoginAttempt(models.Model):
	action = models.CharField(max_length=64)
	ip = models.GenericIPAddressField(null=True)
	timestamp = models.DateTimeField(default=timezone.now)
	uname = models.CharField(max_length=256, null=True)
	
	def __unicode__(self):
		return '{0} - {1} - {2}'.format(self.action, self.uname, self.ip)

	def __str__(self):
		return '{0} - {1} - {2}'.format(self.action, self.uname, self.ip)

@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):  
	ip = request.META.get('REMOTE_ADDR')
	LoginAttempt.objects.create(action='UserLogin', ip=ip, uname=user.username)


@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):  
	ip = request.META.get('REMOTE_ADDR')
	LoginAttempt.objects.create(action='UserLogout', ip=ip, uname=user.username)


@receiver(user_login_failed)
def user_login_failed_callback(sender, request, credentials, **kwargs):
	ip = request.META.get('REMOTE_ADDR')
	LoginAttempt.objects.create(action='FailedUserLogin', ip=ip, uname=credentials.get('username', None))


