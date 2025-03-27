from django.shortcuts import render
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
# Create your views here.

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True) # Convert to JSON
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data) # Now converted to Python data
        if serializer.is_valid():
            serializer.save()
            return Response({ "success" : "user created"}, status=status.HTTP_201_CREATED)
        
