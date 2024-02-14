from django.urls import path, re_path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # re_path('signup', views.signup),
    # re_path('login', views.login),
    # re_path('test_token', views.test_token),
    path('', views.website_ToolsList, name='website_tools'),
    path('website_tools/', views.website_ToolsList, name='website_tools'),
    path('website_tools/<int:id>/', views.website_ToolsDetail, name='website_tools_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
