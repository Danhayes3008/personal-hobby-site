# Generated by Django 4.0.6 on 2022-08-02 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlenderModeling', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blendermodels',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='static/video/%y'),
        ),
        migrations.AlterField(
            model_name='blendermodels',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
    ]
