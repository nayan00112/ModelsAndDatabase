from django.db import models

# Create your models here.

class Table1_models(models.Model):
    name = models.TextField()
    email = models.EmailField( max_length=254)
    desc = models.TextField()