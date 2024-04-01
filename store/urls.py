from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_detail),   
                                                        # each path function maps url --> view, name= paramaeter is to name the mapping
    path('collections/<int:pk>/', views.collection_detail, name='collection-detail')
]