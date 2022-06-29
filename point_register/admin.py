from django.contrib import admin

from .models import Bakery, Point, Type

admin.site.register(Bakery)
admin.site.register(Point)
admin.site.register(Type)
