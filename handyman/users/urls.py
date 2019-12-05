from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.index , name='users-index'),
    path('profile/', views.profile, name='users-profile'),
    path('register/', views.register, name='users-register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='users-login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='users-logout'),
]
