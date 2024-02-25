from django.contrib import admin
from .models import website_Tools

class Display_listOfTools(admin.ModelAdmin):
    list_display = ['name', 'pricing', 'description', 'category', 'url', 'created_at', 'updated_at']
    search_fields = ['name', 'pricing', 'category']
    

admin.site.register(website_Tools, Display_listOfTools)
