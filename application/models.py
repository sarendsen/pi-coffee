from django.db import models


class Setting(models.Model):
    key = models.CharField(null=False, blank=False, max_length=100)
    value = models.IntegerField(null=True, blank=True)
