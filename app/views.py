from typing import Any
from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView,FormView,ListView
from app.forms import *
from django.http import HttpResponse
class Temp(TemplateView):
    template_name='Temp.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ECDO=super().get_context_data(**kwargs)
        #ECDO['name']='Ashu'
        ECDO['SFO']=SchoolForm
        return ECDO
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('data is Inserted')


class SchoolInsertForm(FormView):
    form_class=SchoolForm
    template_name='SchoolInsertForm.html'

    def form_valid(self, form) -> HttpResponse:
        form.save()
        return HttpResponse('Data is inserted')


class DisplaySchool(ListView):
    model=School
    template_name='DisplaySchool.html'
    context_object_name='sclist'
    ordering=['Sage']































