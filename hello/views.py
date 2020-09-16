from django.shortcuts import render
from django.views import generic
from .models import Hello
# Create your views here.
def view_count(request, post_id):
	post = Hello.objects.get(id=post_id)   
    post.hello_views += 1
    post.save() 

resp.set_cookie('dj4e_cookie', 'd8012652', max_age=1000)
    