# Generated by Django 2.0 on 2021-03-19 20:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={},
        ),
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]