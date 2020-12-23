from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model
from .forms import LoginForms


def login_forms(request):
    loginform = LoginForms(request.POST or None)
    if loginform.is_valid():
        username = loginform.cleaned_data.get("username")
        password = loginform.cleaned_data.get("password")
        print(username , password)
    context = {
        'form': loginform
    }
    return render(request, 'login.html', context)


