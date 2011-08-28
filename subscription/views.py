from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms 
from django.core.mail import send_mail
from subscription.forms import	SubscriptionForm
from subscription.models import	Subscription
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse, resolve
from django.http import HttpResponseRedirect

def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
	return new(request)


def new(request):
    form = SubscriptionForm()
    context = RequestContext(request, {'form': form})
    return render_to_response('subscription/new.html', context)

def create(request):
    form = SubscriptionForm(request.POST)
    
    if not form.is_valid():
        context = RequestContext(request, {'form': form})
        return render_to_response('subscription/new.html', context)

    subscription = form.save()
    send_mail(
        subject = u'Inscricao no EventeX',
        message = u'Obrigado por se inscrever no EventeX!',
        from_email = 'eventex@rrmartins.com',
        recipient_list = [ subscription.email ],
    )

    return HttpResponseRedirect(reverse('subscription:success', args=[ subscription.pk ]))


def success(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    context = RequestContext(request, {'subscription': subscription})
    return render_to_response('subscription/success.html', context)

