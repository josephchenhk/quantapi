# from django.db import models
from djongo import models

# Create your models here.

class Hk(models.Model):
    code = models.CharField('Stock Code', max_length=20, primary_key=True)
    data = models.JSONField('Data', null=True)

    def __str__(self):
        return self.code





