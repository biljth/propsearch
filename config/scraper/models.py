from django.db import models

class Property(models.Model):
    title = models.TextField()
    price = models.CharField(max_length=100)
    location = models.TextField()
    link = models.URLField()
    source = models.CharField(max_length=50)

    min_luas_tanah = models.CharField(max_length=50, blank=True, null=True)
    max_luas_tanah = models.CharField(max_length=50, blank=True, null=True)
    min_luas_bangunan = models.CharField(max_length=50, blank=True, null=True)
    max_luas_bangunan = models.CharField(max_length=50, blank=True, null=True)
    kata_kunci = models.CharField(max_length=255, blank=True, null=True)