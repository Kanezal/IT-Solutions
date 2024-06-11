from django.db import models

class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    external_id = models.IntegerField(default=0)
    author = models.CharField(max_length=255)
    views_count = models.IntegerField(default=0)
    position = models.IntegerField()

    def __str__(self):
        return self.title