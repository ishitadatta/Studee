from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, request, HttpResponseRedirect
from django.template import loader
from django.contrib import messages, auth
from django.shortcuts import render, redirect
import json

from .forms import *
from .models import *
from authentication.models import Account

# Create your views here.


def home(request):
    if request.method == "POST":
        club = Club.objects.get(slug=request.POST['join-club'])
        join_club(request, club)
        messages.success(request, f'You have joined {club.name}. You have earned 1 credit')
        return redirect('clubs:home')
    else:
        clubs = Club.objects.all()
        events = list(Events.objects.values().all())
        event_data = get_events(events)
        context = {
            'clubs': clubs,
            'event_data': json.dumps(event_data)
        }
        template = loader.get_template('clubs/home.html')
        return HttpResponse(template.render(context, request))


def create_club(request):
    if request.method == "POST":
        club_form = ClubForm(request.POST)
        if club_form.is_valid():
            head = Account.objects.get(username=request.user.username)
            club_form = club_form.save(commit=False)
            club_form.head = head
            club_form.save()
            join_club(request, Club.objects.get(slug=club_form.slug), head=True)
            messages.success(request, f'Your club has been created')
            return redirect("clubs:home")
    else:
        club_form = ClubForm()
        context = {
            "create_form": club_form,
            "title": "Create New Club"
        }
        return render(request, "clubs/create_club.html", context)


def create_event(request, slug):
    if request.method == "POST":
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            club = Club.objects.get(slug=slug)
            event_form = event_form.save(commit=False)
            event_form.club = club
            event_form.save()
            messages.success(request, f'Your event has been created')
            return redirect("clubs:club", slug=slug)
    else:
        event_form = EventForm()
        context = {
            "create_form": event_form,
            "title": "Create New Event"
        }
        return render(request, "clubs/create_event.html", context)


def club_view(request, slug):
    if request.method == "POST":
        if 'join-club' in request.POST:
            club = Club.objects.get(slug=slug)
            join_club(request, club)
            messages.success(request, f'You have joined {club.name}. You have earned 1 credit')
            return redirect('clubs:club', slug=slug)
        if 'attend-event' in request.POST:
            attendee = EventAttendees(event=Events.objects.get(id=request.POST['attend-event']), attendee=Account.objects.get(username=request.user.username))
            attendee.save()
            messages.success(request, f'Thank you for attending the event! You earn 0.5 credits')
            return redirect('clubs:club', slug=slug)
        if 'skip-event' in request.POST:
            EventAttendees.objects.filter(event=Events.objects.get(id=request.POST['skip-event']), attendee=Account.objects.get(username=request.user.username)).delete()
            messages.warning(request, f"We're sorry to see you go! 0.5 credits have been deducted")
            return redirect('clubs:club', slug=slug)
        if 'leave-club' in request.POST:
            Members.objects.filter(member__username=request.user.username, club__slug=slug).delete()
            club = Club.objects.get(slug=slug)
            messages.success(request, f'You have left the {club.name}. 1 credit has been deducted')
            return redirect('clubs:club', slug=slug)
        if 'delete-event' in request.POST:
            Events.objects.filter(id=request.POST['delete-event']).delete()
            messages.success(request, f'Your event has been deleted')
            return redirect('clubs:club', slug=slug)
        if 'delete-club' in request.POST:
            Club.objects.filter(slug=slug).delete()
            messages.success(request, f'Your club has been deleted')
            return redirect('clubs:home')
    else:
        club = Club.objects.get(slug=slug)
        members = Members.objects.filter(club=club).all()
        part_vax = full_vax = True
        for member in members:
            if member.approved:
                if member.member.vaccination.vaccination_status == 'Not Vaccinated':
                    full_vax = part_vax = False
                elif member.member.vaccination.vaccination_status == 'Partially Vaccinated':
                    full_vax = False
        if full_vax:
            messages.success(request, f'All the members in our club are fully vaccinated! <i class="fas fa-syringe text-primary"></i>')
        elif part_vax:
            messages.success(request, f'All the members in our club at least partially vaccinated! <i class="fas fa-syringe text-primary"></i>')
        events_list = list(Events.objects.filter(club=club).values().all())
        events = Events.objects.filter(club=club).all()
        event_data = get_events(events_list)
        context = {
            "club": club,
            "members": members,
            'event_data': json.dumps(event_data),
            'events': events,
            'type': 'assignments'
        }
        return render(request, "clubs/club.html", context)


def join_club(request, club, head=False):
    approval = head or not club.approval_required
    user = Account.objects.get(username=request.user.username)
    member = Members(member=user, club=club, approved=approval)
    member.save()


def get_events(events):
    event_list = []
    for event in events:
        event_list.append({
            'name': event['name'],
            'description': event['description'],
            'club': Club.objects.get(slug=event['club_id']).name,
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


def approve_member(request):
    [club, username] = request.POST['approve-member'].split("_")
    member = Members.objects.get(club__slug=club, member__username=username)
    member.approved = True
    member.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

