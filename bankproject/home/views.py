# Create your views here.
from django.shortcuts import render

from bankapp.models import District, Branch



from django.shortcuts import render


def home_page(request):
    return render(request, 'index.html')
