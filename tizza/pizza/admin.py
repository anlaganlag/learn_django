from django.contrib import admin
from .models import Pizza ,Pizzeria,Likes

class PizzaAdmin(admin.ModelAdmin):
  pass

admin.site.register(Pizza,PizzaAdmin)
admin.site.register(Pizzeria)
admin.site.register(Likes)
