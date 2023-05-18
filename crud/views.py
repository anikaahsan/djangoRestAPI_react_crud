from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import status
from . models import Product
from .serializer import ProductSerializer



@api_view(['GET','POST'])
def product(request):
    #retrieve
    if request.method=="GET":
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data)


    ##create
    if request.method=='POST':
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():  
            ##serializer.is_valid(raise_exception=True)
            serializer.save()
            print(serializer.validated_data)
            print('dataaaaaaa')
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def product_detail(request,pk):
    product=Product.objects.get(pk=pk)

    if request.method=='GET':
        serializer=ProductSerializer(product)
        return Response(serializer.data)
    
    if request.method=='PUT':
         serializer=ProductSerializer(product,data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return Response(serializer.data,status=status.HTTP_200_OK)
    
      
    if request.method=='DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['PUT'])
def product_update(request,pk):
    if request.method=='PUT':
         serializer=ProductSerializer(product,data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return Response(serializer.data,status=status.HTTP_200_OK)
    

@api_view(['delete'])    
def product_delete(request,pk):
    product=Product.objects.get(pk=pk)
    if request.method=='DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)