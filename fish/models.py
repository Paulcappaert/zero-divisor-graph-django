from django.db import models
from django.contrib.auth.models import User
from company.models import FishingCompany

SPECIES = [
    'Salmon',
    'Halibut',
]


class Fish(models.Model):

    SPECIES = (
        ('SA', 'Salmon'),
        ('HA', 'Halibut'),
    )

    qr_code = models.CharField(max_length=24, unique=True)
    caught_by = models.ForeignKey(FishingCompany, on_delete=models.CASCADE)
    caught_on = models.DateTimeField(auto_now_add=True)
    species = models.CharField(max_length=2, choices=SPECIES)
    location = models.CharField(max_length=20)

    def __str__(self):
        return self.species
