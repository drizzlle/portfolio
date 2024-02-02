from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date_of_birth = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/')
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    about_me = RichTextField(default='say something about your self here')
    #what I am doing goes here
    service_title=models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.first_name

class Service(models.Model):
    title = models.CharField(max_length=255)
    icon_url = models.FileField(upload_to='photos/%Y/%m/')
    description = RichTextField(default='say something about your self here')
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Experience(models.Model):
    organisation_name = models.CharField(max_length=255)
    timeline = models.CharField(max_length=255)
    postion = models.CharField(max_length=255)
    summary = RichTextField(default='say something about your education')
    def __str__(self):
        return self.organisation_name

class Education(models.Model):
    school_name = models.CharField(max_length=255)
    timeline = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    summary = RichTextField(default='say something about your education')
    def __str__(self):
        return self.school_name

class Testimonial(models.Model):
    testimonial_title = models.CharField(max_length=255)
    testimonial_avi = models.FileField(upload_to='photos/%Y/%m/')
    testimonials_text = RichTextField(default='say something about your self here')
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.testimonial_title

class Client(models.Model):
    client_title = models.CharField(max_length=255)
    client_logo = models.ImageField(upload_to='photos/%Y/%m/')
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.client_title

class Skill(models.Model):
    skill_title = models.CharField(max_length=255)
    skill_summary = RichTextField(default='say something about your skill')
    def __str__(self):
        return self.skill_title

class Project(models.Model):

    category_choice =  (
        ('Web development','Web development'),
        ('App development', 'App development'),
        ('Wordpress', 'Wordpress'),
        ('Office 365 setup', 'Office 365 setup'),
    )

    project_title = models.CharField(max_length=255)
    category = models.CharField( choices = category_choice, max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/')
    summary = models.CharField(max_length=255)

    def __str__(self):
        return self.project_title

class Post(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now)
    pub_photo = models.ImageField(upload_to='photos/%Y/%m/')
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.title
