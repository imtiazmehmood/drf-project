# Generated by Django 4.1.4 on 2022-12-31 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0002_movie_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
