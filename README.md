# Dog Spotter
A simple check-app. Creates sightings of dogs.

## Entities
- User (just a username - no actual implimentation)
- City
- DogBreed
- Sighting (AKA Spot, main structure of the app)
    - user_id
    - city_id
    - breed_id
    - timestamp (autogenerated at creation)
    - headline
    - body text (optional)
    - dog's name (optional)
    - image (optional, just a file name string, no implimentation)
    - address

## Running
Run migration
Run manage.py seed - this will create a new dataset

API is functional for:
- '/spots' (index of posts)
- '/spots/recent' (filter to top 25 newest)
- '/spots/city/<cityname>' (posts from a city. URL friendly name as variable. You'll need to look up a city name that's generated.)
- '/spots/breed/<breedname>' (posts of a certain dog breed. Same conditions as city)
- '/spots/<username>' (posts by a user. As above, so below)

Not quite working:
- Create/Update/Delete sighting (CSRF token needed?)
- ANY front end. Just outputs JSON at the moment
