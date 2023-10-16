"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from api.views import demo, demo1, demo2, DemoView, DemoView1, WeaponView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', demo),
    path('demo1/', demo1),
    path('demo2/', demo2),
    path('demo3/', DemoView.as_view()),
    path('demo4/', DemoView1.as_view()),
    path('weapon/<pk>/', WeaponView.as_view()),
]
