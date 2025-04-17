from django.conf import settings  
from django.conf.urls.static import static
from django.urls import path
from . import views  # Import your views here


urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("student-dashboard/", views.student_dashboard, name="student_dashboard"),
    path("teacher-dashboard/", views.teacher_dashboard, name="teacher_dashboard"),
    path("courses/", views.courses, name="courses"),
    path("forgot-password/", views.forgot_password, name="forgot_password"),
    path("verify/", views.verify_account, name="verify_account"),
    path("dashboard/", views.main_dashboard, name="dashboard"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
