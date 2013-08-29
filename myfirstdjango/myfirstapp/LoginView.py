# login/logout view

##from django import forms
#from django.contrib.sessions.models import Session
#from django.shortcuts import render
#import requests
#from django.contrib.auth import User    #maybe no
#from django.contrib.auth.models import User
#from .forms import LoginForm    #it imports LoginForm form
#from django.contrib.auth import login, authenticate    #oki
#from django.contrib import auth    #maybe this or the line above
#from django.http import HttpResponseRedirect
#from django import forms    #form module




#class loginForm (forms.Form):    #to define the login form
    #username = forms.CharField( label=('username', max_length=30) )
    #password = forms.CharField( label=('password'), widget=forms.PasswordInput )
    #user = None    #it allow access to user object
    ##def clean(self):    #further check for validation
        ##if self._errors: return
    ##def __unicode__(self):
        ##return self.name
    #def clean_password(self):    #check if the password is longer than 5 words
        #password = self.cleaned_data.get('password', "write the password please")
        #NumWord = len (password.split())
        #if NumWord < 5:
            #raise forms.ValidationError("Not enough words!")
        #return password

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login    #module to login, authentication
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout    #module to logout
from django.contrib.auth.decorators import login_required    #module to check if user is logged in
from .forms import RegForm    #registration form




#def clean_username (self): 
        #try:
            #User.objects.get(username=self.cleaned_data['username'])
        #except User.DoesNotExist:
            #return self.cleaned_data['username']
        #raise forms.ValidationError(USERNAME_ALREADY_IN_USE)


def loginTry(request):
    message1 = "this is the last render"
    if request.method == 'POST': # If the form has been submitted
        form = LoginForm(request.POST)    #A form bound to the POST data
        if form.is_valid():    #to check whether a form is bound to valid data
            username = form.cleaned_data['username']
            #email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            #username = request.POST['username']
            #password = request.POST['password']
            user = authenticate ( username=username, password=password )
            if request.user.is_authenticated():    #it checks if the user is already authenticated
                messageAuthenticated = "you are already authenticated"
                return render ( request, 'myfirstapp/LogOutTemp.html', { 'message' : messageAuthenticated } )
            else:
                try:
                    UserCheck = User.objects.get(username=username)
                except User.DoesNotExist:
                    messageName = 'the user not exists'
                    return render ( request, 'myfirstapp/LoginTemp.html', {'message' : messageName} )
                if user is not None :
                    #the password is correct
                    if user.is_active:
                        #the password is correct and the user is active
                        login (request, user)
                        return HttpResponseRedirect('/SdnBoss/')
                        #message2 = "the password is correct and user is active"
                        #return render ( request, 'myfirstapp/LoginTemp.html', {'message' : message2} )
                    else:
                        message2 = "the user is not active"
                        return render ( request, 'myfirstapp/LoginTemp.html', { 'message' : message2 } )
                else:
                    message21 = "please verify the password"
                    return render ( request, 'myfirstapp/LoginTemp.html', { 'message' : message21, } )
            #else:
                #message = "values form are not valid"
                #return render ( request, 'myfirstapp/LoginTemp.html', { 'message' : message } )
    else:
        form = LoginForm()    #unbound form
    return render ( request, 'myfirstapp/LoginTemp.html', { 'message' : message1, 'form' : form } )


#the logout view

@login_required(login_url="/login/", redirect_field_name="requestUrl")
def logoutView(request):
    messageLogOut = "logged off"
    logout(request)
    return render ( request, 'myfirstapp/LogOutTemp.html/', { 'message' : messageLogOut } )



#the registration view first way

#def regView(request):
    #messageNo = "i'm in the last render'"
    #if request.method == 'POST': # If the form has been submitted
        #form = RegForm(request.POST)    #A form bound to the POST data
        #if form.is_valid():    #to check whether a form is bound to valid data
            #username = form.cleaned_data['username']
            ##passwOne = form.cleaned_data['passw_One']
            #passTwo = form.cleaned_data['pass_Two']
            #email = form.cleaned_data['email']
            ##NewUser = form.save()
            #NewUser = User.objects.create_user ( username=username, password=passTwo, email=email)
            ##NewUser = User ( username=username, password=passTwo, email=email)
            ##NewUser.save()
            #messageOki = "you have created a new user"
            #return render ( request, 'myfirstapp/LoginTemp.html', { 'message' : messageOki, } )
    #else:
        #form = RegForm()
        #return render ( request, 'myfirstapp/RegTemp.html', { 'form' : form } )
    #return render ( request, 'myfirstapp/RegTemp.html', { 'message' : messageNo, 'form' : form } )

