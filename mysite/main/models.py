from django.db import models

# Create your models here.

class AboutUs(models.Model):
    name = models.CharField('About name', max_length=50)
    text = models.TextField('About text')

class HomeCars(models.Model):
    name = models.CharField('Car name', max_length=50)
    img = models.ImageField('Car image', upload_to='media')
    price = models.IntegerField('Car price')

    def __str__(self):
        return self.name