from django.shortcuts import render

from authentication.models import User
from post.models import Post

def home(request):
    if request.user.is_authenticated:
        users = User.objects.all().exclude(username=request.user.username)
        posts = Post.objects.all().exclude(user=request.user)
    else:
        users = User.objects.all().exclude()
        posts = Post.objects.all().exclude()

    ctx = {'users': users, 'posts': posts}
    return render(request, 'home.html', context=ctx)
