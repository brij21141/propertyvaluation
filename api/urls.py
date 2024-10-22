from django.urls import path,include 
from . import views
from .views import LoginAPI, LogoutAPI,EngineerViewSet,UserViewSet,ReceptionViewSet,ReporterViewSet,UserProfileUpdateView,UserdetailViewSet
from .views import ResetPasswordRequestView, ResetPasswordConfirmView,BankViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'engineer',EngineerViewSet)
router.register(r'user',UserViewSet)
router.register(r'reception',ReceptionViewSet)
router.register(r'reporter',ReporterViewSet)
router.register(r'userdetail',UserdetailViewSet)
router.register(r'bank',BankViewSet)

urlpatterns = [
    # to get all users api
    path('profile/update/<int:pk>/', UserProfileUpdateView.as_view(), name='profile-update'),
    path('all-users',views.allUsers,name='alluserapi'),
    path('currentuser',views.currentUser,name='currentuserapi'),
    path('export',views.export,name='exportalluserapi'),
    path('bankexport',views.bankexport,name='bankexport'),
    path('receptiongenreportexport',views.receptiongenreportexport,name='receptiongenreportexport'),
    path('engcompletedreportexport',views.engcompletedreportexport,name='engcompletedreportexport'),
    path('reportercompletedexport',views.reportercompletedexport,name='reportercompletedexport'),
    path('rolewiseuser',views.rolewiseuser,name='rolewiseuserapi'),
    path('recepreportpriority/<int:uid>',views.recepreportpriority,name='recepreportpriority'),
    path('engreportstatus/<str:status>/<int:uid>',views.engreportstatus,name='engreportstatus'),
    path('reporterreportstatus/<int:uid>',views.reporterreportstatus,name='reporterreportstatus'),
    path('reportassign/<int:uid>',views.reportassign,name='reportassign'),
    path('loginapi/',LoginAPI.as_view(),name='loginapi'),
    path('logoutapi/',LogoutAPI.as_view(),name='logoutapi'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_resetapi')),
    path('request-reset-password/', ResetPasswordRequestView.as_view(), name='request-reset-password'),
    path('reset-password/', ResetPasswordConfirmView.as_view(), name='reset-password'),
    path('', include(router.urls)),
]
