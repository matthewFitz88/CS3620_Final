from django.db import models

# Create your models here.
class RecentReports(models.Model):
    location_name = models.CharField(max_length=200)
    sky = models.CharField(max_length=200)
    temp = models.CharField(max_length=200)
    water_temp = models.CharField(max_length=200)
    lures = models.CharField(max_length=500)
    fish_caught = models.CharField(max_length=200)
    species_caught = models.CharField(max_length=200)
    hours_fished = models.FloatField()
    report_image = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.location_name

class TopMonth(models.Model):
    location_name = models.CharField(max_length=200)
    fish_caught = models.CharField(max_length=200)
    species_caught = models.CharField(max_length=200)
    trips = models.CharField(max_length=200)
    average = models.CharField(max_length=200)
    top_image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.location_name

class TopSeason(models.Model):
    location_name = models.CharField(max_length=200)
    fish_caught = models.CharField(max_length=200)
    species_caught = models.CharField(max_length=200)
    trips = models.CharField(max_length=200)
    average = models.CharField(max_length=200)
    top_image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.location_name

class FishCaught2018(models.Model):
    location_name = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
    percent = models.CharField(max_length=200)

    def __str__(self):
        return self.location_name

class FishCaughtMonth2018(models.Model):
    month_name = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
    percent = models.CharField(max_length=200)

    def __str__(self):
        return self.month_name

class SpeciesCaught2018(models.Model):
    species_name = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
    percent = models.CharField(max_length=200)

    def __str__(self):
        return self.species_name

class FishCaughtSeason2018(models.Model):
    season_name = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
    percent = models.CharField(max_length=200)

    def __str__(self):
        return self.season_name

class Ratings2018(models.Model):
    rating = models.CharField(max_length=200)
    range = models.CharField(max_length=200)

    def __str__(self):
        return self.rating

class ReportData2018(models.Model):
    location_name = models.CharField(max_length=200)
    date1 = models.CharField(max_length=200, blank=True)
    date2 = models.CharField(max_length=200, blank=True)
    date3 = models.CharField(max_length=200, blank=True)
    date4 = models.CharField(max_length=200, blank=True)
    date5 = models.CharField(max_length=200, blank=True)
    date6 = models.CharField(max_length=200, blank=True)
    date7 = models.CharField(max_length=200, blank=True)
    date8 = models.CharField(max_length=200, blank=True)
    date9 = models.CharField(max_length=200, blank=True)
    date10 = models.CharField(max_length=200, blank=True)
    date11 = models.CharField(max_length=200, blank=True)
    date12 = models.CharField(max_length=200, blank=True)
    fish_caught = models.CharField(max_length=200)
    species_caught = models.CharField(max_length=200)

    def __str__(self):
        return self.location_name

class OverallLakeData(models.Model):
    location_name = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
    percent = models.CharField(max_length=200)

    def __str__(self):
        return self.location_name

class OverallMonthData(models.Model):
    month_name = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
    percent = models.CharField(max_length=200)

    def __str__(self):
        return self.month_name

class OverallSpeciesData(models.Model):
    species_name = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
    percent = models.CharField(max_length=200)

    def __str__(self):
        return self.species_name

class OverallSeasonData(models.Model):
    season_name = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
    percent = models.CharField(max_length=200)

    def __str__(self):
        return self.season_name

class OverallPaginator(models.Model):
    location_name = models.CharField(max_length=200)

    def __str__(self):
        return self.location_name