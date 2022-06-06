from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy, reverse

# Create your views here.

def index(request):
    # if the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        #If the form is valid
        if form.is_valid():
            # Yes, save
            form.save()
            # Redirect to Home
            return HttpResponseRedirect('/')
        else:
            # No, Show error
            return HttpResponseRedirect(form.errors.as_json())

    # Get all post, limit = 20
    post = Post.objects.all().order_by('-created_at')[:20]
    
    # Show
    return render(request, 'post.html',
                            {'post' : post})

def delete(request, post_id):
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')

def LikeView(request, post_id):
    post=Post.objects.get(id=post_id)
    post.likes = post.likes+1
    post.save()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        return render(request, 'edit.html', {'post': post })
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

