from django.shortcuts import render
import tweepy, csv, sys, re
from website import twitterAPI
from django.contrib.auth.decorators import login_required
import os



# This is supposed to make the homescreen blank before submitting any word to the search box
@login_required
def home(request):

    if request.GET:
            hashtag = request.GET['q']

            # Sentiments = [positive, negative, neutral, objective, subjective, count]
            # Allteets = [location, username , created, text]
            [sentiments, coordinates] = twitterAPI.twitter_streamer(hashtag, 200)

            show_content = True
            context = {'sentiments': sentiments,
                       'show_content': show_content,
                       'coordinates': coordinates,
                       'locations_available': len(coordinates),
                       'API_KEY': os.environ.get('API_KEY'),
                       }

            # Takes the html file from templates folder which is inside the website project folder
            return render(request, 'website/home.html', context)
    else:
        # Doesn't show to graphs because there isn't any available data
        show_content = False
        context = {'show_content': show_content}
        return render(request, 'website/home.html', context)

def about(request):
    return render(request, 'website/about.html')


# When submitting a word to the search box this function should
# return the word back to home.html as a 'context'

