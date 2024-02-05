from django.shortcuts import render, get_object_or_404, redirect
from .models import Certificate, Profile, Service, Testimonial, Client, Education, Experience, Skill, Project
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages


def home(request):
    profiles = Profile.objects.all()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    clients = Client.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    #Query the blog posts
    certificates = Certificate.objects.all()
    #Contact
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        message = request.POST['message']

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        email_subject = 'You have a new message from Portfolio'
        message_body = 'Name:' + full_name + '. Email:' + email + '. Message:' + message
        send_mail(
                email_subject,
                message_body,
                'info@aliyu.com.ng',
                [admin_email],
                fail_silently=False,
            )
        messages.success(request, 'Thank you for contacting me, I will get back to you shortly')
        return redirect ('home')
    data = {
        'profiles': profiles,
        'services': services,
        'testimonials': testimonials,
        'clients': clients,
        'educations': educations,
        'experiences': experiences,
        'skills': skills,
        'projects': projects,
        'certificates': certificates,  # Include the blog posts in the data dictionary
    }
    return render(request, "pages/home.html", data)
    
