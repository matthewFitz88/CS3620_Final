# Generated by Django 4.1.2 on 2022-12-09 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitzfishing', '0016_alter_reportdata2018_date1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OverallLakeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=200)),
                ('total', models.CharField(max_length=200)),
                ('percent', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OverallMonthData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_name', models.CharField(max_length=200)),
                ('total', models.CharField(max_length=200)),
                ('percent', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OverallSeasonData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_name', models.CharField(max_length=200)),
                ('total', models.CharField(max_length=200)),
                ('percent', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OverallSpeciesData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species_name', models.CharField(max_length=200)),
                ('total', models.CharField(max_length=200)),
                ('percent', models.CharField(max_length=200)),
            ],
        ),
    ]