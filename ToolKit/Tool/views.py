from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import website_Tools
from .serializers import website_ToolsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(['GET', 'POST'])
def website_ToolsList(request, format=None):
    """
    This function is used to list all the website
    tools and also to add a new website tool.
    """
    if request.method == 'GET':
        website_tools = website_Tools.objects.all()
        serializer = website_ToolsSerializer(website_tools, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = website_ToolsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def website_ToolsDetail(request, id, format=None):
    """
    This function is used to retrieve a single
    website tool by its id.
    """
    try:
        website_tool = website_Tools.objects.get(id=id)
    except website_Tools.DoesNotExist:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = website_ToolsSerializer(website_tool)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = website_ToolsSerializer(website_tool, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        website_tool.delete()
        return Response(status=204)
