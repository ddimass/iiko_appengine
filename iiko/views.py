from django.shortcuts import render
from django.http import JsonResponse

from .models import Iiko
# Create your views here.
def index(request):
    resp = JsonResponse(Iiko.get_menu())
    resp["Access-Control-Allow-Origin"] = "*"
    return resp
