from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Location(models.Model):
    country = models.CharField(verbose_name='country', max_length=50)
    city = models.CharField(verbose_name='city', max_length=50)
    street = models.CharField(max_length=50)
    building_number = models.SmallIntegerField()
    phone_number = PhoneNumberField()

    def __str__(self):
        return f'{self.country} - {self.city}'

class Restaurant(models.Model):
    name = models.CharField(verbose_name='restaurant name', max_length=100, unique=True)
    brief = models.TextField(verbose_name='brief about the restaurant', blank=True)
    location = models.ForeignKey(Location, verbose_name=("restaurant location"), on_delete=models.CASCADE)
    delivery = models.BooleanField(null=False, blank=False, default=False)
    Takeout = models.BooleanField(null=False, blank=False, default=True)
    img = models.ImageField(upload_to='images', null=True, blank=True, default=None)

    def calc_score(self):
        num_score = self.rate_set.count()
        sum_score = self.rate_set.all().aggregate(models.Sum('score')).get('score__sum')
        if sum_score is None:
            return [1,]
        else:
            socore = list(range(0, round(sum_score / num_score)))
            return socore or 0
    
    def rest_of_score(self):
        score = self.calc_score()
        if len(score) < 5:
            return list(range(5 - len(score)))
        else:
            return False

    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        #? here was an error because i forget to add app name to reverse func
        return reverse("restaurant_rating:restaurant_detail", kwargs={"name": self.name})
    
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url
    

class RatingChooses(models.IntegerChoices):
    VERY_POOR = 1, _('very poor')
    POOR = 2, _('poor')
    FAIR = 3, _('fair')
    GOOD = 4, _('good')
    EXCELLENT = 5, _('excellent')

class Rate(models.Model):
    name = models.CharField(max_length=50, blank=False)
    restaurant = models.ForeignKey(Restaurant, verbose_name=("Restaurant"), on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    score = models.IntegerField(choices=RatingChooses.choices, default=1)

    def __str__(self):
        return f'{self.name} - {self.restaurant} - {self.score}'
    
    def calc_score(self):
        socore = list(range(self.score))
        return socore 
    
    def rest_of_score(self):
        score = self.calc_score()
        if len(score) < 5:
            return list(range(5 - len(score)))
        else:
            return False