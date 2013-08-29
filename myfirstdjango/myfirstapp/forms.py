# to define form for login
# I use newforms

#from django.utils.translation import ugettext_lazy as _, ugettext
#from django import forms    #form module
#from django.contrib.auth import login, authenticate    #maybe it isn't need here???
##from django.contrib.auth import User    #maybe no
#from django.contrib.auth.models import User
#import string
#from django.forms import ModelForm    #to use class meta to create a form

from django import forms    #it loads form module
#from django.contrib.auth.models import User
from django.forms import ModelForm    #to use class meta to create a form
from django.contrib.auth.models import User    #for the registration form



# form from user instance
#class LoginForm (forms.ModelForm):
    #class Meta:
        #model = User
        #fields = ('username', 'password' )



#the login form

class LoginForm (forms.Form):    #to define the login form
    username = forms.CharField( label=('username'), widget = forms.TextInput(attrs={'placeholder' : 'username'}),
                                error_messages={'required' : 'you didn\'t insert your username'} )
    password = forms.CharField( label=('password'), widget=forms.PasswordInput(attrs={'placeholder' : 'your password'}),
                                error_messages={'required' : 'insert your password please'} )
    def clean_password(self):    #check if the password is longer than 5 words
        passwordCheck = self.cleaned_data.get('password')
        if len (passwordCheck) < 7:
            raise forms.ValidationError('not long enough')
        return passwordCheck
    def __unicode__(self):
        return self.username



#the registration form

class RegForm (forms.Form):
    firstName = forms.CharField( label=('First Name'), required=True, 
                                widget = forms.TextInput(attrs={'placeholder' : 'First Name'}),
                                error_messages={'required' : 'insert your first name please'} )
    lastName = forms.CharField( label=('Last Name'), required=True,
                                widget = forms.TextInput(attrs={'placeholder' : 'Last Name'}),
                                error_messages={'required' : 'insert your last name please'} )
    username = forms.CharField( label=('Username'), max_length=77, required=True,
                                widget = forms.TextInput(attrs={'placeholder' : 'username'}),
                                error_messages={'required' : ' insert your username please'},
                                help_text="max 30 characters" )
    email = forms.EmailField( label=('email'), widget = forms.TextInput(attrs={'placeholder' : 'email'} ),
                                required=True, error_messages={'required' : 'insert your email address please'} )
    pass_One = forms.CharField( label=('Password'), widget=forms.PasswordInput(attrs={'placeholder' : 'password'}) ,
                            error_messages={'required' : 'insert the password, please'} )
    pass_Two = forms.CharField( label=('Repeat Password'), widget=forms.PasswordInput(attrs={'placeholder' : 'confirm password'}),
                                error_messages={'required' : 'confirm the password please'} )
    def clean_username(self):    #unique username check
        usernameChk = self.cleaned_data.get('username')
        try:
            User.objects.get(username=usernameChk)
            raise forms.ValidationError("This username already exists")
        except User.DoesNotExist:
            return usernameChk
    def clean_email(self):    #unique email address check
        emailChk = self.cleaned_data.get('email')
        try:
            User.objects.get(email=emailChk)
            raise forms.ValidationError("This email address already exists")
        except User.DoesNotExist:
            return emailChk
    def clean_pass_One(self):    #password minimun seven control
        passOne = self.cleaned_data.get("pass_One")
        if len( passOne ) < 7:
            raise forms.ValidationError("7 min")
        return passOne
    def clean_pass_Two(self):    #password 7 min and matching passwords check
        passTwo = self.cleaned_data.get("pass_Two")
        passOne = self.cleaned_data.get("pass_One")
        if len( passTwo ) < 7:
            raise forms.ValidationError("7 min")
        else:
            if passOne != passTwo:
                raise forms.ValidationError("the password didn't match")
        return passTwo

#authenticated user action form


OPTION= ( 
        ("op1", "profilo"),
        ("opt2", "logOut")
        )

class authUser(forms.Form):

    c = "casa"
    #UserAction = forms.CharField(label=c, widget=forms.Select(choices = [ (1,2) ] ) )
    UserAction = forms.ChoiceField( label=c, choices = OPTION)











