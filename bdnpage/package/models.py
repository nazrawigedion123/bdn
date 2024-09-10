from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, Group


# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    price = models.FloatField(default=0)
    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("package:feature_list")
class Package(models.Model):
    name = models.CharField(max_length=200)
    features = models.ManyToManyField(Feature,blank=True)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=1000)
    added_date = models.DateTimeField(auto_now_add=True)

    @property
    def features_display(self):
        return ', '.join(str(features) for features in self.features.all())

    def get_absolute_url(self):
        return reverse("package:package_list")

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['-added_date']

class Order(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True)
    phone=models.CharField(max_length=20)
    email=models.CharField(max_length=200)
    package = models.ForeignKey(Package , on_delete=models.CASCADE,)
    added_date = models.DateTimeField(auto_now_add=True)



    def get_absolute_url(self):
        return reverse("package:order_list")

    class Meta:
        ordering = ['-added_date']


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user receiving the notification
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  # Related order
    message = models.CharField(max_length=255)  # Notification message
    created_at = models.DateTimeField(auto_now_add=True)  # When the notification was created
    is_read = models.BooleanField(default=False)  # Has the notification been read?

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"

