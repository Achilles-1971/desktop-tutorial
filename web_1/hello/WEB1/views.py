from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.template.response import TemplateResponse
def index(request):
    return render(request, "WEB1/index.html")
def about(request):
    return HttpResponse("About")
def contact(request):
    return HttpResponseRedirect("/about")
def details(request):
    return HttpResponsePermanentRedirect("/")