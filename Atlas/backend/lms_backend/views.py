# STEP 1 — YOUR OWN BASE
from django.shortcuts import render, redirect

def role_select(request):
    if request.method == "POST":
        role = request.POST.get("role")
        request.session["role"] = role
        return redirect("login")
    return render(request, "index.html")

# STEP 2 — LOGIN LOGIC (YOUR CORE PART)
def login_view(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        password = request.POST.get("password")
        role = request.session.get("role")

        # dummy check (for demo)
        if user_id == "test" and password == "123":
            if role == "admin":
                return redirect("admin")
            elif role == "faculty":
                return redirect("faculty")
            elif role == "student":
                return redirect("student")
        return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")

# STEP 3 — DASHBOARDS (SIMPLE)
def admin_dashboard(request):
    return render(request, "admin.html")

def faculty_dashboard(request):
    return render(request, "faculty.html")

def student_dashboard(request):
    return render(request, "student.html")

# STEP 4 — LOGOUT (YOUR WORK)
def logout_view(request):
    request.session.flush()
    return redirect("role")


