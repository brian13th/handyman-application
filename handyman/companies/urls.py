from django.urls import path
from .views import CompanyPostListView, CompanyPostDetailView

urlpatterns = [
    path('company-home/', CompanyPostListView.as_view(template_name='companies/companyhome.html'), name='company-home'),
    path('company-home/<pk>/', CompanyPostDetailView.as_view(template_name='companies/companypost.html'), name='company-post'),
]
