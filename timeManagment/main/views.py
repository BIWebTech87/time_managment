from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    context = {
        'user': request.user.get_full_name,
        'title': 'Home Page',
    }
    print(request.user.get_full_name, request.method)  # This will print the logged-in user's username if authenticated'
    return render(request, 'index.html', context)


