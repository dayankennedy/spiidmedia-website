from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *


# base view

def base(request):

    return render(request, 'blogpost/base.html')

def home(request):
    return render(request, 'blogpost/home.html')

# about vied
def about(request):

    return render(request, 'blogpost/about.html')

# contact view
def contact(request):
    return render(request, 'blogpost/contact.html')

# Donate view
def donate(request):

    return render(request, 'blogpost/donate.html')
# mission view
def mission(request):
    return render(request, 'blogpost/mission.html')

# blog view
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blogpost/blog.html',{'posts': posts})

# like and unlike views
@login_required
def like_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    Like.objects.create(user=request.user, post=post)
    return redirect('post_detail', post_id=post.id)

@login_required
def unlike_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    Like.objects.filter(user=request.user, post=post).delete()
    return redirect('post_detail', post_id=post.id)


