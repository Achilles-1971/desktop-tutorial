from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import *
from WEB1.forms import UserForm
def index(request):
    if request.method == "POST":
        name = request.POST.get("name") # получить значения поля Имя
        age = request.POST.get("age") # значения поля Возраст
        output = "<h2>Пользователь</h2><h3>Имя - {0}, Возраст – {1}</h3>".format(name, age)
        return HttpResponse(output)
    else:
        userform = UserForm()
        return render(request, "WEB1/index.html", {"form": userform})
def about(request):
    return HttpResponse("About")
def contact(request):
    return HttpResponseRedirect("/about")
def details(request):
    return HttpResponsePermanentRedirect("/")