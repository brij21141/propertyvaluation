from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('reporter/<int:repid>',views.add_report,name='reporterreport'),
    path('reporterhome/',views.reporterhome,name='reporterhome'),
    # path('deleteengineerreport/<int:repid>/<str:appno>',views.del_report),
    path('updatereporterreport/<int:repid>',views.update_report),
    path('geomap/',Geomapview.as_view(),name='geomap'),
]
