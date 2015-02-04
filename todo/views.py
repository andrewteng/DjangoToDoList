from django.contrib.auth import logout
from django.shortcuts import render_to_response  
from django.http import HttpResponseRedirect
from datetime import datetime 

from todo.models import List  
from todo.models import Item  

'''
def login(request):
    user_obj = User.objects.filter(email=request.POST.get('email'), password=request.POST.get('password'))
    if user_obj.count():
        print (user_obj)
        request.session['user_id']=user_obj[0].id
        request.session['fname']=user_obj[0].fname
    return HttpResponseRedirect('/')
'''

def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')

def login(request):

    return render_to_response('login.html')

def addTask(request):
#    item_title = request.GET.get('title')
#    item_date = request.GET.get('created_date')
#    item_priority = request.GET.get('priority')
#    item_completed = request.GET.get('completed')
#    new_task = Item(title=item_title,created_date=item_date)
#    new_task.save()
#    return HttpResponse(new_task.id)
    return render_to_response('addTask.html')

def createAcct(request):
    return render_to_response('createAcct.html')
                              
def status_report(request):  

    todo_listing = []  
    for todo_list in Item.objects.all():  
        todo_dict = {}  
        todo_dict['list_object'] = todo_list.title  
        todo_listing.append(todo_dict)  
    return render_to_response('status_report.html', { 'todo_listing': todo_listing })
