from django.db import models

class Translation(models.Model):
    language = models.CharField(max_length=20)
    key = models.CharField(max_length=255)
    value = models.TextField()

    class Meta:
        unique_together = ("language", "key")
