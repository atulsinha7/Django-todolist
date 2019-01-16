"""Project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from todolist import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/$', views.getUsers),
    url(r'^users/(?P<user_id>\d+)/$', views.getList),
    url(r'^create_user/', views.create),
    # url(r'^update_list/(?P<user_id>\d+)/$', views.update),
    url(r'^update_task/(?P<user_id>\d+)/(?P<tname>\w+)/$', views.update_task),
    url(r'^delete_user/(?P<user_id>\d+)/$', views.del_user)
]
