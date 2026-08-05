from django.urls import path

from . import views

urlpatterns = [

    path(
        "register/",
        views.register,
        name="register"
    ),

    path(
        "login/",
        views.CustomLoginView.as_view(),
        name="login"
    ),

    path(
        "logout/",
        views.CustomLogoutView.as_view(),
        name="logout"
    ),

    path(
        "citizen/",
        views.citizen_dashboard,
        name="citizen_dashboard"
    ),

    path(
        "engineer/",
        views.engineer_dashboard,
        name="engineer_dashboard"
    ),

    path(
        "admin-dashboard/",
        views.admin_dashboard,
        name="admin_dashboard"
    ),
    path(
    "engineer/",
    views.engineer_dashboard,
    name="engineer_dashboard",
),
]