from django.contrib import admin
from .models import UserProfile, Course

# Register models so they appear in the Django admin panel
admin.site.register(UserProfile)
admin.site.register(Course)
