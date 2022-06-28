from multiprocessing import context
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

from .models import Bakery


def index(request):
    return render(request, 'point_register/index.html')

def bakery_detail(request):
    bakery_list = Bakery.objects.all()
    context = {'bakery_list': bakery_list}
    return render(request, 'point_register/bakery_detail.html', context)

def setbox_deatail(request):
    pass