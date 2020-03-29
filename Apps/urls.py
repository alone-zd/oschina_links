"""
# @Time: 2020/3/28 21:58
# @Author: Alone
# @File: urls.py
"""
from django.urls import path
from Apps.views import index

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),

]
