from django.db import models
from django.contrib.auth.models import User
from company.models import FishingCompany

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    tag_line = models.CharField(max_length=128, blank=True)
    company = models.ForeignKey(FishingCompany, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.user.username + ' profile'
