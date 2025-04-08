"""
URL configuration for octofit_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("octofit_tracker_app.urls")),
]

# Add api_root
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        "users": reverse("user-list", request=request, format=format),
        "teams": reverse("team-list", request=request, format=format),
        "activity": reverse("activity-list", request=request, format=format),
        "leaderboard": reverse("leaderboard-list", request=request, format=format),
        "workouts": reverse("workout-list", request=request, format=format),
    })
