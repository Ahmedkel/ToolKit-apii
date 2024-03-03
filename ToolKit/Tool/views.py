from .models import website_Tools,Category
from .serializers import website_ToolsSerializer
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAdminUser



from rest_framework import generics
from .models import website_Tools, Category
from .serializers import website_ToolsSerializer
from rest_framework.permissions import IsAdminUser


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

class website_ToolsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This class is used to retrieve,
    update and delete a single
    website tool by its id.
    """
    queryset = website_Tools.objects.all()
    serializer_class = website_ToolsSerializer
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
