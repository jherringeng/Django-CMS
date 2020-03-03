from django import forms

class TweetForm(forms.Form):
    tweet = forms.CharField(widget=forms.Textarea(attrs={ 'max-width':'80%', 'rows':'3', 'placeholder': 'Tell us about some tasty birds...' }))
    # , 'cols' : "70",
    # tweet = forms.CharField(label='Your name', max_length=180)
