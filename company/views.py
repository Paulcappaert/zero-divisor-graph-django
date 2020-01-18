from django.shortcuts import render
from django.views.generic.list import ListView
from .models import FishingCompany

class CompaniesView(ListView):

    model = FishingCompany
    template_name = 'company/companies.html'
    context_object_name = 'companies'
