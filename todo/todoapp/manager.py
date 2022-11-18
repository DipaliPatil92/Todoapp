from django.db import models

class CustomManager(models.Manager):

    def det_queryset(self):

        return super().get_queryset().order_by('-cprice')


    def sortfeeshightolowdev(self):
        
        return super().order_by('-cprice').filter(ccat='Developement')


    def sortfeeshightolowds(self):
        
        return super().order_by('-cprice').filter(ccat='Data Science')

    def sortfeeslowtohighdev(self):
        
        return super().order_by('cprice').filter(ccat='Developement')


    def sortfeeslowtohighds(self):
        
        return super().order_by('cprice').filter(ccat='Data Science')