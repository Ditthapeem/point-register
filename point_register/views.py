from multiprocessing import context
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

from .models import Bakery


def index(request):
    return render(request, 'point_register/index.html')
