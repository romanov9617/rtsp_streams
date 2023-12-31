# Generated by Django 4.2.7 on 2023-11-12 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video', '0009_delete_point_delete_users_video_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='videos', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]
