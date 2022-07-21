from csv import writer
from django.shortcuts import render
from .form import CreateUserForm
from .add_point_form import AddPointForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
import csv
from django.contrib import admin


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

def user_register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            u = UserPoint(name=user, point=0)
            u.save()
            context = {"user_and_point": u}
            return render(request,'point_register/user_point.html', context)
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    context = {'form':form }
    return render(request,'point_register/user_register.html', context)

def user_point(request):
    pass

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            u = UserPoint(name=user, point=0)
            u.save()
            messages.info(request, 'Member Registration successfully!')
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    context = {'form':form }
    return render(request,'point_register/register.html', context)

def export_selected_objects(modeladmin, request, queryset):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
    )
    writer = csv.writer(response)
    field = [field.name for field in queryset[0]._meta.get_fields()]
    print(field)
    writer.writerow(field)
    for i in queryset:
        element = []
        for j in field:
            try:
                element.append(get_object(i, j))
            except:
                element.append("#N/A")
                pass
        writer.writerow(element)
    return response

def get_object(someobject, string):
    return getattr(someobject,string)
        