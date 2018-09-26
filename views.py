from django.http import HttpResponse
from dajngo.shortcuts import redirect

def index(request):

	return HttpResponse("index")

def login(request):
	return redirect("/index")
