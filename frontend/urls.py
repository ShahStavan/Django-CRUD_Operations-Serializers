from django.urls import path
from . import views
urlpatterns = [
    path('', views.list, name='list'),
    path('login/', views.login, name='login'),
    path('blog/', views.blog, name='blog'),
]