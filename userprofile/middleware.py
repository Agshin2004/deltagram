from django.utils.timezone import now
from .models import Profile

class UpdateLastSeenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response  # next middleware or view
        
    def __call__(self, request):
        ''' This method is called on each request; /
        
        takes request and must return response object, usually by calling get_response(request) to pass the request to the next middleware or view '''
        
        if request.user.is_authenticated:
            Profile.objects.filter(user=request.user).update(last_seen=now())
        response = self.get_response(request)  # Passing request back to the view
        return response
