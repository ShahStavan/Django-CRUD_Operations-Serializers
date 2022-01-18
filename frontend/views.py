from multiprocessing import context
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Post


# Create your views here.
def list(request):
    return render(request, 'frontend/list.html')
def login(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            response = redirect('frontend/list.html')
            return response

    else:
        form = UserCreationForm()
    
    return render(request, 'userapp/index.html', {'form':form})
    return render(request, 'frontend/login.html')
def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'frontend/blog.html',context)
