from django.urls import include, path

urlpatterns = [
    path("enter/", include("movies.urls")),
]
