from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    text = """<h1>welcome to my app !</h1>"""
    return HttpResponse(text)

# Create your views here.

def viewArticle(request, articleId=None,year=None,month=None):
    if  articleId:
        text = f"Displaying article Number : {articleId}"
    elif 1000<year<=2038 and 0<=month<=12:
        text = f"Displaying articles of year month: {year}/{month}/"
    else:
        text = f" Input  Arguments : {year}/{month}/"
    return HttpResponse(text)