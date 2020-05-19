
from django.urls import path
from . import views

app_name = 'video'
urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('search/', views.SearchiListView.as_view(), name='search'),
]