import base64
import sys
import json
import requests


def movie(moviename):
    api_key_base64 = 'ODY0YjhiZmY='  #Don't look Secret key '864b8bff'
    api_key = base64.b64decode(api_key_base64).decode('utf-8')
    #print(api_key)
    url = 'http://www.omdbapi.com/?t={mn}&apikey={ak}'.format(mn=moviename, ak=api_key)
    #print(url)
    response = requests.get(url)
    moviedetails = json.loads(response.text)
    # Pretty print JSON
    # print(json.dumps(moviedetails,indent=4))
    if ('Ratings' not in moviedetails.keys()):
        print('Ratings data not available for the movie. Exiting')
        exit()
    movieratings = moviedetails['Ratings']
    rating = False
    for i in movieratings:
        if (i['Source'] == 'Rotten Tomatoes'):
            rating = i['Value']
    if (not rating):
        print('Rotten Tomatoes rating not available for the movie. Exiting')
    else:
        return rating

arguments = sys.argv
arguments.pop(0)
moviename = ' '.join(arguments)
print(movie(moviename))
