from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

def main(request):
    args = {}
    args['username'] = auth.get_user(request).username
    return render_to_response('main.html',args)
