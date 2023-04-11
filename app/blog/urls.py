from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("coreapp.urls")),
    path("author/", include("authorapp.urls")),
    path("blog/", include("blogapp.urls")),
]
