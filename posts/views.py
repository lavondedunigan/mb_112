from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from .models import Post


class PastListView(ListView):
    template_name = "posts/list.html"
    model = Post
    
class PostDetailView(DetailView):
    template_name = "posts/detait.html"
    model = Post
    
class PastCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post 
    fields = ["title", "subtitle", "body"]   

