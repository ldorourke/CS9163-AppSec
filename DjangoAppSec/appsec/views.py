from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import loader
from django import forms
from django.views.decorators.csrf import csrf_protect
import re

site_hdr = "AppSec"

def index(request):
    return render(request, 'index.html', {'header': site_hdr})

@csrf_protect
def performspellcheck(request):
	request_dict = request.POST.dict()
	data = request_dict['data']
	all_words = createDictionary()
	error_list = checkFile(data, all_words)
	formatted_list = format(error_list)
	return JsonResponse({'errors': formatted_list})

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
