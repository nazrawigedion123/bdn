from django.db import models
from django.urls import reverse


# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=100)
    comment = models.TextField(max_length=1000)
    added_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('contactUs:comment_list')

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['-added_date']


class Subscriber(models.Model):
    email = models.EmailField(max_length=200, unique=True)
    added_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('contact_us:subscriber_list')

    def __str__(self):
        return str(self.email)

    class Meta:
        ordering = ['-added_date']
