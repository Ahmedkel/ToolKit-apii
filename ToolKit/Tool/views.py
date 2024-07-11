from .models import Website_Tools,Category
from .serializers import Website_ToolsSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.db.models import Q

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
        """ This method is used to add a new website tool. """
        category_id = self.request.data.get('category')
        if category_id is not None:
            category = Category.objects.get(id=category_id)
            serializer.save(category=category)
        else:
            return Response({"error": "Category is required."}, status=400)

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

# New view for filtering tools by category
class ToolsByCategoryList(generics.ListAPIView):
    serializer_class = Website_ToolsSerializer

    def get_queryset(self):
        """ This method is used to filter the website tools by category. """
        category_name = self.kwargs['category_name']
        return Website_Tools.objects.filter(category__name=category_name)


def home(request):
    """ This function is used to handle search queries and sorting. """
    query = request.GET.get('q', '')
    sort = request.GET.get('sort', '')
    tools = Website_Tools.objects.all()

    if query:
        tools = Website_Tools.objects.filter(
            Q(name__icontains=query) |
            Q(category__name__icontains=query) |
            Q(description__icontains=query)
        )

    if sort:
        if sort == 'drpbox-sort-asc':
            tools = tools.order_by('name')  # Ascending order by name
        elif sort == 'drpbox-sort-desc':
            tools = tools.order_by('-name')  # Descending order by name
        elif sort == 'drpbox-sort-date-asc':
            tools = tools.order_by('-created_at')  # Ascending order by date added
        elif sort == 'drpbox-sort-date-desc':
            tools = tools.order_by('created_at')  # Descending order by date added
    else:
        tools = tools.order_by('-created_at')  # Default sorting

    return render(request, 'index.html', {'tools': tools, 'query': query})