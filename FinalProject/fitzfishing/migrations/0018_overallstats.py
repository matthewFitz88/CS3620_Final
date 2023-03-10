# Generated by Django 4.1.2 on 2022-12-11 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitzfishing', '0017_overalllakedata_overallmonthdata_overallseasondata_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OverallStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species1', models.CharField(blank=True, max_length=200)),
                ('species2', models.CharField(blank=True, max_length=200)),
                ('species3', models.CharField(blank=True, max_length=200)),
                ('species4', models.CharField(blank=True, max_length=200)),
                ('species5', models.CharField(blank=True, max_length=200)),
                ('species6', models.CharField(blank=True, max_length=200)),
                ('species_total1', models.CharField(blank=True, max_length=200)),
                ('species_total2', models.CharField(blank=True, max_length=200)),
                ('species_total3', models.CharField(blank=True, max_length=200)),
                ('species_total4', models.CharField(blank=True, max_length=200)),
                ('species_total5', models.CharField(blank=True, max_length=200)),
                ('species_total6', models.CharField(blank=True, max_length=200)),
                ('species_percent1', models.CharField(blank=True, max_length=200)),
                ('species_percent2', models.CharField(blank=True, max_length=200)),
                ('species_percent3', models.CharField(blank=True, max_length=200)),
                ('species_percent4', models.CharField(blank=True, max_length=200)),
                ('species_percent5', models.CharField(blank=True, max_length=200)),
                ('species_percent6', models.CharField(blank=True, max_length=200)),
                ('total', models.CharField(max_length=200)),
                ('trips', models.CharField(max_length=200)),
                ('average', models.CharField(max_length=200)),
            ],
        ),
    ]
