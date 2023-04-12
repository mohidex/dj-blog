from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("coreapp.urls")),
    path("authors/", include("authorapp.urls")),
    path("blogs/", include("blogapp.urls")),
]
