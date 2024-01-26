"""
Faker Seed File
to generate some dummy data for testing/display purposes
"""

from random import randint
from faker import Faker
from app.spotapp.models import Sighting, DogBreed, User, City

# Constants
USER_COUNT = 40
CITY_COUNT = 29
SIGHTING_COUNT = 300
BREED_COUNT = 545

def main():
    """Where the magic happens"""

    # clear out tables
    User.objects.all().delete()
    City.objects.all().delete()
    DogBreed.objects.all().delete()
    Sighting.objecss.all().delete()

    # begin action
    faker = Faker()

    last_user_id = 0
    for _ in range(USER_COUNT):
        new_user = User(
            name = faker.unique.user_name()
        )
        new_user.save()
        last_user_id = new_user.id

    last_city_id = 0
    for _ in range(CITY_COUNT):
        new_city = City(
            name = faker.unique.city()
        )
        new_city.save()
        last_city_id = new_city.id

    last_breed_id = 0
    # breeds list from https://en.wikipedia.org/wiki/List_of_dog_breeds
    breeds_file = open(breeds.txt)
    for line in breeds_file:
        new_breed = DogBreed(
            name = line
        )
        new_breed.save()
        last_breed_id = new_breed.id
    breeds_file.close()

    for _ in range(SIGHTING_COUNT):
        new_sighting = Sighting(
            user_id = randint(last_user_id - USER_COUNT + 1, last_user_id),
            breed_id = randint(last_breed_id - BREED_COUNT, last_breed_id ),
            timestamp = faker.date_time_this_decade(),
            address = faker.address(),
            city = randint(last_city_id - CITY_COUNT + 1, last_city_id),
            img = faker.file_name(category='image'),
            dog_name = faker.first_name(),
            headline = faker.text(max_nb_chars=140),
            body_text = faker.paragraph()
        )
        new_sighting.save()

main()
