from django.db import models
from django.urls import reverse


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=800 , null=True, blank =True)
    image = models.ImageField(upload_to='images/', null=True,)
    description = models.TextField(max_length=1000)
    added_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("project:project_list")

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-added_date']
