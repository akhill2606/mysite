from django.db import models

# Create your models here.
class Hello(models.Model):
    hello_views = models.IntegerField(default=0)
