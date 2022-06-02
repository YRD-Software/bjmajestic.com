from django.core.mail import send_mail, BadHeaderError
from django.http.response import HttpResponse
from contact_us.forms import ContactForm
from django.shortcuts import render, redirect

from django.conf import settings

# Create your views here.


def contact_us(request):
    if request.method == 'GET':
        form = ContactForm()
        success = ''
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, "From " + from_email + "\n" + message,
                          settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_TO_EMAIL])
                success = "Success! Thank you for your message. We will get back to you as soon as possible."
            except BadHeaderError:
                success = "Invalid header found."

    context = {'page': 'contact', 'form': form, 'success': success}
    return render(request, 'contact_us/contact_us.html', context)
