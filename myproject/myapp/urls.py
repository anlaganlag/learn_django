from django.urls import  include, path
from .views import hello,viewArticle

urlpatterns = [

        path('',  hello, name = 'hello'),
        path('article/<int:articleId>',viewArticle  , name = 'view'),
        

    ]