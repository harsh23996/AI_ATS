from django.contrib import admin

# Register your models here.
from .models import User, CandidateProfile, RecruiterProfile

admin.site.register(User)
admin.site.register(CandidateProfile)
admin.site.register(RecruiterProfile)