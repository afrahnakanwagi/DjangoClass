"""
URL configuration for HelloWorld project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Home.views import index
from Home.views import home
from about.views import about
from Home.views import login
from Home.views import register
from Home.views import calculator
from Home.views import todo
from Home.views import contact





urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('home/',home),
    path('about/', about),
    path('login/', login),
    path('register/', register),
    path('calculator/', calculator),
    path('contact/', contact),
    path('todo/', todo),
]   
