from django.db import models
from django.contrib.auth.models import User

class FishingCompany(models.Model):
    name = models.CharField(max_length=60)
    Owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description = models.TextField()
    # picture = models.ImageField()
