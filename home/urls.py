from django.urls import path
from . import views
from home.views import *

urlpatterns = [
    path('',views.homepage,name = "homepage" ),
    path('about',views.about,name="about"),
    path('why/',views.whypage,name='whypage')
]
