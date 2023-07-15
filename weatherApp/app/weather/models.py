from django.contrib.auth.models import User
from django.db import models

class City(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)    
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'

class WeatherForecast(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateField()
    low_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    high_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.city} - {self.date}"