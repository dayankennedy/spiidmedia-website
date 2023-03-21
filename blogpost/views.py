from django.shortcuts import render
from django.utils import timezone
from .models import *


# programming  coding 


def base(request):
    return render(request, 'blogpost/base.html')




def home(request):
    return render(request, 'blogpost/home.html')




def about(request):

    return render(request, 'blogpost/about.html')




def contact(request):
    return render(request, 'blogpost/contact.html')




def donate(request):

    return render(request, 'blogpost/donate.html')




def mission(request):
    return render(request, 'blogpost/mission.html')





def blog(request):
    posts = Post.objects.all()
    return render(request, 'blogpost/blog.html',{'posts': posts})
 


