from .models import Website_Tools,Category
from .serializers import Website_ToolsSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class Website_ToolsList(generics.ListCreateAPIView):
    """
    This class is used to list
    all the website tools and also
    to add a new website tool.
    """
    queryset = Website_Tools.objects.all()
    serializer_class = Website_ToolsSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        category_name = self.request.data.get('category_name')
        category, created = Category.objects.get_or_create(name=category_name)
        serializer.save(category=category)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class Website_ToolsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This class is used to retrieve,
    update and delete a single
    website tool by its id.
    """
    queryset = Website_Tools.objects.all()
    serializer_class = Website_ToolsSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'

    def get_object(self):
        # Override the get_object method to handle the case where the category needs to be fetched or created
        instance = super().get_object()
        category_name = self.request.data.get('category_name', instance.category.name)
        instance.category, created = Category.objects.get_or_create(name=category_name)
        if not created:
            instance.save() # Save instance if category already exists but was not originally in the request data
        return instance

# New view for filtering tools by category
class ToolsByCategoryList(generics.ListAPIView):
    serializer_class = Website_ToolsSerializer

    def get_queryset(self):
        """ This method is used to filter the website tools by category. """
        category_name = self.kwargs['category_name']
        return Website_Tools.objects.filter(category__name=category_name)

def home(request):
    """ This function is used to render the home page. """
    tools = Website_Tools.objects.all()
    return render(request, 'index.html', {'tools': tools})
