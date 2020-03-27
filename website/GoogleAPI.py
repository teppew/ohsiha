from django import forms
#from django.shortcuts import render_to_response
#from gmapi import maps
#from gmapi.forms.widgets import GoogleMap
import requests

res = requests.get('https://ipinfo.io/')
print(res.text["city"])



'''
class MapForm(forms.Form):
    map = forms.Field(widget=GoogleMap(attrs={'width':510, 'height':510}))

    def index(request):
        gmap = maps.Map(opts =
        {
            'center': maps.LatLng(38, -97),
            'mapTypeId': maps.MapTypeId.ROADMAP,
            'zoom': 3,
            'mapTypeControlOptions': { 'style': maps.MapTypeControlStyle.DROPDOWN_MENU },
        })
        context = {'form': MapForm(initial={'map': gmap})}
        return render_to_response('home.html', context)
'''
