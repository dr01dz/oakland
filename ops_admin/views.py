from django.shortcuts import render
from django.http import HttpResponse
from .models import Retailer, Order, Concession, ConcessionNote
from django.views.generic.list import ListView


def home(request):

    return HttpResponse('<h1>App Home</h1>')


def ops_splash(request):

    return HttpResponse('<h1>Ops Admin Home</h1>')


def order_upload(request):

    return HttpResponse('<h1>Upload</h1>')


def order_calendar(request):

    return HttpResponse('<h1>Calendar</h1>')


class RetailerListView(ListView):

    model = Retailer

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['title'] = 'Select Retailer'

        return context


def ops_checklist(request, retailer):

    suppliers = [[supplier['scode'] for supplier in retailer.slist.values()]
                 for retailer in Retailer.objects.filter(rcode=retailer)]

    received = [
        order.scode for order in Order.objects.filter(rcode=retailer)]

    name = [retailer.rname for retailer in Retailer.objects.filter(
        rcode=retailer)][0]

    concessions = Concession.objects.all()

    notes = ConcessionNote.objects.all()

    context = {

        'title': f'{name}',
        'suppliers': suppliers,
        'received': received,
        'concessions': concessions,
        'notes': notes,
    }

    return render(request, 'ops_admin/checklist.html', context)
