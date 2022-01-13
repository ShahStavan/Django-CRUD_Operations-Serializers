from django.urls import path,include
from . import views
urlpatterns =[
    path('',views.article_list,name='article_list'),
    path('articles/<int:year>/',views.article_year,name='article_year'),
    path('articles/<int:year>/<int:month>/<int:pk>/',views.article_detail,name='article_detail'),
]