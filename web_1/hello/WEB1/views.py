from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.template.response import TemplateResponse
def index(request):
    header = "Персональные данные" # обычная переменная
    langs = ["Английский", "Немецкий", "Испанский"] # массив
    user = {"name": "Максим,", "age": 30} # словарь
    addr = ("Виноградная", 23, 45) # кортеж
    data = {"header": header, "langs": langs, "user": user, "address":
    addr}
    return TemplateResponse(request, "index.html", data)
def about(request):
    return HttpResponse("About")
def contact(request):
    return HttpResponseRedirect("/about")
def details(request):
    return HttpResponsePermanentRedirect("/")