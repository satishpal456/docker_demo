from django.db import models

# Create your models here.


class Blog(models.Model):
    test = models.CharField(null=True, max_length=100, blank=True)
    test1 = models.CharField(null=True, max_length=100, blank=True)
    test2 = models.CharField(null=True, max_length=100, blank=True)