from django.urls import include,path
from .views import index,random,randoms


urlpatterns = [
  path('<int:pid>/', index, name='pizza'),
  path('random/', random, name='random'),
  path('randoms/', randoms, name='randoms'),
  path('randoms/<int:random_times>', randoms, name='randoms'),

]
