from django.test import TestCase
from .models import FAQ

class FAQTests(TestCase):
    def setUp(self):
        FAQ.objects.create(question="What is Django?", answer="A web framework for Python.")

    def test_faq_translation(self):
        faq = FAQ.objects.first()
        self.assertEqual(faq.get_translation('hi')['question'], "Django क्या है?")

# Create your tests here.
