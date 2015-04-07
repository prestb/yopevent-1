from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from yop.models import Event
from yop.forms import EventForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required


def home(request):
    context = RequestContext(request)
    return render_to_response('home.html', context)
    # return render_to_response('django_facebook/home.html', context)


@csrf_protect
@login_required(login_url='/')
def handle_event(request):
    # u = request.user
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            program = form.cleaned_data['program']
            spot = form.cleaned_data['spot']
            start_date = form.cleaned_data['start_date']
            start_time = form.cleaned_data['start_time']
            duration = form.cleaned_data['duration']
            description = form.cleaned_data['description']
            event = Event(program=program, spot=spot, start_date=start_date, start_time=start_time, duration=duration,
                          description=description, uid=request.user.get_user_id())
            event.save()
            return HttpResponseRedirect('/myevents')
    else:
        form = EventForm()
    context = RequestContext(request, {"form": form})
    return render_to_response('event.html', context)


@login_required(login_url='/')
def myevents(request):
    if request.user.is_authenticated():
        events = Event.objects.filter(uid=request.user.get_user_id()).order_by('-created_on')
        context = RequestContext(request, {"events": events})
    return render_to_response('myevents.html', context)