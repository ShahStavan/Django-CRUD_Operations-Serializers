from django.urls import path
from django.urls import path
from . import views
urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('task-list/', views.taskList, name='taskList'),
    path('task-detail/<str:pk>/', views.taskDetail, name='taskDetail'),
    path('create/',views.taskCreate,name="taskCreate"),
    path('update/<str:pk>/', views.taskUpdate, name='taskUpdate'),
    path('delete/<str:pk>/', views.taskDelete, name='taskDelete'),
]

