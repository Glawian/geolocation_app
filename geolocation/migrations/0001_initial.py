# Generated by Django 3.2.6 on 2021-08-28 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Geolocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15)),
                ('continent_name', models.CharField(max_length=15)),
                ('country_name', models.CharField(max_length=50)),
                ('region_name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=15)),
                ('latitude', models.CharField(max_length=20)),
                ('longitude', models.CharField(max_length=20)),
            ],
        ),
    ]
