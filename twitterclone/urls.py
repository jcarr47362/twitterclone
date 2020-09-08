"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitteruser import views as twitteruser_index_view
from tweet import views as tweet_view
from authentication import views as auth_view
from notification import views as notification_view

urlpatterns = [
    path('', twitteruser_index_view.IndexView.as_view(), name='homepage'),
    path('login/', auth_view.login_view, name="login_view"),
    path('signup/', twitteruser_index_view.SignUpView.as_view(), name="signup_view"),
    path('addtweet/', tweet_view.AddTweetView.as_view(), name="tweet_view"),
    #path('following/<int:follow_id>/', auth_view. ),
    #path('unfollowing/<int:unfollow_id>')
    path('logout/', auth_view.logout_view, name="logout_view"),
    path('admin/', admin.site.urls),
]
