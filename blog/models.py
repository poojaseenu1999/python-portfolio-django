from django.db import models

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    date = models.DateField()
