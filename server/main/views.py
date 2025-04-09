from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from django.conf import settings

navbar_links = [
    {'name': _('Home'), 'url': 'index'},
    {'name': _('Employees'), 'sub1': _('All'), 'sub2': _('New')},
    {'name': _('Projects'), 'sub1': _('All'), 'sub2': _('New')},
    {'name': _('Tasks'), 'sub1': _('All'), 'sub2': _('New')},
]

LANGUAGES = settings.LANGUAGES


@login_required
def index(request):
    context = {
        'title': 'Home Page',
        'LANGUAGES': LANGUAGES,
    }
    return render(request, 'index.html', context)


