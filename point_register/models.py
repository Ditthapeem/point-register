from unicodedata import name
from django.db import models
from django.contrib.auth.models import User


class Bakery(models.Model):
    name_text = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name_text

class Point(models.Model):
    name = models.OneToOneField(Bakery, on_delete=models.CASCADE)
    point = models.IntegerField(default=100)

    def __str__(self) -> str:
        return str(f'{self.name}: {self.point} points')

class Type(models.Model):
    name = models.OneToOneField(Bakery, on_delete=models.CASCADE)
    type_text = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(f'{self.name}: Bakery {self.type_text}')

class UserPoint(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    point = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(f'{self.name}: {self.point} points')