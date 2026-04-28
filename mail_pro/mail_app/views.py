from django.shortcuts import render, redirect 
from django.contrib.auth import login, logout 
from django.contrib.auth.decorators import login_required 
from mail_app.models import UserInfoModel, ContactModel
from mail_app.forms import RegisterForm, LoginForm, ContactForm

from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings



def home_page(request):
    return render(request, 'home.html')


def contact_page(request):
    if request.method == 'POST':
        form_data = ContactForm(request.POST)
        if form_data.is_valid():
            contact_instance = form_data.save()         
            subject = f"New Contact Message: {contact_instance.subject}"
            message = f"From: {contact_instance.email}\n\nMessage:\n{contact_instance.messages}"
            
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER], 
                fail_silently=False,
            )
            return redirect('home_page')
    else:
        form_data = ContactForm()
        
    context = {
        'form_data': form_data,
        'form_title': 'Contact Us',
        'btn_name': 'Send Message',
    }
    return render(request, 'base_auth.html', context)


def register_page(request):
    if request.method == 'POST':
        form_data = RegisterForm(request.POST)
        if form_data.is_valid():
            user = form_data.save()
            
            subject = "Welcome to Our Platform!"
            email_context = {'user': user}
            html_content = render_to_string('emails/welcome_email.html', email_context)
            text_content = strip_tags(html_content) 
            
            email = EmailMultiAlternatives(
                subject=subject,
                body=text_content,
                from_email=settings.EMAIL_HOST_USER,
                to=[user.email],
            )
            email.attach_alternative(html_content, "text/html")
            email.send()
            
            return redirect('login_page')
    else:
        form_data = RegisterForm() 
        
    context = { 
        'form_data': form_data, 
        'form_title': 'Register Form', 
        'btn_name': 'Register', 
    }
    return render(request, 'base_auth.html', context)


def login_page(request):
    if request.method == 'POST':
        form_data = LoginForm(request, data=request.POST) 
        if form_data.is_valid():
            user = form_data.get_user()
            login(request, user)
            return redirect('home_page')
    else:
        form_data = LoginForm() 
        
    context = { 
        'form_data': form_data, 
        'form_title': 'Login Form', 
        'btn_name': 'Login', 
    }
    return render(request, 'base_auth.html', context)


@login_required 
def logout_page(request):
    logout(request)
    return redirect('login_page')
