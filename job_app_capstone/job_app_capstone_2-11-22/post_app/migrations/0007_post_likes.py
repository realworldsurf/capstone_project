# Generated by Django 4.0.1 on 2022-02-21 07:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post_app', '0006_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
