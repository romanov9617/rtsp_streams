# Generated by Django 4.2.7 on 2023-11-05 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_users_salt_alter_users_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]
