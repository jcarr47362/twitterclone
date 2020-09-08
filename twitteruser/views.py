from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from twitteruser.forms import AddSignupForm
from tweet.models import Tweet

@login_required
def index_view(request):
    my_tweets = Tweet.objects.all()
    return render(request, "index.html", {"my_tweets": my_tweets})

def signup_view(request):
    if request.method == "POST":
        form = AddSignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = TwitterUser.objects.create_user(
                username=data.get("username"),
                password=data.get("password"),
            )
            if new_user:
                login(request, new_user)
                return HttpResponseRedirect(reverse("homepage"))

    form = AddSignupForm()
    return render(request, "generic_form.html", {"form": form})

#def author_detail(request, author_id):
   # author = TwitterUser.objects.filter(id=author_id).first()
   # return render(request, "author_detail.html", {"author_detail": author_detail})






