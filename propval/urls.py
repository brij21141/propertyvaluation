from django.contrib.auth import views as auth_views
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter  
from .views import UserActivityViewSet  

router = DefaultRouter()  
router.register(r'user-activity', UserActivityViewSet)  


urlpatterns = [
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('profile/<int:uid>',views.profile,name='profile'),
    path('generatebill/',views.generatebill,name='generatebill'),
    path('generatebill/bill/<int:uid>',views.bill,name='bill'),
    path('generatebill/bills/<int:uid>',views.bills,name='bills'),
    path('generatebill/billinpdf',views.billinpdf.as_view(),name='billinpdf'),
    path('userlog',views.Userlog,name='userlog'),
    
    path('', include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOTPROFILE)  +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  

