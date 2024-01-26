from django.contrib import admin
from .models import Sighting, User, City, DogBreed

# Register your models here.
admin.site.register(Sighting)
admin.site.register(User)
admin.site.register(City)
admin.site.register(DogBreed)
