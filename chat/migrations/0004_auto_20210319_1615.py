# Generated by Django 2.0 on 2021-03-19 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_myimage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyImage',
        ),
        migrations.AddField(
            model_name='message',
            name='model_pic',
            field=models.ImageField(null='True', upload_to='foto'),
        ),
    ]
