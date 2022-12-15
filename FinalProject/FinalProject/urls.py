"""FinalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fitzfishing import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('current_reports/', views.current_reports, name="current_reports"),
    path('yearly_reports/', views.yearly_reports, name="yearly_reports"),
    path('overall_stats/', views.overall_stats, name="overall_stats"),
    path('about/', views.about, name="about"),
    path('2018/', views.year1, name="2018"),
    path('adams2018/', views.adams2018, name="adams2018"),
    path('east_canyon2018/', views.east_canyon2018, name="east_canyon2018"),
    path('hobbs2018/', views.hobbs2018, name="hobbs2018"),
    path('holmes2018/', views.holmes2018, name="holmes2018"),
    path('jensen2018/', views.jensen2018, name="jensen2018"),
    path('kaysville2018/', views.kaysville2018, name="kaysville2018"),
    path('kens2018/', views.kens2018, name="kens2018"),
    path('lost_creek2018/', views.lost_creek2018, name="lost_creek2018"),
    path('pineview2018/', views.pineview2018, name="pineview2018"),
    path('rockport2018/', views.rockport2018, name="rockport2018"),
    path('strawberry2018/', views.strawberry2018, name="strawberry2018"),
    path('willard2018/', views.willard2018, name="willard2018"),
]

urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
