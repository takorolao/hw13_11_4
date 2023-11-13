from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Burger(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient)
    price = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
    file = models.FileField(upload_to='burger_files/', null=True, blank=True)
    image = models.ImageField(upload_to='burgers/', null=True, blank=True)

    def __str__(self):
        return self.name
