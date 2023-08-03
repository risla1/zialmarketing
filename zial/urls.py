from django.urls import path
import zial.views

urlpatterns = [
    path('', zial.views.home, name='home'),
path('contact', zial.views.home, name='contact'),
path('register', zial.views.register, name='register'),
path('catalogue', zial.views.catalogue, name='catalogue'),
]