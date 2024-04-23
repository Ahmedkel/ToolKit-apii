from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Website_Tools, Category
from .serializers import Website_ToolsSerializer

class WebsiteToolsModelTest(TestCase):
    def setUp(self):
        """ this method is called before each test"""
        self.category = Category.objects.create(name='Test Category')
        self.website_tool = Website_Tools.objects.create(
            name='Test Tool',
            description='This is a test tool.',
            pricing=Website_Tools.PricingChoices.FREE,
            category=self.category,
            url='https://www.example.com'
        )

    def test_website_tool_content(self):
        """ this method tests the website tool content """
        website_tool = Website_Tools.objects.get(id=1)
        expected_object_name = f'{website_tool.name} - {website_tool.created_at.strftime("%d-%m-%Y %H:%M:%S")}'
        self.assertEqual(expected_object_name, str(website_tool))

class WebsiteToolsSerializerTest(TestCase):
    def setUp(self):
        """ this method is called before each test """
        self.category = Category.objects.create(name='Test Category')
        self.website_tool = Website_Tools.objects.create(
            name='Test Tool',
            description='This is a test tool.',
            pricing=Website_Tools.PricingChoices.FREE,
            category=self.category,
            url='https://www.example.com'
        )
        self.serializer = Website_ToolsSerializer(instance=self.website_tool)

    def test_website_tool_serializer_fields(self):
        """ this method tests the website tool serializer fields """
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'category', 'image', 'description', 'created_at', 'updated_at', 'pricing', 'url']))

    def test_website_tool_serializer_data(self):
        """ this method tests the website tool serializer data """
        data = self.serializer.data
        self.assertEqual(data['name'], 'Test Tool')
        self.assertEqual(data['description'], 'This is a test tool.')
        self.assertEqual(data['pricing'], 'FREE')
        self.assertEqual(data['url'], 'https://www.example.com')

class WebsiteToolsAPIViewTest(TestCase):
    def setUp(self):
        """ this method is called before each test """
        self.client = APIClient()
        self.category = Category.objects.create(name='Test Category')
        self.website_tool = Website_Tools.objects.create(
            name='Test Tool',
            description='This is a test tool.',
            pricing=Website_Tools.PricingChoices.FREE,
            category=self.category,
            url='https://www.example.com'
        )
        self.website_tool_url = reverse('website_tool-detail', kwargs={'pk': self.website_tool.id})

    def test_get_website_tool(self):
        """ this method tests the get website tool """
        response = self.client.get(self.website_tool_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Tool')

    def test_create_website_tool(self):
        """ this method tests the create website tool """
        website_tool_data = {
            'name': 'New Tool',
            'description': 'This is a new tool.',
            'pricing': 'PAID',
            'category': self.category.id,
            'url': 'https://www.newtool.com'
        }
        response = self.client.post(reverse('website_tool-list'), website_tool_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Website_Tools.objects.count(), 2)
        self.assertEqual(Website_Tools.objects.get(name='New Tool').description, 'This is a new tool.')
