from django.shortcuts import render , redirect
from django.contrib.auth import login, get_user_model ,authenticate
from .forms import LoginForms


def login_forms(request):
    loginform = LoginForms(request.POST or None)

    if loginform.is_valid():
        username = loginform.cleaned_data.get('username')
        password = loginform.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            login(request, user)
            return redirect('/')

    context = {
        'form': loginform
    }
    return render(request, 'login.html', context)


