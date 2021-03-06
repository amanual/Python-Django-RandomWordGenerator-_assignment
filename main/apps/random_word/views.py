from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from models import *
# Create your views here.

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0       
 
    request.session['random'] = get_random_string(length=14)
    request.session['counter'] += 1      
    
    return render(request, 'random_word/index.html')
def reset(request):
    request.session['counter'] = 0
    return redirect('/')