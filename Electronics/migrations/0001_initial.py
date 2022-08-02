# Generated by Django 4.0.6 on 2022-08-02 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='electronicsProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('video', models.FileField(upload_to='static/video/%y')),
                ('description', models.CharField(max_length=500, null=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Electroniocs Projects',
            },
        ),
    ]