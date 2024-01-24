from django.shortcuts import render
from django.http import HttpResponse
from .models import Sighting

# Create your views here.
def spot(request, sighting_id):
    return HttpResponse(f"This is a sighting {sighting_id}")

def post_sighting (request):
    pass

def index ():
    pass
