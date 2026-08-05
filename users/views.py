from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import CitizenRegistrationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from complaints.models import Complaint

@login_required
def citizen_dashboard(request):
    return render(
        request,
        "dashboard/citizen_dashboard.html"
    )
    
def register(request):

    if request.method == "POST":

        form = CitizenRegistrationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect("citizen_dashboard")

        else:
            print(form.errors)

    else:

        form = CitizenRegistrationForm()

    return render(
        request,
        "users/register.html",
        {
            "form": form
        }
    )
    
    
from complaints.models import Complaint

@login_required
def engineer_dashboard(request):

    if request.user.role != request.user.Role.ENGINEER:
        return redirect("citizen_dashboard")

    if request.method == "POST":

        complaint = Complaint.objects.get(
            id=request.POST["complaint_id"]
        )

        complaint.status = request.POST["status"]
        complaint.save()

        return redirect("engineer_dashboard")

    complaints = Complaint.objects.all().order_by("-created_at")

    return render(
        request,
        "dashboard/engineer_dashboard.html",
        {
            "complaints": complaints,
            "statuses": Complaint.Status.choices,
        },
    )
    
class CustomLoginView(LoginView):
    template_name = "users/login.html"

    def get_success_url(self):

        user = self.request.user

        if user.role == user.Role.CITIZEN:
            return reverse_lazy("citizen_dashboard")

        elif user.role == user.Role.ENGINEER:
            return reverse_lazy("engineer_dashboard")

        elif user.role == user.Role.ADMIN:
            return reverse_lazy("admin_dashboard")

        return reverse_lazy("register")
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("home")


from users.models import User

@login_required
def admin_dashboard(request):

    if request.user.role != request.user.Role.ADMIN:
        return redirect("citizen_dashboard")

    complaints = Complaint.objects.all().order_by("-created_at")

    context = {
        "complaints": complaints,

        "total": complaints.count(),
        "submitted": complaints.filter(status="SUBMITTED").count(),
        "review": complaints.filter(status="UNDER_REVIEW").count(),
        "resolved": complaints.filter(status="RESOLVED").count(),

        "citizens": User.objects.filter(role=User.Role.CITIZEN).count(),
        "engineers": User.objects.filter(role=User.Role.ENGINEER).count(),
    }

    return render(
        request,
        "dashboard/admin_dashboard.html",
        context,
    )