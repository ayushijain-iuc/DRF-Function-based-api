from django.shortcuts import render
from . serializer import BookSerializer
from . models import Book
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
@api_view(['GET','POST','PUT','DELETE'])
def booklistapi(request,pk=None):
    if request.method=="GET":
        id=pk
        if id is not None:
            stu=Book.objects.get(id=id)
            p=BookSerializer(stu)
            return Response(p.data)
            
            
        book=Book.objects.all()
        p=BookSerializer(book,many=True)
        return Response(p.data)
    
    if request.method=="POST":
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    if request.method=="PUT":
        id=pk
        # id=request.data.get('id')
        stu = Book.objects.get(pk=id)
        serializer=BookSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=="DELETE":
        id=pk
        # id=request.data.get('id')
        stu = Book.objects.get(pk=id)
        stu.delete()
        return Response(status=status.HTTP_201_CREATED)
        
        
        
    
            
            
        
        
    
# Create your views here.
