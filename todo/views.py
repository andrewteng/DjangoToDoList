from django.contrib.auth import logout
from django.shortcuts import render_to_response  
from django.http import HttpResponseRedirect, HttpResponse
from todo.models import Item 

def login (request):
    if (request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate (email = email, password = password)
        if user:
                if user.is_active:
                    login (request, user)
                    return HttpResponseRedirect ('status_report.html')
        else
            return HttpResponse ("Email/Password not found.")
    else
        return render_to_response ('home.html')


def logout(request):
    logout(request)
    return HttpResponseRedirect('/')
                              
def status_report(request):  
    todo_list = Item.objects.all()
    return render_to_response('status_report.html', { 'todo_list': todo_list })
