from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('getmenu/',  views.index, name='index'),
    path('adduser/<int:code>/<int:phone>/', views.getuser, name='getuser'),
    path('sendsms/', views.sendsms, name='sendsms')
]
