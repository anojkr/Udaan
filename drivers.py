# API Key : 87e3e78caa114427892002478ea95e16

from Controller.HeadlineController import HeadlineController
from Controller.EverythingController import EverthingController
from Controller.SourceController import SourceController

from DAO.HeadlinesDAO import HeadlinesDAO
from DAO.EverythingDAO import EverythingDAO
from DAO.SourceDAO import SourceDAO

from pprint import pprint
import requests
import json
import uuid

KEY = '87e3e78caa114427892002478ea95e16'


def headline(query, headlineObject):
    URL = 'https://newsapi.org/v2/top-headlines?country={}&apiKey={}'.format(query, KEY)
    response = requests.get(URL)
    data = json.loads(response.content)
    articles = data['articles']

    resp = {}
    for item in articles:
        uid = uuid.uuid4()
        author = item['author']
        title = item['title']
        headlineResponse = headlineObject.createHeadlines(uid, author, title, query)
        resp[headlineResponse] = True

    print("\nHeadlines")
    pprint(resp)
    print("\nHeadlines News")
    for key in resp.keys():
        print(headlineObject.GetHeadlines(key).title)


def everything(query, everthingObject):
    URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(query, KEY)
    response = requests.get(URL)
    data = json.loads(response.content)
    articles = data['articles']

    resp = {}
    for item in articles:
        uid = uuid.uuid4()
        author = item['author']
        title = item['title']
        everythingResponse = everthingObject.CreateEverything(uid, author, title, query)
        resp[everythingResponse] = True

    print("\n Everything")
    pprint(resp)
    print("\n Everything News")

    for key in resp.keys():
        print(everthingObject.GetEverything(key).title)
    # print(resp)


def sources(sourceObject):
    URL = 'https://newsapi.org/v2/sources?apiKey={}'.format(KEY)
    response = requests.get(URL)
    data = json.loads(response.content)['sources']
    # print(data)
    resp = {}
    for item in data:
        uid = uuid.uuid4()
        name = item['name']
        des = item['description']
        response = sourceObject.CreateSource(uid, name, des)
        resp[uid] = True

    print("\nSources")
    pprint(resp)
    print("\nNews Sources")
    for key in resp.keys():
        print(sourceObject.GetSource(key).name)


def init():
    headlineObject = HeadlineController(HeadlinesDAO())
    everthingObject = EverthingController(EverythingDAO())
    sourceObject = SourceController(SourceDAO())

    headline('za', headlineObject)
    everything('america', everthingObject)
    sources(sourceObject)

    print("Hurry! Ready to code")


if __name__ == '__main__':
    init()
