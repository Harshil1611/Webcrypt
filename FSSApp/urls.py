from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.home, name='home'),
    path('manage_users', views.manage_users, name='manage_users'),
    path('about_us', views.about_us, name='about_us'),
    path('find_contacts', views.find_contacts, name='find_contacts'),
    path('company_list', views.company_list, name='company_list'),
    path('join_company/<str:name>/', views.join_company, name='join_company'),
    path('approve_request/<str:username>/', views.approve_request, name='approve_request'),
    path('temp_remove_user/<str:username>/', views.temp_remove_user, name='temp_remove_user'),
    path('deny_request/<str:username>/', views.deny_request, name='deny_request'),
]

handler404 = 'FSSApp.views.error_404'
# handler500 = 'FSSApp.views.error_500'
# handler403 = 'FSSApp.views.error_403'
# handler400 = 'FSSApp.views.error_400'
