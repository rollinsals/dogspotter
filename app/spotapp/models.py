from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(unique=True, max_length=24)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Profile,self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/{self.slug}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class DogBreed(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        ordering = ["name"]

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

def img_directory_path(instance, filename):
    return f"usr/{instance.user_id.id}/{filename}"

class Sighting(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    breed_id = models.ForeignKey(DogBreed, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    img = models.ImageField(upload_to=img_directory_path, max_length=100, null=True, blank=True)
    dog_name = models.CharField(max_length=100, null=True, blank=True)
    headline = models.CharField(max_length=140)
    body_text = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"Sighting no. {self.id}"
