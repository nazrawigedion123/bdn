from django.contrib import admin
from .models import Feature,Package, Notification


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name','description')

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name','features_display','image','description','added_date')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user','order','message','created_at','is_read')

# Register your models here.
