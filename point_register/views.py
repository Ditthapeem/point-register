from multiprocessing import context
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

from .models import Bakery, Type


def index(request):
    return render(request, 'point_register/index.html')

def bakery_detail(request):
    type_list = Type.objects.all()
    context = { 'list': type_list}
    print(context)
    return render(request, 'point_register/bakery_detail.html', context)

def setbox_deatail(request):
    pass