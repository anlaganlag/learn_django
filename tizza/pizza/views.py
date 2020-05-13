import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Pizza
from random import randint,sample


from django.shortcuts import render
from django.views import View


class GetTenPizzasView(View):
    template_name = 'ten_pizzas.html'

    def get(self, request)
        pizzas = Pizza.objects.order_by('?')[:10]
        return render(request, self.template_name, {'pizzas': pizzas})


@login_required
def home(request,pid):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_pizza = Pizza.objects.create(
            titile = data['title'],
            description = data['description'],
            creator = request.user,
        )
        new_pizza.save()
        return HttpResponse( f" <p>id: {new_pizza.id}</p> <p>title: {new_pizza.title}</p><p> description: {new_pizza.description}</p>" )
    elif request.method == 'GET':
        pizza = Pizza.objects.get(id=pid)
        return HttpResponse( f" <p>id: {pizza.id}</p> <p>title: {pizza.title}</p><p> description: {pizza.description}</p>" )
    elif request.method == 'DELETE':
        if 'can_delete' in request.user.user_permissions:
            pizza = Pizza.objects.get(id=pid)
            pizza.delete()
            return HttpResponse( content={
                'id': pizza.id,
            })
        else:
            return HttpResponse(status_code=404)

    


def index(request, pid):
    try:
        pizza = Pizza.objects.get(id=pid)
        return HttpResponse( f" <p>id: {pizza.id}</p> <p>title: {pizza.title}</p><p> description: {pizza.description}</p>" )
    except:
        return HttpResponse(f"<p>status: error</p> <p>message: pizza_id={pid} not found</p>")


def randoms(request,random_times=1):
    text = ""
    object_nums = len(Pizza.objects.all())
    if random_times>object_nums:
        text+=f"您選擇的隨機的次數{random_times}!<br>大於當前存在的pizza數量{object_nums},<br>故只隨機顯示{object_nums}個pizza!!"
        random_times =object_nums
    pid_list =  sample(range(1,object_nums+1),random_times)
    for  i in pid_list:
        try:
            pizza = Pizza.objects.get(id=i)
            text += f" <p>id: {pizza.id}</p> <p>title: {pizza.title}</p><p> description: {pizza.description}</p><br><br>" 
        except:
            text +=f"<p>id:{i}</p><p>status: error</p> <p>message: pizza_id={i} not found</p><br><br>"
    return HttpResponse(text)

    
def logged(request):
    return  HttpResponse("Have successful logged in!")


    

    


    