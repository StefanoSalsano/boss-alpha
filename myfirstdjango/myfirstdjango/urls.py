from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myfirstdjango.views.home', name='home'),
    # url(r'^myfirstdjango/', include('myfirstdjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    url(r'^myfirstapp/$', 'myfirstapp.views.index'),
    url(r'^myfirstapp/info/$', 'myfirstapp.views.info'),
    url(r'^myfirstapp/(?P<poll_id>\d+)/$', 'myfirstapp.views.detail'),
    url(r'^myfirstapp/(?P<poll_id>\d+)/results/$', 'myfirstapp.views.results'),
    url(r'^myfirstapp/(?P<poll_id>\d+)/vote/$', 'myfirstapp.views.vote'),    
    
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/home/virtualmininetu/djcode/python-test/myfirstdjango/media'}),
    url(r'^admin/', include(admin.site.urls) ),
    url(r'^SdnBoss/$', 'myfirstapp.SwHo.switchesInfo'),    #WORKINPROGRESS (new)
    url(r'^GoSwitch/(?P<DpidUrl>.+)/$', 'myfirstapp.SingleSwitch.singleSwitch'),    #WORKINPROGRESS HERE
    url(r'^Boss/FloodlightContrLoadedModules/$', 'myfirstapp.LoadMod.LoadedMod'),
    url(r'^prova/$', 'myfirstapp.prova1.prova'),    #DEVELOPMENT: to parse new scripting
    url(r'^casa/$', 'myfirstapp.debug1.debug1'),    #DEVELOPMENT: to parse new scripting
    url(r'^bug1/$', 'myfirstapp.bug1.bugOne'),    #DEVELOPMENT: to parse session 
    url(r'^bug2/$', 'myfirstapp.bug2.bugTwo'),    #DEVELOPMENT: to parse session 
    url(r'^bug3/$', 'myfirstapp.bug3.bugThree'),    #DEVELOPMENT: to parse session 
    url(r'^bug4/$', 'myfirstapp.bug4.bugFour'),    #DEVELOPMENT: to parse session 
    url(r'^login/$', 'myfirstapp.LoginView.loginTry'),    #login view url
    #url(r'^login/$', 'django.contrib.auth.views.login', {'LoginTemp.html': 'LoginTemp.html'}),    #to login
    url(r'^logout/$', 'myfirstapp.LoginView.logoutView'),
    url(r'^usereg/$', 'myfirstapp.LoginView.regView'),
    url(r'^action/(?P<username>.*)', 'myfirstapp.LoginView.authUserInfo'),
)
