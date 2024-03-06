from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest


def index_view(request: HttpRequest) -> HttpResponse:
    
    context = {}
    return render(request, 'core/index.html', context)

# ----------------------------------------------------------------

def about_us_view(request: HttpRequest) -> HttpResponse:
    
    context = {}
    return render(request, 'core/about-us.html', context)