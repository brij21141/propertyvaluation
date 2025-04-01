from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('reporter/<int:repid>',views.add_report,name='reporterreport'),
    path('reporterhome/',views.reporterhome,name='reporterhome'),
    # path('deleteengineerreport/<int:repid>/<str:appno>',views.del_report),
    path('updatereporterreport/<int:repid>',views.update_report),
    path('geomap/',Geomapview.as_view(),name='geomap'),
    path('rep_engreport/<int:repid>',views.rep_engreport,name='rep_engreport'),
    path('download_rep_eng_images/<int:repid>',views.download_rep_eng_images,name='download_rep_eng_images'),
]
