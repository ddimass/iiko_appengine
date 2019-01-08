from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import random

from .models import Iiko, Commit
# Create your views here.
def index(request):
    resp = JsonResponse(Iiko.get_menu())
    resp["Access-Control-Allow-Origin"] = "*"
    return resp


def getuser(request, code, phone):
    comm = Commit.objects.get(phone = phone)
    if (comm.code == code):
        comm.delete()
        resp =JsonResponse({'userid': Iiko.add_user('Aleks', '79211058291')})
        resp["Access-Control-Allow-Origin"] = "*"
        return resp
    else:
        resp = {'error': 'Verification code is invalid'}
        return resp


def sendsms(request):
    s = ''
    for i in range(1,8):
        s = s + str(random.randint(1,9))
    obj = Commit.objects.filter(phone = ph)
    comm = Commit(phone = '79211058291', code=s)
    comm.save()
    resp =JsonResponse(Iiko.sendsms('79211058291', 'Ваш проверочный код - ' + s,'MediaGramma'))
    resp["Access-Control-Allow-Origin"] = "*"
    return resp

