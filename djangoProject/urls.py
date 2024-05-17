"""
URL configuration for djangoProject project.

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
from django.urls import path, include
from djangoProject.views import musicians, add_musician, add_album, albums
urlpatterns = [
    path('admin/', admin.site.urls),
    path('musicians/', musicians, name='musicians'),
    path('add_musician/', add_musician, name='add_musicians'),
    path('add_album/', add_album, name='add_album'),
    path('albums/', albums, name='albums')
]
