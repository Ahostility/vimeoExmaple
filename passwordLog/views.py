from django.shortcuts import render
from pymongo import *
from django.http import JsonResponse,HttpResponse

def insert_document(collection, data):
    """ Function to insert a document into a collection and
    return the document's id.
    """
    return collection.insert_one(data).inserted_id

def videoCreate(request):
    name = "https://player.vimeo.com/video/535464304"
    return render(request,'videoVimeo/videoVimeo.html',locals())
"""
<iframe src="https://player.vimeo.com/video/535464304"
width="640" height="298" frameborder="0" allow="autoplay;
fullscreen; picture-in-picture" allowfullscreen></iframe>
"""

def find_document(collection, elements, multiple=False):
    """ Function to retrieve single or multiple documents from a provided
    Collection using a dictionary containing a document's elements.
    """
    if multiple:
        results = collection.find(elements)
        return [r for r in results]
    else:
        return collection.find_one(elements)

# Create the client
client = MongoClient('localhost', 27017)

# Connect to our database
db = client['SeriesDB']

# Fetch our series collection
series_collection1 = db['passwordLog_checkaudioname']
series_collection2 = db['auth_user']


new_show = {
    "name": "FRIENDS",
    "year": 1994
}

# print(insert_document(series_collection, new_show))

# result1 = find_document(series_collection1, {'datetime': "2020.12.12"})
# result2 = find_document(series_collection2, {'username': 'jfisto'})
# print(dict(result1).get('passUser'))
# print(dict(result2).get('email'))

# Create your views here.
def acync_job(request):
    return HttpResponse('Start uploading...')
