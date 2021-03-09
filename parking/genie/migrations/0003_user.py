# Generated by Django 3.0.3 on 2021-03-09 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genie', '0002_parkingspot_distance'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('renter', models.BooleanField(default=True)),
                ('owner', models.BooleanField(default=False)),
            ],
        ),
    ]