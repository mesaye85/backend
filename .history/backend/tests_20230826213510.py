from django.test import TestCase
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt    

# Create your tests here.

class Test(TestCase):
    def test(self):
        self.assertEqual(1, 1)
        

class TestViews(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, world. You're at the polls index.")
        
        