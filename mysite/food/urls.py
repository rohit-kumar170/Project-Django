from django.urls import path
from . import views

app_name='food'
urlpatterns = [
    #/food/
    path('',views.IndexClassView.as_view(),name='index'),
    #/food/1
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
    #add item
    path("add/",views.CreateItem.as_view(),name="create_item"),
    #edit
    path('update/<int:id>/',views.update_item,name='update_item'),
    #delete
    path('delete/<int:id>/',views.delete_item,name='delete_item'),
]
