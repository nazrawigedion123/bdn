# Generated by Django 4.2.15 on 2024-09-09 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0003_alter_package_features'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
