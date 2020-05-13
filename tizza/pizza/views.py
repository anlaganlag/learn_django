from django.http import HttpResponse
from .models import Pizza
from random import randint

def index(request, pid):
    try:
        pizza = Pizza.objects.get(id=pid)
        return HttpResponse( f" <p>id: {pizza.id}</p> <p>title: {pizza.title}</p><p> description: {pizza.description}</p>" )
    except:
        return HttpResponse(f"<p>status: error</p> <p>message: pizza_id={pid} not found</p>")

def random(request):
    try:
        pid = randint(1,6)
        pizza = Pizza.objects.get(id=pid)
        return HttpResponse( f" <p>id: {pizza.id}</p> <p>title: {pizza.title}</p><p> description: {pizza.description}</p>" )
    except:
        return HttpResponse(f"<p>status: error</p> <p>message: pizza_id={pid} not found</p>")

    


    
