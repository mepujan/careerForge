# Generated by Django 5.0.1 on 2024-01-30 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_job_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='icons',
        ),
        migrations.AddField(
            model_name='category',
            name='i_class',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
