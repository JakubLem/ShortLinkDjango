from django.urls import re_path as url, include


urlpatterns = [
    url("api/", include("api.urls")),
]
