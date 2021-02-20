from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.


def home(req):
    posts = Post.objects.order_by('publish_date').reverse()
    return render(req,"posts/home.html", {"posts": posts})

def post_detail(req, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(req,"posts/post_detail.html", {"post_id": post_id,"post": post})