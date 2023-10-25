from django.shortcuts import render ,HttpResponse ,redirect
from .models import Item 
from django.template import loader
from .forms import ItemForm

# Create your views here.
def hello(request):
    item_list=Item.objects.all()
    # template=loader.get_template('food/index.html')
    context={
        'item_list':item_list,
    }
    return render(request,'food/index.html',context)
    #  " does the same as above "return HttpResponse(template.render(context,request))
def item(request):
    return HttpResponse('this is an item view')

def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    context={
        'item':item,
    }
    # return HttpResponse ("this is an item view : %s" % item_id )
    return render(request,'food/detail.html',context)


def create_item(request):
    form=ItemForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item-form.html',{'form':form})
    
