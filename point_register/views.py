from multiprocessing import context
from django.shortcuts import render
from .form import CreateUserForm

from .models import Bakery, Type, Point, UserPoint


def index(request):
    return render(request, 'point_register/index.html')

def bakery_detail(request):
    type_list = Type.objects.all()
    context = { 'list': type_list}
    return render(request, 'point_register/bakery_detail.html', context)

def setbox_deatail(request):
    pass

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            u = UserPoint(name=user, point=0)
            u.save()
    context = {'form':form }
    return render(request,'point_register/register.html', context)