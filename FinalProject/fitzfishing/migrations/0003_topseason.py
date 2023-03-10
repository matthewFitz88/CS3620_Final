# Generated by Django 4.1.2 on 2022-11-28 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitzfishing', '0002_topmonth'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopSeason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=200)),
                ('fish_caught', models.FloatField()),
                ('species_caught', models.CharField(max_length=200)),
                ('trips', models.FloatField()),
                ('average', models.FloatField()),
                ('top_image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
