from django.db import models

class Quote(models.Model):
    text = models.CharField(max_length=500)
    pub_date = models.DateField('date to publish')

class Freebie(models.Model):
    link = models.CharField(max_length=500)
    pub_date = models.DateField('date to publish')
    def __unicode__(self):
        return self.link

class Survey(models.Model):
    link  = models.CharField(max_length=200,unique=True)
    active = models.BooleanField()
    value = models.DecimalField(max_digits=5, decimal_places=2)
    def __unicode__(self):
        return self.link
    
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    surveys = models.ManyToManyField(Survey,blank=True)
    
class Configuration(models.Model):
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)