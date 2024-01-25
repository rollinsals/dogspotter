"""
Faker Seed File
to generate some dummy data for testing/display purposes
"""
from django.core.management.base import BaseCommand

from random import randint
from faker import Faker
import faker.providers
from spotapp.models import Sighting, DogBreed, User, City

# Constants
USER_COUNT = 40
CITY_COUNT = 29
SIGHTING_COUNT = 300
BREED_COUNT = 120

DOGBREEDLIST =[]

class Provider(faker.providers.BaseProvider):
    def dog_breed(self):
        return self.random_element(DOGBREEDLIST)

class Command(BaseCommand):
    help = "Command info"

    def handle(self, *args, **kwargs):
        # breeds list from https://en.wikipedia.org/wiki/List_of_dog_breeds
        breed_file = open("breeds.txt", "r")
        for line in breed_file:
            DOGBREEDLIST.append(line)
        breed_file.close()

        # begin action
        faker = Faker()
        faker.add_provider(Provider)


        for _ in range(1,USER_COUNT):
             User.objects.create(
                name = faker.unique.user_name()
            )

        for _ in range(1, CITY_COUNT):
            City.objects.create(
                name = faker.unique.city()
            )

        for _ in range(1, BREED_COUNT):
            DogBreed.objects.create(
                name = faker.unique.dog_breed()
            )
        for _ in range(SIGHTING_COUNT):
            Sighting.objects.create(
                user_id = randint(1, USER_COUNT),
                breed_id = randint(1, BREED_COUNT),
                timestamp = faker.date_time_this_decade(),
                address = faker.address(),
                city = randint(1, CITY_COUNT),
                img = faker.file_name(category='image'),
                dog_name = faker.first_name(),
                headline = faker.text(max_nb_chars=140),
                body_text = faker.paragraph()
            )

            print("We did it Joe")
