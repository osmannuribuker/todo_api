from django.contrib import admin
from django.urls import path

from apps.api.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', TodoCreate.as_view(), name='create_todo'),
    path('todos/', TodoList.as_view(), name='get_all_todo'),
    path('todo/<int:pk>', TodoDetail.as_view(), name='single_todo')
]
