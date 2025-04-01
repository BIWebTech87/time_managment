from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    context = {
        'user': request.user.get_full_name,
        'title': 'Home Page',
        'is_superuser': request.user.is_superuser,
    }
    return render(request, 'index.html', context)


