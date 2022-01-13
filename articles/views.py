from django.db import connections
from django.shortcuts import render
from .models import article

# Create your views here.
def article_list(request):
    articles = article.objects.order_by('id')[:5]
    return render(request, 'articles/article_list.html', {'articles':articles})
def article_year(request, year):
    articles = article.objects.filter(pub_date__year=year)
    return render(request, 'articles/article_list.html', {'articles':articles})
def article_detail(request, year, month, pk):
    myarticle = article.objects.get(pub_date__year=year, pub_date__month=month, pk=pk)
    return render(request, 'articles/article_detail.html', {'article':myarticle})
