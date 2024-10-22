from django.urls import path
from . import views

urlpatterns = [
    path('reception',views.add_report,name='receptionreport'),
    path('receptionhome/',views.receptionhome,name='receptionhome'),
    path('deletereceptionreport/<int:repid>',views.del_report,name='deletereceptionreport'),
    path('updatereceptionreport/<int:repid>',views.update_report, name='updatereceptionreport'),
    path('add_report/', views.add_report, name='add_report'),
    path('delete_file/<int:doc_id>/', views.delete_file, name='delete_file'),
    path('engcompreportpdf/<int:doc_id>/', views.engcompreportpdf, name='engcompreportpdf'),
]
