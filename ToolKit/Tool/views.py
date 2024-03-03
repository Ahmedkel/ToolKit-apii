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


@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
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
        # Check if the category exists, if not create it
        category_name = request.data.get('category_name')
        category, created = Category.objects.get_or_create(name=category_name)

        # Update the request data with the category instance
        mutable = request.POST._mutable
        request.POST._mutable = True
        request.data['category'] = category.id
        request.POST._mutable = mutable
        
        serializer = website_ToolsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
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


@api_view(['POST'])
def signup(request):
    """
    signup view for the user. This
    view will return a token and the
    user data if the user is created.
    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})
    return Response(serializer.errors, status=status.HTTP_200_OK)

@api_view(['POST'])
def login(request):
    """
    Login view for the user. This
    view will return a token and the
    user data if the user is found.
    """
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed!")
