# Generated by Django 4.1.2 on 2022-12-11 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitzfishing', '0018_overallstats'),
    ]

    operations = [
        migrations.AddField(
            model_name='overallstats',
            name='location_name',
            field=models.CharField(default='Adams', max_length=200),
        ),
    ]
