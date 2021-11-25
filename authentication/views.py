from django import template
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.template import loader
from django.db.models import Max
import json

from .forms import *
from .models import Account
from courses.models import Course
from forum.models import Post
from django.http import HttpResponse
from clubs.models import Club, Events
from scheduler.models import Preference

# Display landing page 
def landingPage(request):
    if request.user.is_authenticated:
        return redirect("authentication:home")
    return render(request, 'landing.html')

# Display home dashboard once logged in
@login_required
def homePage(request):
    events = list(Events.objects.values().all())
    event_data = get_events(events)
    template = loader.get_template('home.html')

    tiers = []
    perks = ['Coffee', 'Cookie', 'Popcorn', 'Ice Cream', 'Donut', 'Burger', 'Meal']
    for i in range(7):
        tiers.append(
            {
                'value': i,
                'image': 'tier_' + str(i) + '.png',
                'points_to_next': request.user.tier_points[i] - request.user.points,
                'perk': perks[i]
            }
        )
    credit_data = [request.user.assignment_credits, request.user.forum_credits, request.user.club_credits, request.user.course_credits]
    credit_stars = Account.objects.filter(username__in=get_credit_star()).all()
    if request.user.vaccination.vaccination_status != 'Fully Vaccinated':
        messages.warning(request, f'Get fully vaccinated in order to attend offline classes or join clubs')
    context = {
        'event_data': event_data,
        'tiers': tiers,
        'credit_data': json.dumps(credit_data),
        'credit_stars': credit_stars
    }
    return HttpResponse(template.render(context, request))

# Sign up
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
            user = Account.objects.get(username=username)
            preference = Preference(user=user)
            if user.type == 'Teacher':
                preference.vaccination_status = 'Fully Vaccinated'
            preference.save()
            messages.success(request, f'Your account has been created successfully!')

            return redirect('authentication:home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'authentication/register.html', context)

# Sign in
def loginView(request):
    context = {}
    if request.user.is_authenticated:
        return redirect("authentication:home")
    if request.POST:
        form = AccountAuthenticateForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("authentication:home")
    else:
        form = AccountAuthenticateForm()
    if form.non_field_errors():
        messages.error(request, f'The username or password you entered is incorrect. Please try again.')

    context['login_form'] = form
    return render(request, 'authentication/login.html', context)

# Log out
def logout_view(request):
    logout(request)
    return redirect('authentication:landing')

# Display events calendar on home dashboard
def get_events(events):
    event_list = []
    for event in events:
        club = Club.objects.get(slug=event['club_id']).name
        event_list.append({
            'name': event['name'],
            'description': event['description'],
            'club': club,
            'year': event['date'].year,
            'month': event['date'].month,
            'day': event['date'].day,
            'hour': event['date'].hour,
            'minute': event['date'].minute,
            'duration': event['duration'],
        })
    return {
        'events': event_list
    }

# User profile page
@login_required
def profile(request):
    template = loader.get_template('authentication/profile.html')
    profile_form = ProfileUpdateForm(instance=Account.objects.get(username=request.user.username))
    context = {
        'profile_form': profile_form
    }
    return HttpResponse(template.render(context, request))

# Edit profile
@login_required
def editProfile(request):
    template = loader.get_template("authentication/editProfile.html")
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=Account.objects.get(username=request.user.username))
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, f'Your account has been updated successfully!')
            return redirect('authentication:profile')
    else:
        profile_form = ProfileUpdateForm(instance=Account.objects.get(username=request.user.username))

    context = {
        'profile_form': profile_form
    }
    return HttpResponse(template.render(context, request))

# Delete user
def deleteuser(request):
    if request.method == 'POST':
        Account.objects.filter(username=request.user.username).delete()
        messages.success(request, 'Your account has been deleted. To create a new account, register here!')
        return redirect('authentication:register')
    else:
        template = loader.get_template("authentication/deleteAccount.html")
        context = {}
        return HttpResponse(template.render(context, request))

# User settings
@login_required
def accountSettings(request):
    template = loader.get_template("authentication/accountSettings.html")
    context = {}
    return HttpResponse(template.render(context, request))

# Change password
@login_required
def password_change_done(request):
    messages.success(request, f'Your account has been updated successfully!')
    return redirect('account_settings')

# Display tar student with highest credits
def get_credit_star():
    max_credits = 0
    credit_stars = []
    users = Account.objects.filter(type='Student').all()
    for user in users:
        if user.points > max_credits:
            max_credits = user.points

    for user in users:
        if user.points == max_credits:
            credit_stars.append(user.username)
    return credit_stars

