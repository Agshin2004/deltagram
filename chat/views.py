from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from authentication.models import User
from chat.forms import MessageForm

from .models import Message, Room


@login_required(login_url='/authentication/login/')
def chat(request):
    '''This view will list all chats that user has'''
    # Getting Rooms
    rooms = Room.objects.filter(participants=request.user)
    users = User.objects.filter(username=request.user.username)
        
    # Getting interlocutors
    interlocutors = {}
    for room in rooms:
        interlocutors[room.id] = room.participants.exclude(id=request.user.id)
    
    # Getting all users user can start chat with
    #rooms_with_current_user = Room.objects.filter()  # Get all rooms
    #user_ids_in_rooms = rooms_with_current_user.values_list('participants__id', flat=True)  # get ids of users who are already in rooms with current user as QuerySet
    
   # users_without_conversation = User.objects.exclude(id__in=user_ids_in_rooms).exclude(id=request.user.id)  #exclude users that have room with current user and then exclude current user too

    ctx = {'rooms': rooms, 'interlocutors': interlocutors, 'users': users}
    return render(request, 'chat/all_chats.html', context=ctx)


def chat_detail(request, chat_uuid):
    room = Room.objects.get(id=chat_uuid)
    if request.user not in room.participants.all():
        return HttpResponse('Access Denied', status=403)
    
    messages = Message.objects.filter(room=room).order_by('-date_sent')
    form = MessageForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)    
        obj.sender = request.user
        obj.receiver = room.participants.exclude(id=request.user.id).first()  # Getting receiver by excluding the current user
        obj.room = room
        obj.save()
        return redirect('chat_detail', chat_uuid=chat_uuid)
        
    ctx = {'messages': messages, 'form': form}
    return render(request, 'chat/chat_detail.html', context=ctx)



def start_chat(request):
    # Check if user submitted the form
    if request.POST:
        current_user_id = request.user.id
        start_chat_with_id = request.POST.get('user')
        print(start_chat_with_id)
        participant_ids = [current_user_id, start_chat_with_id]
        slug = '-'.join(str(id) for id in participant_ids)  # Getting slug 
        room, created = Room.objects.get_or_create(slug=slug)
        
        if created:
            room.participants.add(
                User.objects.get(id=current_user_id),
                User.objects.get(id=start_chat_with_id),
            )
            
            return redirect('chat_detail', chat_uuid=room.id)
        else:
            return redirect('chat_detail', chat_uuid=room.id)
            
