from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

class UserProfile(AbstractUser):  # Extending Django's built-in User model
    USER_TYPES = [
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='student')

    def __str__(self):
        return self.username

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    instructor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    material = models.FileField(upload_to='course_materials/', blank=True, null=True)  # File Upload

    def clean(self):
        """Ensure only teachers can create courses."""
        if self.instructor.user_type != 'teacher':
            raise ValidationError("Only teachers can create courses.")

    def __str__(self):
        return self.title

