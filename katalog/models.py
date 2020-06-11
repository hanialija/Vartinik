from django.db import models
from django import forms

# Create your models here.

class Card(models.Model):
    titulli = models.CharField(max_length= 30, null=False)
    desc = models.CharField(max_length= 60, null=False)
    qmimi = models.IntegerField( blank=True, null=True)
    foto = models.ImageField(upload_to='media', verbose_name='image')
    data = models.DateTimeField(auto_now=True)

class CardForm(forms.ModelForm):
    class Meta:
        model = Card        
        # fields = '__all__'
        fields = [
            'titulli',
            'desc',
            'qmimi',
            'foto'
        ]