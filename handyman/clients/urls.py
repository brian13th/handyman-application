from django.urls import path
from .views import ClientPostListView


urlpatterns = [
    path('client-home/', ClientPostListView.as_view(template_name='clients/clienthome.html'), name='client-home')
]
