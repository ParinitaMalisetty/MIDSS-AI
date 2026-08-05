from django.contrib import admin
from .models import Complaint

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "category",
        "status",
        "priority",
        "user",
        "created_at",
    )

    list_filter = (
        "category",
        "status",
        "priority",
    )

    search_fields = (
        "title",
        "description",
    )