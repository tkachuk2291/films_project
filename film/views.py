from rest_framework import viewsets
from film.models import Film
from film.serializers import FilmsSerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    model = Film
    serializer_class = FilmsSerializer
