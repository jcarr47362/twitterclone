from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from twitteruser.models import TwitterUser
from authentication.forms import AddLoginForm
from django.contrib.auth.decorators import login_required



def login_view(request):
    if request.method == "POST":
        form = AddLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get('username'), password=data.get('password'))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))

    form = AddLoginForm()
    return render(request, 'generic_form.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))

