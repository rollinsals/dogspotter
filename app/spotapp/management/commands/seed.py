"""
Faker Seed File
to generate some dummy data for testing/display purposes
"""
from django.core.management.base import BaseCommand

from random import randint, choices
import secrets
import hashlib
import string
from faker import Faker
import faker.providers
from django.contrib.auth.models import User
from spotapp.models import Sighting, DogBreed, Profile, City

# Constants
USER_COUNT = 40
CITY_COUNT = 29
SIGHTING_COUNT = 300
BREED_COUNT = 120

DOGBREEDLIST =[]

class Provider(faker.providers.BaseProvider):
    def dog_breed(self):
        return self.random_element(DOGBREEDLIST)

def random_passhash():
    """Get hashed and salted password of length N | 8 <= N <= 15"""
    raw = ''.join(
        choices(
            string.ascii_letters + string.digits + '!@#$%&', # valid pw characters
            k=randint(8, 15) # length of pw
        )
    )
    salt = secrets.token_hex(16)
    return hashlib.sha512((raw + salt).encode('utf-8')).hexdigest()

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


        for _ in range(USER_COUNT):
            new_user = User(
                username = faker.unique.user_name(),
                password = random_passhash()
            )
            new_user.save()
            Profile.objects.create(
                user = new_user,
                name = faker.unique.user_name()
            )

        for _ in range(CITY_COUNT):
            City.objects.create(
                name = faker.unique.city()
            )

        for _ in range(BREED_COUNT):
            DogBreed.objects.create(
                name = faker.unique.dog_breed()
            )
        for _ in range(SIGHTING_COUNT):
            u_id = randint(1, USER_COUNT)
            b_id = randint(1, BREED_COUNT)
            c_id = randint(1, CITY_COUNT)
            Sighting.objects.create(
                user_id = Profile.objects.get(pk=u_id),
                breed_id = DogBreed.objects.get(pk=b_id),
                timestamp = faker.date_time_this_decade(),
                address = faker.address(),
                city = City.objects.get(pk=c_id),
                img = faker.file_name(category='image'),
                dog_name = faker.first_name(),
                headline = faker.text(max_nb_chars=140),
                body_text = faker.paragraph()
            )

            #print("We did it Joe")
