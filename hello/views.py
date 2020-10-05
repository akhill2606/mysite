from django.shortcuts import render
from django.views import generic
from .models import Hello
from django.http import HttpResponse
# Create your views here.
def Hello(request):
    hello_views = request.session.get('hello_views', 0)
    request.session['hello_views'] = hello_views+ 1
    #if num_visits > 4 : del(request.session['hello_views'])
    context = {
        'hello_views': hello_views,
    }
    

resp.set_cookie('dj4e_cookie', 'd8012652', max_age=1000)