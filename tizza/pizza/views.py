from django.http import HttpResponse
from .models import Pizza
from random import randint,sample

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

    


    

    


    