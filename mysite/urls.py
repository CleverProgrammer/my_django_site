"""mysite URL Configuration

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
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 127.0.0.1:8000/accounts/login --> local
    # mydjangosite.com/accounts/login --> online
    path('accounts/login/', auth_views.login, name='login'),

    # 127.0.0.1:8000/accounts/logout --> local
    # mydjangosite.com/accounts/logout --> online
    path('accounts/logout/', view=auth_views.logout, name='logout', kwargs={'next_page': 'post_list'}),

    # 127.0.0.1:8000
    path('', include('blog.urls')),
]
