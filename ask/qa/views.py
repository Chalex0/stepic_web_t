from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

# Create your views here.
 
def test(request, *args, **kwargs):
    return HttpResponse('OK')
