from django.db import models

# Create your models here.


class SuperUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    create_date = models.DateTimeField('date published')
