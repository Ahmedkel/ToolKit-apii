from django.db import models


class PricingChoices(models.TextChoices):
    FREE = 'FREE', 'Free'
    PAID = 'PAID', 'Paid'
    FREEMIUM = 'FREEMIUM', 'Freemium'
    
class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    def __str__(self) -> str:
        return self.name

class website_Tools(models.Model):
    """ This class is used to create the website_Tools model. """
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pricing = models.CharField(max_length=8, choices=PricingChoices.choices, default=PricingChoices.FREE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='images/')
    url = models.URLField()
    
    def __str__(self):
        return self.name + ' - ' + self.created_at.strftime('%d-%m-%Y %H:%M:%S')
