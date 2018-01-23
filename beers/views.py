from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def first_view(request):
    context={
        "sample_var": "ejemplo",
    }
    return render(request, 'beers.html', context)