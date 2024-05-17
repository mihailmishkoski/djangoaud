from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    POSITION_GENRES = [
        ("RC", "Rock"),
        ("RA", "Rap"),
        ("CL", "Classic"),
        ("PO", "Pop"),
        ("JZ", "Jazz")
    ]

    def __str__(self):
        return f"{self.name}  {self.artist}"
