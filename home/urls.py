from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('authentication/login/home',views.home,name='home_Page'),
    path('decryption/',views.decryption,name='decryption'),
    # path('login/', views.login, name='login'),
    path('download/', views.download, name='download'),
    path('save_to_favorites/', views.save_to_favorites, name='save_to_favorites'),
    # path('decryption/login/',views.login,name='login'),
]