#second way

#def regView(request):
    #messageNo = "i'm in the last render'"
    #if request.method == 'POST': # If the form has been submitted
        #form = RegForm(request.POST)    #A form bound to the POST data
        #if form.is_valid():    #to check whether a form is bound to valid data
            #username = form.cleaned_data['username']
            ##passOne = form.cleaned_data['pass_One']
            ##passTwo = form.cleaned_data['pass_Two']
            #email = form.cleaned_data['email']
            #NewUser = User.objects.create_user ( username = username,  email = email )
            #messageOki = "you have created a new user"
            #return render ( request, 'myfirstapp/RegTemp.html', { 'message' : messageOki, 'form' :form } )
    #else:
        #form = RegForm()
        #return render ( request, 'myfirstapp/RegTemp.html', {'form' : form } )
    #return render ( request, 'myfirstapp/RegTemp.html', { 'message' : messageNo, 'form' : form } )


#REGISTRATION WORK IN PROGRESS

def regView(request):
    messageNo = "i'm in the last render'"
    if request.method == 'POST': # If the form has been submitted
        form = RegForm(request.POST)    #A form bound to the POST data
        if form.is_valid():    #to check whether a form is bound to valid data
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            username = form.cleaned_data['username']
            passOne = form.cleaned_data['pass_One']
            passTwo = form.cleaned_data['pass_Two']
            email = form.cleaned_data['email']
            #NewUser = form.save()
            NewUser = User.objects.create_user ( first_name=firstName, last_name=lastName, 
                                                username=username, password=passTwo, email=email)
            #NewUser = User ( username=username, password=passTwo, email=email)
            #NewUser.save()
            messageOki = "you have created a new user"
            return render ( request, 'myfirstapp/LoginTemp.html', { 'message' : messageOki, } )
    else:
        form = RegForm()
        return render ( request, 'myfirstapp/RegTemp.html', { 'form' : form } )
    return render ( request, 'myfirstapp/RegTemp.html', { 'message' : messageNo, 'form' : form } )


#actions for the authenticated user

from .forms import authUser


#def authUserView(request):
    #form = authUser()
    ##if request.method == 'POST':
        ##form = authUser(request.POST)
        ##if form.is_valid():
            ##userAction = form.cleaned_data['userAction']
        ##else:
            ##form = authUser()
    #return render( request, 'myfirstapp/authUser.html', { 'form' : form} )




#call profile information

from django.contrib.sessions.models import Session    #to use session variable



def authUserInfo(request, username):
    a = type (username)
    user = User.objects.get(username=username)
    #request.session [username] ['profile'] = {}
    #request.session [username] ['profile']['name'] = user.get_full_name()
    #request.session [username] ['profile']['email'] = user.get_email()
    #request.session [username] ['profile']['permission'] = user.get_group_permissions()
    bugOne = {}
    bugOne['username']['profile'] = user.get_full_name()

    
    return render ( request, 'myfirstapp/authUser.html', { 'name' : request.session [username] ['profile']['name'],
                                                        'email' : request.session [username] ['profile']['email'],
                                                        'perm' : a } )


#TO TRY A FORM

#from django.shortcuts import render
#from django.http import HttpResponseRedirect
#from .forms import ContactForm

#def contact(request):
    #message1 = "i'm in the last render"
    #if request.method == 'POST': # If the form has been submitted...
        #form = ContactForm(request.POST) # A form bound to the POST data
        #if form.is_valid(): # All validation rules pass
            #message = "form is valid"
            #return HttpResponseRedirect('contact.html', { 'message' : message} ) # Redirect after POST
    #else:
        #form = ContactForm() # An unbound form

    #return render(request, 'myfirstapp/contact.html', { 'message' : message1,
        #'form': form,
    #})