# Generated by Django 5.0.1 on 2024-01-24 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='job-seeker', max_length=10),
        ),
    ]
