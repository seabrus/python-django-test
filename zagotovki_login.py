# ==========================================================
#   How to create a new user
# ==========================================================

from django.contrib.auth.models import User
user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

new_user = User.objects.create_user(self.cleaned_data['username'],
                                  self.cleaned_data['email'],
                                  self.cleaned_data['password1'])

new_user.first_name = self.cleaned_data['first_name']
new_user.last_name = self.cleaned_data['last_name']
new_user.save()

# http://stackoverflow.com/questions/11287485/taking-user-input-to-create-users-in-django
#     SEE also:               
# http://www.tangowithdjango.com/book/chapters/login.html
# http://www.obeythetestinggoat.com/using-the-built-in-views-and-forms-for-new-user-registration-in-django.html

>>>   forms.py
from django.contrib.auth.models import User
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

>>>   views.py
from forms import UserForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
def adduser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(new_user)
            # redirect, or however you want to get to the main view
            return HttpResponseRedirect('main.html')
    else:
        form = UserForm() 
    return render(request, 'adduser.html', {'form': form}) 

>>>   template 'adduser.html'
<form method="post" action="">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Create a new user account" />
</form>





# ==========================================================
# ==========================================================
# ==========================================================

if request.user.is_authenticated():
    # Do something for authenticated users.
    ...
else:
    # Do something for anonymous users.
    ...


from django.contrib.auth import authenticate, login

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
            ...
    else:
        # Return an 'invalid login' error message.
        ...


from django.conf import settings
from django.shortcuts import redirect

def my_view(request):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    # ...

from django.shortcuts import render

def my_view(request):
    if not request.user.is_authenticated():
        return render(request, 'myapp/login_error.html')
    # ...


from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    ...

from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def my_view(request):
    ...
from django.contrib.auth import views as auth_views

url(r'^accounts/login/$', auth_views.login),


from django.contrib.auth.decorators import login_required, permission_required

@permission_required('polls.can_vote', raise_exception=True)
@login_required
def my_view(request):
    ...


urlpatterns = [
    url('^', include('django.contrib.auth.urls'))
]
^login/$ [name='login']
^logout/$ [name='logout']
^password_change/$ [name='password_change']
^password_change/done/$ [name='password_change_done']


from django.contrib.auth import views as auth_views

urlpatterns = [
    url('^change-password/', auth_views.password_change)
]
urlpatterns = [
    url(
        '^change-password/',
        auth_views.password_change,
        {'template_name': 'change-password.html'}
    )
]


# ADD a new user form
# http://www.obeythetestinggoat.com/using-the-built-in-views-and-forms-for-new-user-registration-in-django.html

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = patterns('',
    url('^register/', CreateView.as_view(
            template_name='register.html',
            form_class=UserCreationForm,
            success_url='/'
    )),
    url('^accounts/', include('django.contrib.auth.urls')),

    # rest of your URLs as normal
)

# =================================================================
# =================================================================
# =================================================================

registration/login.html template you can use as a starting point. It assumes you have a base.html template that defines a content block:

{% extends "base.html" %}

{% block content %}

{% if form.errors %}
<p>Your username and password didn't match. Please try again.</p>
{% endif %}

{% if next %}
    {% if user.is_authenticated %}
    <p>Your account doesn't have access to this page. To proceed,
    please login with an account that has access.</p>
    {% else %}
    <p>Please login to see this page.</p>
    {% endif %}
{% endif %}

<form method="post" action="{% url 'django.contrib.auth.views.login' %}">
{% csrf_token %}
<table>
<tr>
    <td>{{ form.username.label_tag }}</td>
    <td>{{ form.username }}</td>
</tr>
<tr>
    <td>{{ form.password.label_tag }}</td>
    <td>{{ form.password }}</td>
</tr>
</table>

<input type="submit" value="login" />
<input type="hidden" name="next" value="{{ next }}" />
</form>

{# Assumes you setup the password_reset view in your URLconf #}
<p><a href="{% url 'password_reset' %}">Lost password?</a></p>

{% endblock %}




{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}. Thanks for logging in.</p>
{% else %}
    <p>Welcome, new user. Please log in.</p>
{% endif %}


















"""
Rather if you are looking for a way to limit access to logged in users, see the login_required() decorator.
"""
from django.contrib.auth import authenticate
user = authenticate(username='john', password='secret')
if user is not None:
    # the password verified for the user
    if user.is_active:
        print("User is valid, active and authenticated")
    else:
        print("The password is valid, but the account has been disabled!")
else:
    # the authentication system was unable to verify the username and password
    print("The username and password were incorrect.")
