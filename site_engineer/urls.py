from django.urls import path
from . import views

urlpatterns = [
    path('engineer/<int:repid>',views.add_report,name='engineerreport'),
    path('engineerhome/',views.engineerhome,name='engineerhome'),
    path('deleteengineerreport/<int:repid>/<str:appno>',views.del_report),
    path('updateengineerreport/<int:repid>',views.update_report),
    path('delete_file/<int:doc_id>/', views.delete_file, name='delete_file'),
]