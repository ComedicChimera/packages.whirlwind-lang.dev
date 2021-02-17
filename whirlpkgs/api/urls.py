from django.urls import path

from .util import route_table

urlpatterns = [path(pathname, func) for pathname, func in route_table.items()]