from django.contrib import admin
from .models import Website_Tools, Category

class Display_listOfTools(admin.ModelAdmin):
    """ Display the list of tools in the admin panel. """
    list_display = ['name', 'pricing', 'description', 'category', 'url', 'created_at', 'updated_at']
    search_fields = ['name', 'pricing', 'category']
    list_filter = ('category',)
    

admin.site.register(Website_Tools, Display_listOfTools)
admin.site.register(Category)