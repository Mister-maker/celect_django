from django.shortcuts import render, redirect
from .models import RegistrationForm
from django.contrib import messages
from django.core.mail import send_mail

# from django.contrib.auth.forms import UserCreationForm

# from accounts.forms import RegistrationForm

def registration_view(request, *args, **kwargs):
    if request.method == 'POST':
        student_name = request.POST['student_name']
        course = request.POST['course']
        email = request.POST['email']
        phone = request.POST['phone']
        roll_number = request.POST['roll_number']
        linkedin_url = request.POST['linkedin_url']
        github_url = request.POST['github_url']
        portfolio_url = request.POST['portfolio_url']
        date_of_birth = request.POST['date_of_birth']
        resume = request.POST['resume']
        college_company_name = request.POST['college_company_name']
        year = request.POST['year']
        internship_details = request.POST['internship_details']
        
        #  Check if user has made inquiry already
        if RegistrationForm.objects.all().filter(roll_number=roll_number).exists():
            messages.error(request, 'You have already Registered ')
            return redirect('/accounts/register')

        if RegistrationForm.objects.all().filter(email=email).exists():
            messages.error(request, 'This email address has already been used to register and cannot be registered again')
            return redirect('/accounts/register')

        registrationForm = RegistrationForm(student_name=student_name, course=course, email=email, phone=phone, roll_number=roll_number,linkedin_url=linkedin_url, github_url=github_url, portfolio_url=portfolio_url, date_of_birth=date_of_birth, resume=resume, college_company_name=college_company_name, year=year, internship_details=internship_details)

        registrationForm.save()

        # Send Mail 
        send_mail(
            'Registration Celect',
            'Thank You! \n Your submission is received and we will contact you soon.',
            '******@gmail.com',
            [email],
            fail_silently=False
        )

        messages.success(request, 'You have registered successfully')
        # return redirect('/accounts/register')
        return render(request, "accounts/register.html")

    else:
        return render(request, "accounts/register.html")





