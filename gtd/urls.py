from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^report/$', 'todo.views.status_report'),
    url(r'^home/$', 'todo.views.login'),
    #url(r'^logout/$', logout_page),
    url(r'^createAcct/$', 'todo.views.createAcct'),
    url(r'^addTask/$', 'todo.views.addTask'),                
                       
    # Serve static content.
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'static'}),
)
