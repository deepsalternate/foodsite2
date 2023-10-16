from django.shortcuts import render ,HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('Hello World')
def item(request):
    return HttpResponse('this is an item view')

