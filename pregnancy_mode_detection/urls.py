"""pregnancy_mode_detection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from pregnancy_mode_detection.views import templateexample,form,addreport,showreport,report,login
urlpatterns = [
    path('', login,name="login"),
    path('admin/', admin.site.urls),
    path('template/', templateexample),
    path('addreport/', addreport,name="addreport"),
    path('reports/', showreport,name="showreports"),
    path('report/<id>/', report,name="report")
]
