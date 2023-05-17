from django.db import models
from django import forms


# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=200)
    resume = models.TextField()
    miniature = models.ImageField()
    contenu = models.TextField()
    auteur = models.CharField(max_length=100)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)

class Contact(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    email = models.CharField(max_length=150, null=True, blank=True)
    message = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)


