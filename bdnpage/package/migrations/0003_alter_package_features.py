# Generated by Django 4.2.15 on 2024-09-05 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0002_alter_package_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='features',
            field=models.ManyToManyField(blank=True, to='package.feature'),
        ),
    ]
