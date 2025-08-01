from django.shortcuts import render
from . models import Post
def post_List(request):
    posts=Post.objects.all()
    return render(request,"posts/posts_List.html",{'posts':posts})
# Create your views here.
def post_Detail(request,slug):
    post=Post.objects.get(slug=slug)
    return render(request,"posts/post_Detail.html",{'post':post})


def contact(request):
    return render(request,'posts/i.html')
