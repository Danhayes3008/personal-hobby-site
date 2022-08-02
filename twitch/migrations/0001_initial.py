# Generated by Django 4.0.6 on 2022-08-02 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='twitchStreaming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='static/video/%y')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('description', models.CharField(max_length=500, null=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Twitch Streaming Videos',
            },
        ),
    ]