from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

class User(AbstractUser):
    username= None
    email = models.EmailField(unique=True)

    ROLE_CHOICES= [
        ('Candidate', 'Candidate'),
        ('Recruiter', 'Recruiter'),
        ('Admin', 'Admin'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Candidate')
    is_verified = models.BooleanField(default=False)
    objects = UserManager() 

    USERNAME_FIELD = 'email'    # we want email as login not username 
    REQUIRED_FIELDS = []        # we don't want any other required fields for creating superuser
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidate_profile')
    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    portfolio = models.URLField(blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.email

class RecruiterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='recruiter_profile')
    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    linkedin = models.URLField(blank=True)
    designation = models.CharField(max_length=100, blank=True)  
    
    def __str__(self):
        return self.user.email