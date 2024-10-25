from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages



from post.forms import CommentForm, PostForm
from post.models import Post, Comment



def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()

            messages.success(request, 'Post has been added!')
            return redirect('user_profile', username=request.user.username)
        else:
            messages.success(request, 'Fix errors below!')
            return render(request, 'post/add_post.html', context=ctx)

    
    form = PostForm()
    ctx = {'form': form}
    return render(request, 'post/add_post.html', context=ctx)

def remove_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    messages.success(request, 'Post was deleted')
    return redirect('home')
    

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post).order_by('-date_created')
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            obj = comment_form.save(commit=False)
            obj.post = post
            obj.user = request.user
            obj.save()
            
            messages.success(request, 'Comment was added successfully')
            return redirect('post_detail', post_id=post_id)
        else:
            print(comment_form.errors)  
    else:
        ctx = {'post': post, 'comment_form': comment_form, 'comments': comments}
        return render(request, 'post/post_detail.html', context=ctx)
    
    
    
def like_or_dislike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    print(post.like)
    if request.user in post.like.all():
        post.like.remove(request.user)
        return JsonResponse({'success': 'Disliked'})
    else:
        post.like.add(request.user)
        return JsonResponse({'success': 'Liked'})
