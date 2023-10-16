from django.shortcuts import render ,HttpResponse
from .models import Item

# Create your views here.
def hello(request):
    item_list=Item.objects.all()
    
    return HttpResponse(item_list)
def item(request):
    return HttpResponse('this is an item view')

