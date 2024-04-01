from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# from current folder
from .models import Product
from .serializers import ProductSerializer

# Create your views here.



# Serializer - Product object --> dict

# REST Framework has class called JSON Renderer 
    # Method: render(dict) --> JSON object
    
@api_view()
def product_list(request):

    products_queryset = Product.objects.select_related('collection').all().order_by("pk")

    serializer = ProductSerializer(products_queryset, many=True, context={'request': request})

    productsDictionary = serializer.data
    return Response(productsDictionary)



@api_view()
def product_detail(request, id):
    

        product = get_object_or_404(Product, pk=id)

        serializer = ProductSerializer(product,context={'request': request})

        productDictionary : dict = serializer.data
        # this dictionary is converted to JSON object under the hood

        return Response(productDictionary)
    

    

    # try:
    #     product = Product.objects.get(pk=id)

    #     serializer = ProductSerializer(product)

    #     productDictionary : dict = serializer.data
    #     # this dictionary is converted to JSON object under the hood

    #     return Response(productDictionary)
    
    # except Product.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

@api_view()
def collection_detail(request, pk):
      
      return Response('ok')