
from django.shortcuts import render
from . import forms
from . import models
from django.http import HttpResponse
import re
import feedparser
# Create your views here.

def feed(request):
	return render(request, 'rss_feed/home.html')

def search(request):
    if 'i' in request.GET:
    	try:
    		d = feedparser.parse(request.GET['i'])
    		s = d['feed']['title'] + '\n' +  d['feed']['description'] + '\n'
    		for post in d.entries:
        		s = s + '\n' + post.title + '\n'
        		su = post.summary
        		su = re.sub('<.*?>','',su)
        		s = s + '\n' + su + '\n'
    		for post in d.entries:
    			s = s + post.link
    		models.link(url = request.GET['i']).save()
    		return HttpResponse(s)
    	except KeyError:
    		return HttpResponse("rss feed is not valid")
    else:
        message = 'form is empty'
        return HttpResponse(message)
