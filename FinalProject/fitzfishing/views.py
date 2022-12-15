from django.shortcuts import render
from django.core.paginator import Paginator
from .models import RecentReports
from .models import TopMonth
from .models import TopSeason
from .models import FishCaught2018
from .models import FishCaughtMonth2018
from .models import SpeciesCaught2018
from .models import FishCaughtSeason2018
from .models import Ratings2018
from .models import ReportData2018
from .models import OverallLakeData
from .models import OverallMonthData
from .models import OverallSpeciesData
from .models import OverallSeasonData
from .models import OverallPaginator

# Create your views here.
def index(request):
    month_list = TopMonth.objects.all()
    season_list = TopSeason.objects.all()
    reports_list = RecentReports.objects.all()
    most_recent = RecentReports.objects.filter(location_name="Lost Creek")
    return render(request, 'fitzfishing/index.html',{'month_list': month_list, 'season_list': season_list, 'reports_list': reports_list, 'most_recent': most_recent})

def current_reports(request):
    reports_list = RecentReports.objects.all()
    month_list = TopMonth.objects.all()
    return render(request, 'fitzfishing/current_reports.html', {'reports_list': reports_list, 'month_list': month_list})

def yearly_reports(request):
    return render(request, 'fitzfishing/yearly_reports.html')

def overall_stats(request):
    overall_lake_list = OverallLakeData.objects.all()
    overall_month_list = OverallMonthData.objects.all()
    overall_species_list = OverallSpeciesData.objects.all()
    overall_season_list = OverallSeasonData.objects.all()
    overall_name_list = OverallPaginator.objects.all()

    lake_name = request.GET.get('lake_name')
    if lake_name != '' and lake_name is not None:
        overall_name_list = overall_name_list.filter(location_name__icontains=lake_name)

    paginator = Paginator(overall_name_list, 5)
    page = request.GET.get('page')
    overall_name_list = paginator.get_page(page)
    return render(request, 'fitzfishing/overall_stats.html', {'overall_lake_list': overall_lake_list, 'overall_month_list': overall_month_list, 'overall_species_list': overall_species_list, 'overall_season_list': overall_season_list, 'overall_name_list': overall_name_list})

def about(request):
    return render(request, 'fitzfishing/about.html')

def year1(request):
    total_list = FishCaught2018.objects.all()
    month_list = FishCaughtMonth2018.objects.all()
    species_list = SpeciesCaught2018.objects.all()
    seasons_list = FishCaughtSeason2018.objects.all()
    rating_list = Ratings2018.objects.all()
    return render(request, 'yearly_reports/2018/2018.html', {'total_list': total_list, 'month_list': month_list, 'species_list': species_list, 'seasons_list': seasons_list, 'rating_list': rating_list})

def adams2018(request):
    report_adams = ReportData2018.objects.filter(location_name="Adams")
    return render(request, 'yearly_reports/2018/adams.html', {'report_adams': report_adams})

def east_canyon2018(request):
    report_east_canyon = ReportData2018.objects.filter(location_name="East Canyon")
    return render(request, 'yearly_reports/2018/east_canyon.html', {'report_east_canyon': report_east_canyon})

def hobbs2018(request):
    report_hobbs = ReportData2018.objects.filter(location_name="Hobbs")
    return render(request, 'yearly_reports/2018/hobbs.html', {'report_hobbs': report_hobbs})

def holmes2018(request):
    report_holmes = ReportData2018.objects.filter(location_name="Holmes")
    return render(request, 'yearly_reports/2018/holmes.html', {'report_holmes': report_holmes})

def jensen2018(request):
    report_jensen = ReportData2018.objects.filter(location_name="Jensen")
    return render(request, 'yearly_reports/2018/jensen.html', {'report_jensen': report_jensen})

def kaysville2018(request):
    report_kaysville = ReportData2018.objects.filter(location_name="Kaysville")
    return render(request, 'yearly_reports/2018/kaysville.html', {'report_kaysville': report_kaysville})

def kens2018(request):
    report_kens = ReportData2018.objects.filter(location_name="Kens")
    return render(request, 'yearly_reports/2018/kens.html', {'report_kens': report_kens})

def lost_creek2018(request):
    report_lost_creek = ReportData2018.objects.filter(location_name="Lost Creek")
    return render(request, 'yearly_reports/2018/lost_creek.html', {'report_lost_creek': report_lost_creek})

def pineview2018(request):
    report_pineview = ReportData2018.objects.filter(location_name="Pineview")
    return render(request, 'yearly_reports/2018/pineview.html', {'report_pineview': report_pineview})

def rockport2018(request):
    report_rockport = ReportData2018.objects.filter(location_name="Rockport")
    return render(request, 'yearly_reports/2018/rockport.html', {'report_rockport': report_rockport})

def strawberry2018(request):
    report_strawberry = ReportData2018.objects.filter(location_name="Strawberry")
    return render(request, 'yearly_reports/2018/strawberry.html', {'report_strawberry': report_strawberry})

def willard2018(request):
    report_willard = ReportData2018.objects.filter(location_name="Willard")
    return render(request, 'yearly_reports/2018/willard.html', {'report_willard': report_willard})