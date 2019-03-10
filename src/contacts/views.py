from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.

def contact_view(request, *args, **kwargs):
    if request.method == 'POST':
        # Register User 
        form_full_name = request.POST['name']
        form_email = request.POST['email']
        form_message = request.POST['message']
        form_designation = request.POST['designation']

        subject = 'Site Contact Form'
        from_email = settings.EMAIL_HOST_USER
        to_email = ['mkdeveloper1997@gmail.com']
        contact_message = "Name: %s,\nDesignation: %s,\nEmail: %s,\nMessage: %s"%(
            form_full_name,
            form_designation,
            form_email,
            form_message)

        send_mail(subject, 
            contact_message,
            from_email,
            to_email,
            fail_silently=False)

        messages.success(request, 'Your Message Hase Been Send')

        if form_full_name is None:
            print("Null Value")

        return redirect('contact')
        # return render(request, "success.html")
    else:
        return render(request, "contact.html")




