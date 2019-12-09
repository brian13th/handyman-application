from django.urls import path
from .views import ClientPostListView, ClienPostDetailView


urlpatterns = [
    path('client-home/', ClientPostListView.as_view(template_name='clients/clienthome.html'), name='client-home'),
    path('client-home/<pk>/', ClienPostDetailView.as_view(template_name='companies/companypost.html'), name='company-post'),
]
