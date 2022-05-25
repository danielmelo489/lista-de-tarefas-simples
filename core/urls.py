from .views import Home, Task_create, Task_delete
from django.urls import path

app_name = 'core'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('create/', Task_create.as_view(), name='task_create'),
    path('<int:id>/', Task_delete.as_view(), name='task_delete'),
]