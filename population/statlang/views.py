from django.shortcuts import render
from .import models
from django.db.models import Avg, Max, Min

# Create your views here.


def home(request):
    population = models.Population.objects.all().order_by('-nbre_habitant')
    context = {
        'population': population,
    }
    return render(request, 'index.html', context)


def stats(request):
    population = models.Population.objects.all().order_by('-nbre_habitant')
    # tt = models.Population.objects.annotate(Max('nbre_habitant')).values('nom', 'nbre_habitant')
    pmax = models.Population.objects.aggregate(Max('nbre_habitant'))
    # pmin = models.Population.objects.annotate(minB=Min('nbre_habitant')).values('nom', 'nbre_habitant')
    
    print(pmax)
    # print(pmin)
    context = {
        'population': population, 
        'tt': pmax, 
        # 'pmax': pmax,
        
    }
    return render(request, 'statistic.html', context)
