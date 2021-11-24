from .models import Preference
from .forms import PreferenceForm 
from authentication.models import Account
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse

# Create your views here.


@login_required
def StudentPreference(request):
    template = loader.get_template('preference.html')
    if request.user.type == 'Student':
        if request.POST:
            form = PreferenceForm(request.POST, request.FILES)
            if form.is_valid():
                submit = form.save(commit=False)
                if submit.vaccination_status != 'Not Vaccinated':
                    submit.file = request.FILES['file']
                submit.user = Account.objects.get(username=request.user.username)
                submit.save()
                messages.success(request, f'Your vaccination status has been updated!')

                return redirect('authentication:home')

        else:
            template = loader.get_template('preference.html')
            preference = Preference.objects.get(user__username=request.user.username)
            form = PreferenceForm(instance=preference)
            context = {
                'status_form': form,
                'preference': preference
            }
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('roster.html')
        preferences = Preference.objects.all()
        context = {
            'preferences': preferences
        }
        return HttpResponse(template.render(context, request))
