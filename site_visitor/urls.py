from django.urls import path
from . import views

urlpatterns = [
    # path('engineer/<int:repid>',views.add_report,name='engineerreport'),
    path('reporterhome/',views.reporterhome,name='reporterhome'),
    # path('deleteengineerreport/<int:repid>/<str:appno>',views.del_report),
    # path('updateengineerreport/<int:repid>',views.update_report),
]
