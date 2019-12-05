from django.urls import path
from .views import CompanyPostListView

urlpatterns = [
    path('company-home/', CompanyPostListView.as_view(template_name='companies/companyhome.html'), name='company-home')
]
