"""surp_payout URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
<<<<<<< HEAD
# from django.urls import re_path
from django.contrib import admin

from payout import views
# from payout.models import Person  # работает
# from . import utils
# from utils import generate_user  # не работает
# print(utils.generate_user())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('proba', views.index),
    url(r'^persons/(?P<person_id>\d+)/', views.persons),  ###
=======
from django.contrib import admin

from payout import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^persons/(?P<person_id>\d+)/', views.persons),
    url(r'action', views.action_func),
    url(r'', views.index),
>>>>>>> Начальный коммит

]
