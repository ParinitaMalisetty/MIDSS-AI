from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from complaints.utils import complaint_image_path


class Complaint(models.Model):

    class Category(models.TextChoices):
        POTHOLE = "Pothole", "Pothole"
        ROAD_CRACK = "Road Crack", "Road Crack"
        GARBAGE = "Garbage", "Garbage"
        DRAINAGE = "Drainage", "Drainage"
        WATERLOGGING = "Waterlogging", "Waterlogging"
        STREETLIGHT = "Streetlight", "Streetlight"

    class Status(models.TextChoices):
        SUBMITTED = "Submitted", "Submitted"
        UNDER_REVIEW = "Under Review", "Under Review"
        IN_PROGRESS = "In Progress", "In Progress"
        RESOLVED = "Resolved", "Resolved"

    class Priority(models.TextChoices):
        LOW = "Low", "Low"
        MEDIUM = "Medium", "Medium"
        HIGH = "High", "High"
        CRITICAL = "Critical", "Critical"

    user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE
)

    title = models.CharField(max_length=150)

    description = models.TextField()

    category = models.CharField(
        max_length=30,
        choices=Category.choices
    )

    from .utils import complaint_image_path

    image = models.ImageField(
    upload_to=complaint_image_path
    )

    latitude = models.FloatField()

    longitude = models.FloatField()
    
    priority = models.CharField(
        max_length=20,
        choices=Priority.choices,
        default=Priority.LOW
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.SUBMITTED
    )
    ai_prediction = models.CharField(
    max_length=100,
    blank=True,
    default=""
    )

    confidence = models.FloatField(
        default=0
    )

    severity = models.CharField(
    max_length=20,
    blank=True,
    default=""
    )

    decision_support = models.TextField(
    blank=True,
    default=""
)
    assigned_engineer = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="assigned_complaints",
    limit_choices_to={"role": "ENGINEER"},
)

    ai_processed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.category} - {self.title}"
    