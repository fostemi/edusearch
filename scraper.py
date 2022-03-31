from serpapi import GoogleSearch
from pymongo import MongoClient
import json

client = MongoClient("mongodb+srv://edusearch:edusearch@cluster0.hiqdm.mongodb.net/scraped?retryWrites=true&w=majority")
db = client.get_database('scraped')

def get_search_sources(query):
    params_gs = {
        "q": query,
        "hl": "en",
        "gl": "us",
        "api_key": "794e970ed3c40b3370c37275a56c63be264ea5e7400dfd33b3dad7075ec17b59" #this is the api key from the edusearch account.
    }
    return GoogleSearch(params_gs)

def get_yt_sources(query):
    params_yt = {
    "engine": "youtube",
    "search_query": query,
    "hl": "en",
    "gl": "us",
    "api_key": "794e970ed3c40b3370c37275a56c63be264ea5e7400dfd33b3dad7075ec17b59"
    }
    return GoogleSearch(params_yt)

def get_scholar_sources(query):
    params_ss = {
    "engine": "google_scholar",
    "q": query,
    "api_key": "794e970ed3c40b3370c37275a56c63be264ea5e7400dfd33b3dad7075ec17b59"
    }
    return GoogleSearch(params_ss)

def get_google_results(query):
    result = get_search_sources(query)
    return result.get_dict()

def get_yt_results(query):
    result = get_yt_sources(query)
    return result.get_dict()

def get_scholar_results(query):
    result = get_scholar_sources(query)
    return result.get_dict()

def search(query):
    response_gs = get_google_results(query)
    results = response_gs.get('organic_results')
    for item in results:
        item['tag'] = 'search_results'
    create_collection = db[query]
    return create_collection.insert_many(results)

def course_search(query):
    response_gs = get_google_results(query + ' courses')
    results = response_gs.get('organic_results')
    for item in results:
        item['tag'] = 'course_results'
    create_collection = db[query]
    return create_collection.insert_many(results)

def yt_search(query):
    response_yt = get_yt_results(query)
    results = response_yt.get('video_results')
    for item in results:
        item['tag'] = 'youtube'
    create_collection = db[query]
    return create_collection.insert_many(results)

def scholar_search(query):
    response_ss = get_scholar_results(query)
    results = response_ss.get('organic_results')
    for item in results:
        item['tag'] = 'scholar'
    create_collection = db[query]
    return create_collection.insert_many(results)

def get_data(query):
  s1 = site()
  subject = []
  col1 = db[query]
  cursor = col1.find({})
  for document in cursor:
    s1.title = document['title']
    s1.link = document['link']
    s1.snippet = document['snippet']
    subject.append(s1)
  return subject
