from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact.html', views.contact, name='contact'),
    path('service.html', views.service, name='service'),
    path('pricing.html', views.pricing, name='pricing'),
    path('about.html', views.about, name='about'),
    path('health_blog.html', views.health_blog, name='health_blog'),
    path('corona_blog.html', views.corona_blog, name='corona_blog'),
    path('appointment.html', views.appointment, name='appointment'),
]
