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
    


# Deserializing: When user types in info for a Product, convert that to product object for the database
    # 1) Need to pass array of HTTP methods to API View Decorator (for the POST)

@api_view(['GET' , 'POST'])
def product_list(request):

    if request.method == 'GET':
        products_queryset = Product.objects.select_related('collection').all().order_by("pk")

        serializer = ProductSerializer(products_queryset, many=True, context={'request': request})

        productsDictionary = serializer.data
        return Response(productsDictionary)

    elif request.method == 'POST':
        # Deserialize

        deserializer = ProductSerializer(data=request.data)

        # Need to validate data

        if deserializer.is_valid():
        
            deserializer.save()
            return Response(deserializer.data, status=status.HTTP_201_CREATED)
        else:
             
            return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    


# PUT - to update all fields
# PATCH - to update subset of fields
@api_view(['GET' , 'PUT' , 'PATCH'])
def product_detail(request, id):
    
    # instance

    product = get_object_or_404(Product, pk=id)

    if request.method == 'GET':    
        

        serializer = ProductSerializer(product,context={'request': request})

        productDictionary : dict = serializer.data
        # this dictionary is converted to JSON object under the hood

        return Response(productDictionary)

    elif request.method == 'PUT':

        # pass product instance
        deserializer = ProductSerializer(product, data=request.data)
        deserializer.is_valid(raise_exception=True)
        deserializer.save()

        return Response(deserializer.data)
    

    

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