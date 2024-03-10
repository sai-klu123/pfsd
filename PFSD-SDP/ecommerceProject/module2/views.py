from django.core.mail import send_mail
from django.http import HttpResponse, request
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
def mainpagecall(request):
    product_range = range(1, 11)
    return render(request,'mainPage.html', {'product_range': product_range})

# def signupcall(request):
#     return render(request,'signup1.html')
def navbar2call(request):
    return render(request,'navBar2.html')
def navbarcall(request):
    return render(request,'signup1.html')
from .models import *
from django.shortcuts import render,redirect
from django.shortcuts import render, redirect
def signupcall(request):
    return render(request,'signup1.html')


from django.core.mail import send_mail

from django.core.mail import send_mail
from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponse
def send_welcome_email(user_email,user_name):
    subject = 'Welcome to TrendyCart!'  # Set your subject here
    message_body = (
        f'Hey {user_name},\n\n'
        f'Welcome to TrendyCart! We are thrilled to have you on board.\n\n'
        f'Feel free to explore our website and discover amazing features.\n\n'
        f'If you have any questions or need assistance, don\'t hesitate to contact us.\n\n'
        f'Enjoy your time on TrendyCart!\n\n'
        f'Best regards,\n'
        f'TrendyCart Team'
    )  # Extend your email content here

    send_mail(
        subject,
        message_body,
        '2200033073cseh@gmail.com',
        [user_email],
        fail_silently=False,
    )


from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def registerloginfunction(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        password = request.POST.get('password')

        try:
            validate_email(email)
        except ValidationError:
            return HttpResponse("Invalid email address. Please enter a valid email.")
        if Register_user.objects.filter(email=email).exists():
            return HttpResponse("Email already registered. Please enter a different email.")
        new_user = Register_user.objects.create(name=name, email=email, phonenumber=phonenumber, password=password)
        send_welcome_email(new_user.email, new_user.name)
        return redirect('logincall')

    return render(request, 'signup1.html')


# authentication/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
def logincall(request):
    return render(request,'loginPage.html')



# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Register_user

from django.shortcuts import render
from django.http import JsonResponse
from .models import Register_user

def authenticate_user(request):
    if request.method == 'POST':
        useremail = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Register_user.objects.get(email=useremail, password=password)
            if user.email == 'admin@gmail.com' and password == 'admin':
                return JsonResponse({'success': True, 'user_type': 'admin'})
            else:
                return JsonResponse({'success': True, 'user_type': 'user'})
        except Register_user.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Invalid credentials'})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})



def aboutcall(request):
    return render(request,'about.html')

def servicecall(request):
    return render(request,'services.html')
def teamcall(request):
    return render(request,'team.html')
def contactcall(request):
    return render(request,'contactUs.html')


from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import contact_fb

def feedbackformfunction(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phonenumber=request.POST.get('phonenumber')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create ContactUs object
        contact_fb.objects.create(name=name, email=email, phonenumber=phonenumber,subject=subject, message=message)

        # Email content
        email_content = f"Subject: Acknowledgement of Your Inquiry\n\nDear {name},\n\nThank you for reaching out to us through our 'Contact Us' form. We've received your message and here's the content:\n\n{message}\n\nRest assured, we'll get back to you soon with the information or assistance you need.\n\nBest regards,"

        # Sending email
        send_mail(
            'THANK YOU for contacting us',
            email_content,
            '2200033073cseh@gmail.com',
            [email],
            fail_silently=False,
        )

        return redirect('contactcall')

    return render(request, 'contactUs.html')


def admincall(request):
    return render(request,'adminPage.html')


def show_user(request):
    users = Register_user.objects.all()
    return render(request, 'View_user.html', {'users': users})

from django.http import HttpResponse
from .models import Register_user  # Import your Register_user model

from django.shortcuts import render, redirect, get_object_or_404
from .models import Register_user

def show_users(request):
    users = Register_user.objects.all()
    return render(request, 'remove_user.html', {'users': users})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Register_user

from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from .models import Register_user

def remove_user(request, pk):
    if request.method == 'POST':
        # Assuming email is unique, find user by email
        user = get_object_or_404(Register_user, email=pk)
        user_email = user.email  # Retrieve the email address of the user
        user_name = user.name  # Assuming you have a 'name' field in your user model
        user.delete()

        # Call the send_removed_user_email function to send the email
        send_removed_user_email(user_email, user_name)

        return redirect('show_users')
    else:
        # This is a GET request, you may want to handle it differently or just redirect
        return redirect('show_users')



from django.core.mail import send_mail

def send_removed_user_email(user_email, user_name):
    subject = 'Account Deactivation Notification'
    message_body = (
        f'Hello {user_name},\n\n'
        f'We regret to inform you that your account on our platform has been deactivated '
        f'due to unusual activity.\n\n'
        f'If you believe this deactivation is in error or have any questions, please '
        f'contact us " TrendyCart@gmail.com" immediately.\n\n'
        f'Thank you for your understanding.\n\n'
        f'Regards,\n'
        f'TrendyCartTeam'
    )

    send_mail(
        subject,
        message_body,
        '2200033073cseh@gmail.com',  # Change to your platform's email
        [user_email],
        fail_silently=False,
    )


def add_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        password = request.POST.get('password')
        if Register_user.objects.filter(email=email).exists():
            return HttpResponse("Email already registered. Please enter a different email.")
        data = Register_user(name=name,email=email,phonenumber=phonenumber,password=password)
        data.save()

        return redirect('show_user')
    else:
        return render(request, 'add_user.html')





