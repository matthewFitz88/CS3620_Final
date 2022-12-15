from django.contrib import admin
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

# Register your models here.
admin.site.register(RecentReports)
admin.site.register(TopMonth)
admin.site.register(TopSeason)
admin.site.register(FishCaught2018)
admin.site.register(FishCaughtMonth2018)
admin.site.register(SpeciesCaught2018)
admin.site.register(FishCaughtSeason2018)
admin.site.register(Ratings2018)
admin.site.register(ReportData2018)
admin.site.register(OverallLakeData)
admin.site.register(OverallMonthData)
admin.site.register(OverallSpeciesData)
admin.site.register(OverallSeasonData)
admin.site.register(OverallPaginator)