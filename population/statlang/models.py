from django.db import models

from django.db.models import Sum

# Create your models here.


class Population(models.Model):
    nom = models.CharField(max_length=255)
    nbre_habitant = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = "Population"
        verbose_name_plural = "Population"
    @property
    def pourcentage(self):
        percentage = self.nbre_habitant*100
        return percentage
    
    @property
    def somme(self):
        percentage = self.nbre_habitant*100
        sums = Population.objects.all().aggregate(mysum = Sum('nbre_habitant'))
        total = (percentage/sums['mysum'])
        return round(total, 2)
    
    # @property
    # def centage(self):
    #     tage = percentage/sums
    #     return tage
    
    def __str__(self):
        return self.nom