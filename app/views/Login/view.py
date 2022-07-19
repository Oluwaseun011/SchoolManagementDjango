from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from app.models import Person

from app.service_provider import app_service_provider


def login_get(request):
    context = {
        'next': request.GET.get("next", 'profile')
    }
    return render(request, 'login.html', context)


def login_post(request):
    context = {

    }
    resolve_url = request.GET.get("next")
    email = request.POST.get('email')
    password = request.POST.get('password')
    person: Person = authenticate(request, email=email, password=password)
    if person is not None:
        login(request, person)
        groups = serialize('json', request.user.groups.all())
    else:
        context['message'] = 'username or password incorrect'
        return render(request, 'login.html', context)


def log_out(request):
    logout(request)
    return redirect("index")
