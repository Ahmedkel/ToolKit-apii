from django.db import models
from django_resized import ResizedImageField


class PricingChoices(models.TextChoices):
    FREE = 'FREE', 'Free'
    PAID = 'PAID', 'Paid'
    FREEMIUM = 'FREEMIUM', 'Freemium'
    
class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    def __str__(self) -> str:
        return self.name

class Website_Tools(models.Model):
    """ This class is used to create the website_Tools model. """
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(unique=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pricing = models.CharField(max_length=8, choices=PricingChoices.choices, default=PricingChoices.FREE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = ResizedImageField(size=[500, 300], quality=80, upload_to='tool_images', force_format='WEBP' , default='tool_images/default.jpg')
    url = models.URLField(unique=True)
    
    def __str__(self):
        return self.name + ' - ' + self.created_at.strftime('%d-%m-%Y %H:%M:%S')
