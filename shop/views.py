from django.shortcuts import render
from shop.models import Collections

# Create your views here.

def index(request):
    context = {
        'collections': Collections.objects.filter(enabled=True).order_by('last_modif')
    }
    return render(request, 'index.html', context)