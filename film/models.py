from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    release_date = models.DateField()
