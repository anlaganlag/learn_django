from django.urls import include,path
from .views import index,randoms
urlpatterns = [
  path('<int:pid>/', index, name='pizza'),
  path('randoms/', randoms, name='randoms'),
  path('randoms/<int:random_times>', randoms, name='randoms'),

]
