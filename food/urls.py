from .import views 
from django.urls  import path
app_name='food'
urlpatterns = [
    #/food/
    path('',views.hello,name='index'),
    #/food/item
    path('item/',views.item),
    #food/item_id    could be any key 1,2 ,3
    path('<int:item_id>/',views.detail,name="detail"),
    # add items
    path('add',views.create_item,name='create_item'),
    path('update/<int:id>',views.update_item,name='update_item'),
    path('delete/<int:id>',views.delete_item,name='delete_item')
    
    
]