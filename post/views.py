from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages



from post.forms import PostForm
from post.models import Post



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
    ctx = {'post': post}
    return render(request, 'post/post_detail.html', context=ctx)
    
    
    
def like_or_dislike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    print(post.like)
    if request.user in post.like.all():
        post.like.remove(request.user)
        return JsonResponse({'Success': 'Disliked'})
    else:
        post.like.add(request.user)
        return JsonResponse({'success': 'Liked'})
