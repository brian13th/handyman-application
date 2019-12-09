from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ClientPost
from django.apps import apps

companypost = apps.get_model('companies', 'CompanyPost')

class ClientPostListView(ListView):
    model = companypost

class ClienPostDetailView(DetailView):
    model = companypost