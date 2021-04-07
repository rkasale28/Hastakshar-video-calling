from django.conf.urls import url
from django.urls import re_path

from . import views

urlpatterns = [
    url('index', views.index, name='index'),
    url('user-preferences', views.user_preferences, name='user-preferences'),
    re_path(r'call',views.call,name='call'),
    url('left',views.left,name='left'),


     url('test', views.call_test, name='call_test'),####Remove this
]