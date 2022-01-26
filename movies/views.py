from django.shortcuts import render
from django.views import generic

from .models import Movie


# Create your views here.
class IndexView(generic.ListView):
    template_name = "movies/index.html"
    context_object_name = "latest_movie_list"

    def get_queryset(self):
        return Movie.objects.order_by("-year")[:50]


class DetailView(generic.DetailView):
    model = Movie
    template_name = "movies/detail.html"


