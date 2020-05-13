from django.http import HttpResponse
from .models import Pizza

def index(request, pid):
    pizza = Pizza.objects.get(id=pid)
    return HttpResponse(
            
    f" <p>id: {pizza.id}</p> <p>title: {pizza.title}</p><p> description: {pizza.description}</p>"
            
    )
