# Generated by Django 4.2.7 on 2023-11-12 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0008_alter_video_address_alter_video_camera_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Point',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.AddField(
            model_name='video',
            name='is_public',
            field=models.BooleanField(default=False, verbose_name='Публичный'),
        ),
    ]
