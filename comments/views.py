
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .form import PostForm


def feed(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'feed.html', {'posts': posts})


def create_post(request):
    form = PostForm()

    if request.method == 'GET':
        context = {
            'form': form
        }
        return render(request, 'comments.html', context)

    elif request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')


def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Comment.objects.create(
                post=post,
                text=text
            )
    return redirect('feed')
