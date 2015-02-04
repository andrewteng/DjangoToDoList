from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User

from todo.models import Item
from todo.forms import Form

def login (request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate (username = username, password = password)
        if user:
                if user.is_active:
                    auth_login (request, user)
                    return HttpResponseRedirect ('/report/') 
        else:
            return HttpResponse ("Username/Password combination not found.")
    else:
        return render(request, 'login.html', {})


def logout(request):
    logout(request)
    return HttpResponseRedirect('/')
                              
def status_report(request):  

    todo_listing = []  
    for todo_list in Item.objects.all():  
        todo_dict = {}  
        todo_dict['list_object'] = todo_list.title  
        todo_listing.append(todo_dict)  
    return render_to_response('status_report.html', { 'todo_listing': todo_listing })
