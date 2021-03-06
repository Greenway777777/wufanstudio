"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]"""
from django.conf.urls import url
from HelloWorld.view import hello
from HelloWorld.view import hello2
from HelloWorld.testdb import testdb
from HelloWorld.testdb import testdb2
from HelloWorld.testdb import testdb3
from HelloWorld.testdb import testdb4
from HelloWorld import search
from HelloWorld import search2
from TestModel.views import login
from TestModel.views import index
from django.contrib import admin
from django.urls import path


urlpatterns = [
        path('admin/', admin.site.urls),
        url('^hello/$', hello),
        url('^hello/(\d{1,2})/$', hello2),
        url('^testdb/$', testdb),
        url('^testdb2/$', testdb2),
        url('^testdb3/$', testdb3),
        url('^testdb4/$', testdb4),
        url(r'^search/$', search.search),
        url(r'^search-form/$', search.search_form),
        url(r'^search-post/$', search2.search_post),
        url(r'^login/$', login),
        url(r'^index/$', index),
]