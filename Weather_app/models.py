from django.db import models


# Create your models here.

class weather_model(models.Model):
    City = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.City

