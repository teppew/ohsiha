from django.shortcuts import render
import tweepy, csv, sys, re
from website import twitterAPI
from website import  GoogleAPI


# This is supposed to make the homescreen blank before submitting any word to the search box
def home(request):

    if request.GET:
            hashtag = request.GET['q']

            # polaritys = [Positive, Negative, Neutral, Hashtag]
            # Allteets = [location, username , created, text]
            [polaritys, alltweets] = twitterAPI.twitter_streamer(hashtag, 200)
            show_content = True
            context = {'polaritys': polaritys, 'show_content': show_content}

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


























'''
    count = 20
    hashtag = "persvako"
    context = {'hashtag': hashtag}
    hashtag = request.GET.get(search)

    return render(request, 'website/home.html', context)

    
'''



