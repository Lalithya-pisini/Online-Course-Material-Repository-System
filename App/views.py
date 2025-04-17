from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile, Course
from .forms import SignupForm  # ✅ Ensure SignupForm is imported

def home(request):
    return render(request, "home.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")  # Redirect to home after login
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after signup
            return redirect("home")  # Redirect to home page after signup
    else:
        form = SignupForm()

    return render(request, "signup.html", {"form": form})

def admin_dashboard(request):
    return render(request, "admindash.html")

def student_dashboard(request):
    students = UserProfile.objects.filter(user_type="student")  # Get only students
    return render(request, "studentdash.html", {"students": students})

def teacher_dashboard(request):
    teachers = UserProfile.objects.filter(user_type="teacher")  # Get only teachers
    return render(request, "teachdash.html", {"teachers": teachers})

def courses(request):
    query = request.GET.get("q")  # Get search query from the URL
    if query:
        course_list = Course.objects.filter(title__icontains=query)  # Filter courses by search term
    else:
        course_list = Course.objects.all()  # Show all courses if no search

    return render(request, "course.html", {"courses": course_list})

def forgot_password(request):
    return render(request, "foregot.html")

def verify_account(request):
    return render(request, "verify.html")

def main_dashboard(request):  # The missing view
    return render(request, "dashboard.html")

def logout_view(request):
    logout(request)
    return redirect("home")  # Redirect to home page after logout
