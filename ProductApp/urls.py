

from django.urls import path,re_path
from ProductApp import views

urlpatterns = [
    re_path(r'^$',views.input),
    re_path(r'^display$',views.display)
]
