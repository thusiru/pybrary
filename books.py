import requests


API_KEY = "AIzaSyBmBpF8M8gKEeyOx-vqrSyw-FZniWqYzAs"
MAX_RESULTS = 5


def search_book(title=None, author=None):
    if not title and not author:
        print("one of Title or Author is required")
        return None
    
    titles = f"{title}+inauthor:{author}"
    payload = {"q": titles, "printType":"books", "key":API_KEY}
    response = requests.get ("https://www.googleapis.com/books/v1/volumes?", params=payload)
    results = response.json()
    print(response.url)

    return[result["volumeInfo"]["title"] for result in results["items"]]
