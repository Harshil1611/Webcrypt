from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('decryption/',views.decryption,name='decryption'),
    # path('login/', views.login, name='login'),
    path('download/', views.download, name='download'),
    # path('decryption/login/',views.login,name='login'),
]
