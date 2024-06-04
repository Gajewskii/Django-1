# views.py
from django.shortcuts import render, redirect,get_object_or_404
from .forms import PostForm,CommentForm
from .models import Post,Comment,Like
from django.db.models import F
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
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()

    added_comment_list = post.comment_set.all()
    
    return render(request, 'www/post_detail.html', {'form': form, 'post': post, 'added_comment_list': added_comment_list})


def like_comment(request, comment_id):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, id=comment_id)
        existing_like = Like.objects.filter(comment=comment).first()
        if existing_like:
            existing_like.delete()
       
             # Remove the like if already exists
        else:
            Like.objects.create(comment=comment) 
        return redirect('post_detail', post_id=comment.post.id)