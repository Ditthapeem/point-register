from django.db import models


class Bakery(models.Model):
    name_text = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name_text

class Point(models.Model):
    name = models.ForeignKey(Bakery, on_delete=models.CASCADE, unique=True)
    point = models.IntegerField(default=100)

    def __str__(self) -> str:
        return str(f'{self.name}: {self.point} points')
