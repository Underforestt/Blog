from django.shortcuts import render
from .models import Post
# Create your views here.
def showblog(request):
    posts = Post.objects
    return render(request, 'blogApp/blog.html', {'posts': posts})



