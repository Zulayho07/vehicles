from django.db import models
from django.contrib.auth.models import User


class Brand(models.Model):
    title = models.CharField(max_length=255)
    country = models.CharField(max_length=350)

    def __str__(self):
        return self.title


class Car(models.Model):
    name = models.CharField(max_length=255)
    year = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    color = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand.title} {self.name} ({self.year})"


class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username}: {self.text}"
