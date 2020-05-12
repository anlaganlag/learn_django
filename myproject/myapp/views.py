from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    text = """<h1>welcome to my app !</h1>"""
    return HttpResponse(text)

# Create your views here.

def viewArticle(request, articleId=None,year=None,month=None):
    if  articleId:
        text = f"Displaying article Number : {articleId}"
    else:
        text = f"Displaying articles of year month: {year}/{month}/"
    return HttpResponse(text)