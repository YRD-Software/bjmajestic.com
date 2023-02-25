""" This module contains the views for the contact_us app."""
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from django.core.mail import BadHeaderError
from django.shortcuts import render
from django.conf import settings
from contact_us.forms import ContactForm

# Create your views here.


def contact_us(request):
    """ This function renders the contact us page. And sends an email to the admin"""
    if request.method == 'GET':
        form = ContactForm()
        success = ''
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            message = contruct_email(form)
            try:
                # Send email
                client = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
                client.set_debuglevel(0)
                client.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                client.sendmail(settings.DEFAULT_FROM_EMAIL,
                                settings.DEFAULT_TO_EMAIL, message.as_string())
                client.quit()
                # Success message
                success = "Success! Thank you for your message. We will get back to you \
                    as soon as possible."
            except BadHeaderError:
                success = "Oops! Try again later."
                print("Bad Header Error")
            except smtplib.SMTPAuthenticationError:
                success = "Oops! Try again later."
                print("SMTP Authentication Error")
            except smtplib.SMTPConnectError:
                success = "Oops! Try again later."
                print("SMTP Connect Error")

    context = {'page': 'contact', 'form': form, 'success': success}
    return render(request, 'contact_us/contact_us.html', context)


def contruct_email(form):
    """contruct_email Extracts the data from the form and constructs an email.

    Args:
        form (ContactForm): the form containing the data from the contact us page.

    Returns:
        MIMEMultipart: the email to be sent to the admin.
    """
    subject = form.cleaned_data['subject']
    from_email = form.cleaned_data['from_email']
    body = form.cleaned_data['message']
    body = f"This is an alert from the contact us page. \
            \n\nFrom: {from_email}\
            \nSubject: {subject}\
            \n\n{body} \n\n"
    message = MIMEMultipart()
    message['From'] = settings.DEFAULT_FROM_EMAIL
    message['To'] = settings.DEFAULT_TO_EMAIL
    message['Subject'] = "Majestic Web - New Alert from Contact Us Page"
    message.attach(MIMEText(body, 'plain'))
    return message
