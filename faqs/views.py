from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FAQ
from django.core.cache import cache

class FAQList(APIView):
    def get(self, request):
        lang = request.GET.get('lang', 'en')
        cache_key = f"faqs_{lang}"
        data = cache.get(cache_key)

        if not data:
            faqs = FAQ.objects.all()
            data = [faq.get_translation(lang) for faq in faqs]
            cache.set(cache_key, data, timeout=60*15)

        return Response(data)




# Create your views here.
