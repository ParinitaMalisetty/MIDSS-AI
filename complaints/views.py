from django.shortcuts import render, redirect

from .models import Complaint
from .forms import ComplaintForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


User = get_user_model()
def home(request):

    total = Complaint.objects.count()

    pending = Complaint.objects.filter(status="Submitted").count()

    resolved = Complaint.objects.filter(status="Resolved").count()

    high = Complaint.objects.filter(priority="High").count()

    return render(
        request,
        "home.html",
        {
            "total": total,
            "pending": pending,
            "resolved": resolved,
            "high": high,
        },
    )

def submit_complaint(request):

    if request.method == "POST":

        form = ComplaintForm(request.POST, request.FILES)

        if form.is_valid():

            complaint = form.save(commit=False)

            complaint.user = request.user

            complaint.save()

            return redirect("/my/")

    else:

        form = ComplaintForm()

    return render(
        request,
        "complaints/submit.html",
        {
            "form": form
        }
    )


def my_complaints(request):

    complaints = Complaint.objects.all().order_by("-created_at")

    return render(
        request,
        "complaints/my_complaints.html",
        {
            "complaints": complaints
        }
    )
def complaint_detail(request, complaint_id):

    complaint = get_object_or_404(
        Complaint,
        id=complaint_id
    )

    return render(
        request,
        "complaints/detail.html",
        {
            "complaint": complaint
        }
    )