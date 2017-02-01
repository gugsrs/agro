from django.http import HttpResponse
from django.template import loader
from django.template.defaulttags import csrf_token
from django.shortcuts import render, redirect
from django.http import Http404 

from safra.models import Harvest


class HarvestView:
    '''
    Harvest View define crud methods.
    '''
    
    def create(request):
        template = 'safra/create_harvest.html'
        if request.method == 'POST':
            name = request.POST.get('name', '')
            date_start = request.POST.get('date_start', '')
            date_end = request.POST.get('date_end', '')
            harvest = Harvest(name=name, date_start=date_start,
                              date_end=date_end)
            harvest.save()
        return render(request, template, {})


    def harvests(request):
        template = 'safra/harvests.html'
        harvests = Harvest.objects.all()
        return render(request, template, {'harvests': harvests})


    def edit(request):
        template = 'safra/edit_harvest.html'
        harvest_id = request.GET.get('harvest_id', None)
        if not harvest_id:
            harvest_id = request.POST.get('harvest_id', None)
        if harvest_id is not None:
            harvest = Harvest.objects.get(pk=harvest_id)
        else:
            raise Http404
        if request.method == 'POST':
            name = request.POST.get('name', '')
            date_start = request.POST.get('date_start', '')
            date_end = request.POST.get('date_end', '')
            harvest.name = name
            harvest.date_start = date_start
            harvest.date_end = date_end
            harvest.save()
            return redirect(HarvestView.harvests)

        if harvest:
            return render(request, template, {'harvest': harvest})
        return render(request, template, {})


    def delete(request):
        harvest_id = request.GET.get('harvest_id', None)
        if harvest_id is not None:
            harvest = Harvest.objects.get(pk=harvest_id)
        if not harvest:
            raise Http404
        harvest.delete()
        return redirect(HarvestView.harvests)
