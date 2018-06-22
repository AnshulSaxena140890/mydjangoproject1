# -*- coding: utf-8 -*-


from django.shortcuts import render

# Create your views here.
def index(request):
    dict1={'text1':'Hello world how are you','num1':100}
    return  render(request,'basic_app/index.html',dict1)

def other(request):
    return  render(request,'basic_app/other.html')

def relative(request):
    return  render(request,'basic_app/relative_url_page.html')

