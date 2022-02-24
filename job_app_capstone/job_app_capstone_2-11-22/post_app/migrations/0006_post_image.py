# Generated by Django 4.0 on 2022-02-21 03:57

from django.db import migrations, models
import post_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0005_alter_message_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=post_app.models.get_upload_path),
        ),
    ]