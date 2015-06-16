from django.shortcuts import render
from django.utils.timezone import now
import datetime


def home(request):
    today = datetime.date.today()
    print(request.COOKIES.get('django_language', '0'))
    return render(
        request, 'taskbuster/index.html', {'today': today, 'now': now()}
    )


def home_files(request, filename):
    return render(request, filename, {}, content_type='text/plain')
