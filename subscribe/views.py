from django.shortcuts import redirect, render
from django.urls import reverse
from subscribe.forms import SubscribeForm

# Create your views here.

def subscribe(request):
    subscribe_form = SubscribeForm()
    email_error = ""
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            # email = subscribe_form.cleaned_data['email']
            # first_name = subscribe_form.cleaned_data['first_name']
            # last_name = subscribe_form.cleaned_data['last_name']
            # subscribe = Subscribe(email=email, first_name=first_name, last_name=last_name)
            # subscribe.save()
            return redirect(reverse('thank_you'))
    context={"form":subscribe_form, "email_error":email_error}
    return render (request, 'subscribe/subscribe.html',context)

def thank_you(request):
    context={}
    return render(request, 'subscribe/thank_you.html',context)
