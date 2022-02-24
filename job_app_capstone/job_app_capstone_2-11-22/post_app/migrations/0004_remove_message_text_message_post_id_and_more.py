# Generated by Django 4.0.1 on 2022-02-17 03:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post_app', '0003_alter_post_remote_type_message_inbox'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='text',
        ),
        migrations.AddField(
            model_name='message',
            name='post_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='post_app.post'),
        ),
        migrations.AlterField(
            model_name='inbox',
            name='messages',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inbox', to='post_app.message'),
        ),
        migrations.AlterField(
            model_name='inbox',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inbox', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages_received', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages_sent', to=settings.AUTH_USER_MODEL),
        ),
    ]
