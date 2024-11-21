from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def all_blogs(request):
    #para mostrar por orden de creacion 
    blogs= Blog.objects.order_by('-date')
    # para mostrar el ultimo
    # blogs= Blog.objects.order_by('-date')[:1]
    return render(request,'blog/all_blogs.html',{'blogs':blogs})

def detail(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':blog})