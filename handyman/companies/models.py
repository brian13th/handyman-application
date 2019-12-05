from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class CompanyPost(models.Model):
    job = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tel = models.CharField(max_length=10)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.job
