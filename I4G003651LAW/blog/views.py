import imp
from django.shortcuts import render

# Create your views here.
from .models import Post
from .models import reverse_lazy
def PostListView(request):
    model = Post

def PostCreateView():
    model = Post

    fields = "__all__"
    
    success_url  = reverse_lazy("blog:all")

def PostDetailView():
    model = Post

def PostUpdateView():
    model = Post

    fields = "__all__"

    success_url  = reverse_lazy("blog:all")

def PostDeleteView():
    model = Post

    fields = "__all__"

    success_url  = reverse_lazy("blog:all")