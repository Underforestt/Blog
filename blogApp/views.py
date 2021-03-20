from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.


def showblog(request):
    posts = Post.objects
    return render(request, 'blogApp/blog.html', {'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blogApp/post_full.html', {'post': post})