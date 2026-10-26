from django.db import models
class Schedule(models.Model):
    browser_key=models.CharField(max_length=64,unique=True)
    state=models.JSONField(default=dict)
    revision=models.PositiveIntegerField(default=0)
