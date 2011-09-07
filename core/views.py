from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic.simple import direct_to_template
from core.models import Speaker, Talk

#def homepage(request):
#    context = RequestContext(request)
#    return render_to_response('index.html', context)

def homepage(request, template=None): #	Unpacking do dict
   return render_to_response(template, RequestContext(request))

def speaker(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return direct_to_template(request, 'core/speaker.html', {'speaker': speaker})

def talks(request):
    return direct_to_template(request, 'core/talks.html', {'morning_talks': Talk.objects.at_morning(),'afternoon_talks': Talk.objects.at_afternoon(),})

def talk_details(request, talk_id):
    talk = get_object_or_404(Talk, id=talk_id)
    return direct_to_template(request, 'core/talk.html', {'talk': talk, 'slides': talk.media_set.filter(type="SL"), 'videos': talk.media_set.filter(type="YT"),})

