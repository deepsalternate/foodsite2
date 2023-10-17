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
    
]
