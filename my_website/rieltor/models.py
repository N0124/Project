from django.db import models

class Flat(models.Model):
    area = models.CharField(max_length=500)
    price = models.CharField(max_length=100)
    link = models.CharField(max_length=5000)
    description = models.CharField(max_length=10000)

    def __str__(self):
        return '%s, %s' % (self.area, self.price)
