from django.contrib import admin
from .models import Certificate, Profile, Service, Testimonial, Client, Education, Experience, Skill, Project

# Register your models here.
admin.site.register(Profile)
admin.site.register(Service)
admin.site.register(Testimonial)
admin.site.register(Client)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Certificate)
