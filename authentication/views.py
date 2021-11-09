from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.template import loader
from .forms import *
from django.http import HttpResponse


def landingPage(request):
    return render(request, 'home.html')

def homePage(request):
    if request.user.type == 'Student':
        template = loader.get_template('student_home.html')

    else:
        template = loader.get_template('teacher_home.html')
    context={}
    return HttpResponse(template.render(context, request))

def register(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)

        if (request.method == 'POST') and (form.is_valid()):
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=username, password=raw_password)
            login(request, account)

            messageList = messages.get_messages(request)
            for msg in messageList:
                pass
            messages.success(request, f'Your account has been created successfully!')

            return redirect('authentication:login')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'authentication/register.html', context)


def loginView(request):
    context = {}
    user = request.user

    if request.POST:
        form = AccountAuthenticateForm(request.POST)
        # if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  
        if user:
            login(request, user)
            # request.session.set_expiry(600)
            return redirect("home")

        # else:
        #     context['login_form'] = form

    else:
        form = AccountAuthenticateForm()
    if form.non_field_errors():
        messageList = messages.get_messages(request)
        for msg in messageList:
            pass
        messages.error(request, f'The username or password you entered is incorrect. Please try again.')

    context['login_form'] = form
    return render(request, 'authentication/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')