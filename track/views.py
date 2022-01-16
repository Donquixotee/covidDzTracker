from django.shortcuts import render
import requests
import json
import datetime


def home(request):
    url = "https://covid-193.p.rapidapi.com/history"
    url2 = "https://api.corona-dz.live/country/latest"

    now = datetime.datetime.now()
    querystring = {"country":"Algeria","day":now.strftime("%Y-%m-%d")}

    headers = {
        'x-rapidapi-key': "e089114c6bmshddddafe1595a05bp115ea8jsn2913e90b71d5",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    response2 = requests.request("GET", url2, ).json()



    data = response['response']
    d = data[0]


    context = {
        'all' : d['cases']['total'],
        'recovered' : d['cases']['recovered'],
        'deaths' : d['deaths']['total'],
        'new' : d['cases']['new'],
        'critical' : d['cases']['critical'],
        'newRecovered': response2['newRecovered'],
        'newDeaths': response2['newDeaths'],
        'avg7Confirmed': response2['avg7Confirmed'],
        'avg7Recovered': response2['avg7Recovered'],
        'avg7Deaths': response2['avg7Deaths']
        
    }

    return render(request, 'index.html', context)

