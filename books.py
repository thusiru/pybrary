from googleapiclient.discovery import build


API_KEY = "AIzaSyAaKNHyn9CrpZXrUcj_aqG41rjkju817Ww"


def search_books(query):
    service = build("books", "v1", developerKey=API_KEY)
    request = service.volumes().list(q=query)
    response = request.execute()

    if "items" in response:
        for item in response["items"]:
            title = item["volumeInfo"]["title"]
            print(title)

    else:
        print("No books found.")