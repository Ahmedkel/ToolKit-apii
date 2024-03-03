from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('website_tools/', views.website_ToolsList.as_view(), name='website_tools'),
    path('website_tools/<int:id>/', views.website_ToolsDetail.as_view(), name='website_tools_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)