from django.shortcuts import render
from django.views.generic import ListView
from .models import CompanyPost
from django.apps import apps

clientpost = apps.get_model('clients', 'ClientPost')

class CompanyPostListView(ListView):
    model = clientpost