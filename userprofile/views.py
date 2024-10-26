from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from authentication.models import User
from post.models import Post

from .models import Profile
from .forms import ProfileForm, UserForm


def user_profile(request, username):
    user_profile = get_object_or_404(Profile, user__username=username)
    posts = Post.objects.filter(user=user_profile.user).order_by('-date_created')
    profiles_following_current_user = Profile.objects.filter(followers=user_profile.user)

    if user_profile.user == request.user:
        if request.method == 'POST':
            user_form = UserForm(request.POST, instance=user_profile.user)
            profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, 'Profile has been updated successfully')
                return redirect('user_profile', username=user_profile.user.username)
            else:
                ctx = {'user_profile': user_profile, 'profile_form': profile_form, 'user_form': user_form}
                return render(request, 'userprofile/user_profile.html', context=ctx)

        user_form = UserForm(instance=user_profile.user)
        profile_form = ProfileForm(instance=user_profile)

        ctx = {'user_profile': user_profile, 'profile_form': profile_form, 'user_form': user_form, 'posts': posts, 'profiles_following_current_user': profiles_following_current_user}
        return render(request, 'userprofile/user_profile.html', context=ctx)

    else:
        # Not current user's profile
        posts = Post.objects.filter(user=user_profile.user).order_by('-date_created')
        ctx = {'user_profile': user_profile, 'posts': posts, 'profiles_following_current_user': profiles_following_current_user}
        return render(request, 'userprofile/user_profile.html', context=ctx)


@login_required(login_url='/authentication/login/')
def follow(request, user_id):
    # Getting User that we wanna follow
    following = User.objects.get(id=user_id)
    user = Profile.objects.get(user=request.user)
    
    following.profile.followers.add(user.user)
    user.following.add(following)
    
    return JsonResponse({'success': 'Followed'})


@login_required(login_url='/authentication/login/')
def unfollow(request, user_id):
    if request.user.is_authenticated:
        # Getting User that we wanna unfollow
        follower = User.objects.get(id=user_id)
        # Getting current user (us)
        user = Profile.objects.get(user=request.user)
        
        # Removing current user (us) from m2m followers field of follower
        follower.profile.followers.remove(user.user)
        # Removing follower from m2m following field (of current_user)
        user.following.remove(follower)
        
        return JsonResponse({'success': 'Unfollowed'})

