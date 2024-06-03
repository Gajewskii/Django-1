# views.py
from django.shortcuts import render, redirect,get_object_or_404
from .forms import PostForm,CommentForm
from .models import Post,Comment

def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  
        else:
            print(form.errors)  # Print form errors to the console for debugging
    else:
        form = PostForm()
    
    posts = Post.objects.all()  
    return render(request, 'www/index.html', {'form': form, 'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    added_comment_list = post.comment_set.all()  # Retrieve comments associated with this post

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  # Assign the comment to the current post
            comment.save()
            # Redirect to the same post detail page after form submission
            return redirect('post_detail', post_id=post_id)  
    else:
        form = CommentForm()

    # Re-fetch the comment list after adding a new comment
    added_comment_list = post.comment_set.all()

    return render(request, 'www/post_detail.html', {'form': form, 'post': post, 'added_comment_list': added_comment_list})