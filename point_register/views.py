from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from .form import CreateUserForm
from .add_point_form import AddPointForm
from django.contrib.auth.models import User

from .models import Bakery, Type, Point, UserPoint


def index(request):
    return render(request, 'point_register/index.html')

def bakery_detail(request):
    type_list = Type.objects.all()
    point_list = Point.objects.all()
    context = { 'list': type_list,
                'point': point_list}
    return render(request, 'point_register/bakery_detail.html', context)

def setbox_detail(request):
    pass

def add_point(request):
    form = AddPointForm()
    if request.method == "POST":
        form = AddPointForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['mobile_number']
            user_point = form.cleaned_data['point']
            user_instance = User.objects.get(username=user_id)
            old_point = UserPoint.objects.get(name=user_instance)
            new_point = int(old_point.point) + int(user_point) 
            user_point = UserPoint.objects.filter(name=user_instance).update(point=new_point) 
            user_and_point = UserPoint.objects.get(name=user_instance)
            context = { "user_and_point": user_and_point }
            print(context)
            return render(request,'point_register/result.html', context)    
    context = {'form':form }
    return render(request,'point_register/bakery_detail.html', context)

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            u = UserPoint(name=user, point=0)
            u.save()
            return render(request, 'point_register/index.html')
    context = {'form':form }
    return render(request,'point_register/register.html', context)