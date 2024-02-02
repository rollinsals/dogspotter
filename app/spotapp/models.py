from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class User(models.Model):
    name = models.CharField(unique=True, max_length=24)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(User, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/{self.slug}"


class DogBreed(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(DogBreed, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/breed/{self.slug}"


class City(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "cities"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f"/city/{self.slug}"

class Sighting(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    breed_id = models.ForeignKey(DogBreed, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    img = models.TextField(null=True, blank=True) # fake 'file' for now. just a dummy file name
    dog_name = models.CharField(max_length=100, null=True, blank=True)
    headline = models.CharField(max_length=140)
    body_text = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"Sighting no. {self.id}"
