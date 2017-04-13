"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from blog_admin import views

from blog_admin.views_dir import authentication

urlpatterns = [
    url(r'^auth_login/', authentication.auth_login),
    url(r'^auth_logout/', authentication.auth_logout),
    url(r'^article/', views.article),
    url(r'^column/', views.column),

    url(r'^tags/add/', views.tags_add),
    url(r'^tags/', views.tags),


    url(r'', views.index),

]
