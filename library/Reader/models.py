from django.db import models

class Readers(models.Model):
    fullName = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=128) 

    def __str__(self):
        return f'{self.fullName}-{self.password}'
