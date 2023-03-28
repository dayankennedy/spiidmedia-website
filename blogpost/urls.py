from django.urls import path
from .views import like_post, unlike_post
from.import views 

urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('donate/', views.donate, name='donate'),
    path('mission/', views.mission, name='mission'),
    path('news/', views.blog, name='blog'),
    path('post/<int:post_id>/like/', like_post, name='like_post'),
    path('post/<int:post_id>/unlike/', unlike_post, name='unlike_post'),
]
