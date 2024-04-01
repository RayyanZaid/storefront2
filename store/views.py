from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.



# Serializer - Product object --> dict

# REST Framework has class called JSON Renderer 
    # Method: render(dict) --> JSON object
    
@api_view()
def product_list(request):

    return Response('ok')



@api_view()
def product_detail(request, id):

    return Response(id)