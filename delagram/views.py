from django.shortcuts import render

from authentication.models import User

def home(request):
    users = User.objects.all().exclude(username=request.user.username)
    ctx = {'users': users}
    return render(request, 'home.html', context=ctx)
