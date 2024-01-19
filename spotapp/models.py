from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(unique=True, max_length=24)

class DogBreed(models.Model):
    name = models.CharField(max_length=50)

class City(models.Model):
    name = models.CharField(max_length=100)

class Sighting(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    breed_id = models.ForeignKey(DogBreed, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    img = models.TextField()
    dog_name = models.CharField(max_length=100)
    headline = models.CharField(max_length=140)
    body_text = models.TextField()