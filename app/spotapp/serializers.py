from rest_framework import serializers
from models import Sighting

class SpotSerializer(serializers.ModelSerialized):
    class Meta:
        model = Sighting
        fields = ('id', 'user_id', 'breed_id', 'timestamp',
                    'address', 'city', 'img', 'dog_name',
                    'headline', 'body_text')
