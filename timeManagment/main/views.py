from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    context = {
        'title': 'Home Page'  # This will be passed to the template as 'title' variable.
    }
    if not request.user.is_authenticated:
        return HttpResponse('You are not logged in.')
    return render(request, 'index.html', context)


