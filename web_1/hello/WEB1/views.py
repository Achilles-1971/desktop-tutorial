from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import *
from WEB1.forms import UserForm
def index(request):
    userform = UserForm()
    return render(request, "WEB1/index.html", {"form": userform})
def about(request):
    return HttpResponse("About")
def contact(request):
    return HttpResponseRedirect("/about")
def details(request):
    return HttpResponsePermanentRedirect("/")