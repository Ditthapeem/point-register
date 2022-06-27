from multiprocessing import context
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

from .models import Bakery


def index(request):
    bakery_list = Bakery.objects.all()
    context = {'bakery_list': bakery_list}
    return render(request, 'point_register/index.html', context)
