from django.shortcuts import render
import tweepy, csv, sys, re
from website import twitterAPI
from website import  GoogleAPI
from django.contrib.auth.decorators import login_required
from website import credentials



# This is supposed to make the homescreen blank before submitting any word to the search box
@login_required
def home(request):

    if request.GET:
            hashtag = request.GET['q']

            # Sentiments = [0positive, 1negative, 2neutral, 3objective, 4subjective, 5i]
            # Allteets = [0-location, 1-username , 2-created, 3-text]
            [sentiments, coordinates] = twitterAPI.twitter_streamer(hashtag, 200)
            show_content = True
            context = {'sentiments': sentiments,
                       'show_content': show_content,
                       'coordinates': coordinates,
                       'locations_available': len(coordinates),
                       'API_KEY': credentials.API_KEY,
                       }

            # Takes the html file from templates folder which is inside the website project folder
            return render(request, 'website/home.html', context)
    else:
        show_content = False
        context = {'show_content': show_content}
        return render(request, 'website/home.html', context)

def about(request):
    return render(request, 'website/about.html')


# When submitting a word to the search box this function should
# return the word back to home.html as a 'context'

