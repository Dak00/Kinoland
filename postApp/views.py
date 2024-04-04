from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import AddPostForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

def homePage(request):
    posts = Post.objects.all().order_by('-postDate')[:9]
    return render(request, "site/home.html", {
        'posts': posts
    })

def allPost(request):
    posts = Post.objects.all().order_by('-postDate')
    return render(request, "site/all-news.html", {
        'posts': posts
    })

def postDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "user/post-detail.html", {
        'post': post
    })

def addPost(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homePage")
    else:
        form = AddPostForm()
    return render(request, "user/add-post.html", {
        'form': form
    })

def deletePost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("allPost")
    return render(request, "user/delete-post.html", {
        'post': post
    })

def editPost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = AddPostForm(request.POST or None, instance=post)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("postDetail", pk=post.pk)
    else:
        form = AddPostForm()
    return render(request, "user/edit-post.html", {
        'post': post,
        'form': form
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homePage')
    else:
        form = UserCreationForm()
    return render(request, 'sign-up.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homePage')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
