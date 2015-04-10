from django.db import models

# Create your models here.

class Beer(models.Model):
    name = models.CharField(max_length=200)
    brewery = models.CharField(max_length=500)
    brewery_website = models.URLField()
    description = models.CharField(max_length=2000)
    style = models.CharField(max_length=200)
    abv = models.FloatField()
    image = models.URLField(max_length=500)

    # Rating Beer
    review = models.CharField(max_length=2000)
    rank = models.IntegerField(null=True, blank=True)

    hoppiness = models.FloatField(null=False)
    drinkability = models.FloatField(null=False)
    alldaybeer =  models.FloatField(null=False)
    fruitiness = models.FloatField(null=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)

    # Rating
    review = models.CharField(max_length=2000)
    rank = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.name
