from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import loader
from django import forms
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import PerformSpellCheck
import json 
import re
import time
import datetime

site_hdr = "AppSec"


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def index(request):
    return render(request, 'index.html', {'header': site_hdr})

@csrf_protect
def performspellcheck(request):
	request_dict = request.POST.dict()
	addToDb(request)
	data = request_dict['data']
	all_words = createDictionary()
	error_list = checkFile(data, all_words)
	formatted_list = format(error_list)
	json_data = json.dumps({'errors': formatted_list})
	http_response = HttpResponse(json_data)
	http_response['X-Frame-Options'] = 'deny'
	http_response['X-Content-Type-Options'] = 'nosniff'
	http_response['X-XSS-Protection'] = '1; mode=block'
	return http_response

def addToDb(request):
	if request.user.is_authenticated:
		requestLog = PerformSpellCheck()
		requestLog.uname = request.user.username
		requestLog.created_at = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
		requestLog.file_preview = request.POST.dict()['data']
		requestLog.save()

def createDictionary():
	lines = [line.rstrip('\n').lower() for line in open('/home/djangoappsec/appsec/data/dictionary.txt')]
	all_words = set(lines)
	return all_words

def checkFile(fileContent, all_words):
	file_lines = fileContent.strip().split("\\n")
	ret_list = []
	for line in file_lines:
		line = cleanLine(line)
		split_line = line.split(" ")
		for word in split_line:
			if (not checkWord(word, all_words)):
				ret_list.append(word)
	return ret_list

def cleanLine(line):
	line = line.replace("\"", "").replace("-", " ").lower()
	line = re.sub("[^a-z\\sA-Z]", "", line)
	return line

def checkWord(word, all_words): 
	if word in all_words:
		return True
	return False

def format(error_list):
	new_list = []
	for word in error_list:
		new_list.append(" " + word)
	return new_list
