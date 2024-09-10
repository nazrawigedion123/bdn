from django.db import models
from django.urls import reverse


class Personnel(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=800)
    image = models.ImageField(upload_to='images/', null=True,)
    location = models.TextField(max_length=1000)

    def get_absolute_url(self):
        return reverse("personnel:personnel_list")

    class Meta:
        ordering = ['-name']

# Create your models here.
