"""
URL configuration for lms_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# STEP 5 — URLS (YOUR CONTROL)
from django.urls import path
from . import views

urlpatterns = [
    path("", views.role_select, name="role"),
    path("login/", views.login_view, name="login"),
    path("admin/", views.admin_dashboard, name="admin"),
    path("faculty/", views.faculty_dashboard, name="faculty"),
    path("student/", views.student_dashboard, name="student"),
    path("logout/", views.logout_view, name="logout"),
]   