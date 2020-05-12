from django.urls import  include, path
from .views import hello

urlpatterns = [

        path('',  hello, name = 'hello'),
        

    ]