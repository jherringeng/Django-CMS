from django.db import models

class Tweet(models.Model):
    #user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    user = models.CharField(max_length=200)
    tweet_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('auto_now_add=True')

class Profile(models.Model):
    user = models.CharField(max_length=200)
    profile_text = models.CharField(max_length=200)
    sex = models.CharField(max_length=20)
    breed = models.CharField(max_length=50)
