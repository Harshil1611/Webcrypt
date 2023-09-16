from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('decryption/',views.decryption,name='decryption'),
    # path('process_form/', views.process_form, name='process_form'),
    path('download/', views.download, name='download'),
]
