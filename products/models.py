from django.db import models
from django.utils import timezone


class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField(
        default=0,
        null=False)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title