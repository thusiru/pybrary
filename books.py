import requests


API_KEY = "AIzaSyAaKNHyn9CrpZXrUcj_aqG41rjkju817Ww"
MAX_RESULTS = 5


def search_title(query):
    payload = {"q": query, "key":API_KEY}
    response = requests.get ("https://www.googleapis.com/books/v1/volumes?", params=payload)
    results = response.json()

    for result in results["items"]:
        print(result["volumeInfo"]["title"])