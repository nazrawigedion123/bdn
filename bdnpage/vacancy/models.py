from django.db import models
from django.urls import reverse
from django.utils import timezone


class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    job_type = models.CharField(max_length=50, choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'),
                                                        ('Contract', 'Contract')])
    added_date = models.DateTimeField(default=timezone.now)
    application_deadline = models.DateField()

    def __str__(self):
        return self.title

    class Meta:

        ordering = ['-added_date']

    def get_absolute_url(self):
        return reverse("vacancy:vacancy_detail", kwargs={'pk': self.pk})