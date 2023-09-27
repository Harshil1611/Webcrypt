from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.auth_view, name='auth_view'),
    path('signup/', views.auth_view, name='signup'),  # Add this pattern for signup
    path('login/', views.login_view, name='login'),  # Replace 'login_view' with your actual view function
]
