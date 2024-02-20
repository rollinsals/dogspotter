from django.shortcuts import get_object_or_404,render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.views import generic


from .models import Sighting, User, DogBreed, City
from .serializers import SpotSerializer
from rest_framework.decorators import api_view

import datetime

# Create your views here.

def home(request):
    return HttpResponse("At least it's not entirely broken")

class IndexView(generic.ListView):
    model = Sighting
    template_name = "spots/index.html"
    context_object_name = "sightings"

    def get_queryset(self):
        return Sighting.objects.all()

class SpotView(generic.DetailView):
    model = Sighting
    context_object_name = 'sighting'
    template_name = "spots/detail.html"


class SpotComposeView(generic.edit.CreateView):
    model = Sighting
    template_name = "spots/compose.html"
    fields = [
        "headline",
        "breed_id",
        "dog_name",
        "address",
        "city",
        "body_text",
        "img"
        ]
    redirect = reverse_lazy('detail', pk=model.pk)

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(SpotComposeView, self).form_valid(form)


def spot_detail(request, sighting_id):
    our_spot = get_object_or_404(Sighting, pk=sighting_id)
    return render(request, "spots/detail.html", {"sighting": our_spot})



def spot(request, sighting_id):
    our_spot = get_object_or_404(Sighting, pk=sighting_id)
    spot_serialized = SpotSerializer(our_spot)
    return JsonResponse(spot_serialized.data)


@api_view(['POST'])
def post_sighting (request):
    new_data = JSONParser().parse(request)
    sighting_serialized = SpotSerializer(data=new_data)
    if sighting_serialized.is_valid():
        sighting_serialized.save()
        return JsonResponse(sighting_serialized.data, status=status.HTTP_201_CREATED)
    return JsonResponse(sighting_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

def index (request):
    queryset = Sighting.objects.all()
    queryset_serialized = SpotSerializer(queryset, many=True)
    return JsonResponse(queryset_serialized.data, safe=False)

def recent(request):
    recent_spots = Sighting.objects.order_by("-timestamp")[:25]
    rs_serialized = SpotSerializer(recent_spots, many=True)
    return JsonResponse(rs_serialized.data, safe=False)

def by_breed(request, breed):
    breed_spots = Sighting.objects.filter(breed_id__slug = breed).order_by("timestamp")
    bs_serialized = SpotSerializer(breed_spots, many=True)
    return JsonResponse(bs_serialized.data, safe=False)

def by_city(request, city):
    city_spots = Sighting.objects.filter(city_id__slug = city).order_by("timestamp")
    cs_serialize = SpotSerializer(city_spots, many=True)
    return JsonResponse(cs_serialize.data, safe=False)

def user_spots(request, user):
    users_spots = Sighting.objects.filter(user_id__slug = user).order_by("timestamp")
    us_serialize = SpotSerializer(users_spots, many=True)
    return JsonResponse(us_serialize.data, safe=False)

"""def spot_search_name(request):
    search_criteria = JSONParser().parse(request)
    search_set = Sighting.objects.filter(dog_name__contains=search_criteria.data)"""
@api_view(['PUT', 'PATCH'])
def update_spot(request, sighting_id):
    spot = Sighting.objects.get(pk=sighting_id)
    upd_data = JSONParser().parse(request)
    spot_serial = SpotSerializer(spot, data=upd_data)
    if spot_serial.is_valid():
        spot_serial.save()
        return JsonResponse(spot_serial.data)

    return JsonResponse(spot_serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_spot(request, sighting_id):
    spot = Sighting.objects.get(pk=sighting_id)
    spot.delete()
    return JsonResponse({'message': 'Spot has been deleted'}, status=status.HTTP_204_NO_CONTENT)

#### Authentication ####

class SpotterRegisterView(generic.FormView):
    template = 'user/registration.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    successful_url = reverse_lazy('home')

    def form_vaild(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SpotterRegisterView, self).form_valid(form)


class SpotterLoginView(LoginView):
    template_name = 'user/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')
