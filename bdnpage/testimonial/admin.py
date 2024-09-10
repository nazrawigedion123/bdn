from django.contrib import admin
from .models import Testimonials

# Register your models here.
@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('person','position','image','testimonial','added_date')
