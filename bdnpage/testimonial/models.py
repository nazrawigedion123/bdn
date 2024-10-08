from django.db import models
from django.urls import reverse


# Create your models here.
class Testimonials(models.Model):
    person = models.CharField(max_length=200)
    position = models.CharField(max_length=800)
    image = models.ImageField(upload_to='images/', null=True,)
    testimonial = models.TextField(max_length=1000)
    added_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("testimonial:testimonials_list")

    def __str__(self):
        return str(self.person)

    class Meta:
        ordering = ['-added_date']
