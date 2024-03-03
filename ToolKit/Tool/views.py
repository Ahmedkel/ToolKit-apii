from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from .models import website_Tools,Category
from .serializers import website_ToolsSerializer, UserSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from rest_framework import generics
from rest_framework.generics import RetrieveDestroyAPIView
from .models import website_Tools, Category
from .serializers import website_ToolsSerializer
from rest_framework.permissions import IsAdminUser

# @api_view(['GET', 'POST'])
# @permission_classes([IsAdminUser])
# def website_ToolsList(request, format=None):
#     """
#     This function is used to list all the website
#     tools and also to add a new website tool.
#     """
#     if request.method == 'GET':
#         website_tools = website_Tools.objects.all()
#         serializer = website_ToolsSerializer(website_tools, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         # Check if the category exists, if not create it
#         category_name = request.data.get('category_name')
#         category, created = Category.objects.get_or_create(name=category_name)

#         # Update the request data with the category instance
#         mutable = request.POST._mutable
#         request.POST._mutable = True
#         request.data['category'] = category.id
#         request.POST._mutable = mutable
        
#         serializer = website_ToolsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

class website_ToolsList(generics.ListCreateAPIView):
    """
    This class is used to list
    all the website tools and also
    to add a new website tool.
    """
    queryset = website_Tools.objects.all()
    serializer_class = website_ToolsSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        category_name = self.request.data.get('category_name')
        category, created = Category.objects.get_or_create(name=category_name)
        serializer.save(category=category)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAdminUser])
# def website_ToolsDetail(request, id, format=None):
#     """
#     This function is used to retrieve a single
#     website tool by its id.
#     """
#     try:
#         website_tool = website_Tools.objects.get(id=id)
#     except website_Tools.DoesNotExist:
#         return Response(status=404)
    
#     if request.method == 'GET':
#         serializer = website_ToolsSerializer(website_tool)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = website_ToolsSerializer(website_tool, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
    
#     elif request.method == 'DELETE':
#         website_tool.delete()
#         return Response(status=204)

class website_ToolsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This class is used to retrieve,
    update and delete a single
    website tool by its id.
    """
    queryset = website_Tools.objects.all()
    serializer_class = website_ToolsSerializer
    permission_classes = [IsAdminUser]

    def get_object(self):
        # Override the get_object method to handle the case where the category needs to be fetched or created
        instance = super().get_object()
        category_name = self.request.data.get('category_name', instance.category.name)
        instance.category, created = Category.objects.get_or_create(name=category_name)
        if not created:
            instance.save() # Save instance if category already exists but was not originally in the request data
        return instance
