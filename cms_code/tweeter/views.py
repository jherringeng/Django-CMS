from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string

from django.conf import settings
from .models import Tweet, Profile
from .forms import TweetForm
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url='/accounts/login/')
def index(request):

    username = request.user.username
    try:
        user_profile = Profile.objects.get(user=username)
        print(user_profile)
        print(user_profile.profile_text)
    except Profile.DoesNotExist:
        profile = Profile(user=username, profile_text="Enter some text about you...")
        profile.save()

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TweetForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            subject = form.cleaned_data['tweet']
            username = request.user.username
            now = datetime.now()

            p = Tweet(user=username, tweet_text=subject, pub_date=now)
            p.save()

            latest_tweets = Tweet.objects.order_by('-pub_date')
            tweet_form = TweetForm()

            users =User.objects.values()
            # print(users)

            context = {
                'user_profile': user_profile,
                'tweet_form': tweet_form,
                'tweets': latest_tweets,

                'users': users,
            }

            return render(request, 'tweeter/tweeter.html', context)

    else:
        latest_tweets = Tweet.objects.order_by('-pub_date')
        tweet_form = TweetForm()

        users =User.objects.values()
        print(users)

        context = {
            'user_profile': user_profile,
            'tweet_form': tweet_form,
            'tweets': latest_tweets,

            'users': users,
        }

    return render(request, 'tweeter/tweeter.html', context)

@login_required(login_url='/accounts/login/')
def profile(request):
    user_name = request.user.username
    user_profile = Profile.objects.get(user=user_name)

    context = {

        'user_profile': user_profile,

    }

    return render(request, 'tweeter/profile.html', context)

@login_required(login_url='/accounts/login/')
def user_profile(request, user_name):
    user_name = str(user_name)
    print(user_name)
    print('some text')
    # user_profile = Profile.objects.get(user=user_name)

    context = {

        # 'user_profile': user_profile,

    }

    return render(request, 'tweeter/profile.html', context)

@login_required(login_url='/accounts/login/')
def base(request):

    context = {}

    return render(request, 'tweeter/base.html', context)
