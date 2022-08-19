from django.contrib import admin
from .views import export_selected_objects

from .models import Bakery, Point, UserPoint

admin.site.register(Bakery)
admin.site.register(Point)
admin.site.register(UserPoint)
admin.site.add_action(export_selected_objects, 'export selected objects')
