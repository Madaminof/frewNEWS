# Generated by Django 5.0.7 on 2024-08-07 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_reklama_youtubevideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeVideo1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.FileField(blank=True, max_length=500, null=True, upload_to='youtubeVideo/')),
            ],
        ),
    ]
