# Generated by Django 4.0.6 on 2022-08-02 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Electronics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='electronicsprojects',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='electronicsprojects',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='static/video/%y'),
        ),
    ]
