from rest_framework import serializers

from film.models import Film


class FilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'title', 'description', 'release_date')
