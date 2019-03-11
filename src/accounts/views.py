from django.shortcuts import render, redirect
from .models import RegistrationForm
from django.contrib import messages

# from django.contrib.auth.forms import UserCreationForm

# from accounts.forms import RegistrationForm

def registration_view(request, *args, **kwargs):
    if request.method == 'POST':
        text = request.POST['text']
        name = request.POST['name']
        #  Check if user has made inquiry already
        # if request.user.is_authenticated:
        #     user_id = request.user.id
        #     has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
        #     if has_contacted:
        #         messages.error(request, 'You have already made an inquiry for this listing')
        #         return redirect('/listings/'+listing_id)

        registrationForm = RegistrationForm(name=name, text=text)

        registrationForm.save()
        messages.error(request, 'You have registered successfully')
        # return redirect('/accounts/register')
        return render(request, "accounts/register.html")

    else:
        return render(request, "accounts/register.html")





