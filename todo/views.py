from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render_to_response, render, get_object_or_404
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
    auth_logout(request)
    return HttpResponseRedirect('/home')
                              
<<<<<<< HEAD
#def status_report(request):  
 #   todo_listing = []  
  #  for todo_list in Item.objects.all():  
   #     todo_dict = {}  
    #    todo_dict['list_object'] = todo_list.title  
     #   todo_listing.append(todo_dict)  
   # return render_to_response('status_report.html', { 'todo_listing': todo_listing })

def status_report(request): 
    todo_list = Item.objects.all()
    if(request.POST.get('Add')):
        item = Item(item_text=request.POST.get('Task'))
        item.save()
    todo_list=Item.objects.all()
    template= loader.get_template('status_report.html')
    context = RequestContext(request, {
        'todo_list': todo_list, 
    })
    return HttpResponse(template.render(context))

def index(request):
    todo_list= Item.objects.all()
    context = {'todo_list':todo_list}
    return render(request, 'status_report.html', context)

def delete(request, item): 
    item = Item.objects.get(item=item)
    item.completed=True
    item.delete()
    return HttpResponse('/')
=======
def status_report(request):    
    
    todo_list = Item.objects.all()
    if (request.POST.get('Add')):
        item1 = Item (title=request.POST.get ('Item'))
        item1.save()
    
    elif (request.POST.get('delete') and todo_list and request.POST.get('listid')):
        item2 = get_object_or_404 (Item, id =request.POST.get('listid'))
        item2.delete()
    todo_list = Item.objects.all()
    template = loader.get_template('status_report.html')
    context = RequestContext (request, {'todo_list': todo_list})
    

    return HttpResponse(template.render(context))


def delete (request, todo_id):
    items = Item.objects.all()
    if request.method == "POST":
        try:
            litem = Item.objects.get (id = request.POST['todo_id'])
            litem.deleted = not litem.deleted
            litem.save()
        except Item.DoesNotExist:
            pass

    return render_to_reponse ("status_report.html", {'items':items})
>>>>>>> 0615f270a6687ed080a45a8b22ad2ba69faebe38
