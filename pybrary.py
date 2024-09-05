from books import search_book
from inputs import parse


def main():
    while True:
        text = parse(input("Command: "))
        if text is None:
            continue
        match text.strip():
            case "search":
                search()

def search():
    title = parse(input("Title: "))
    author = parse(input("Author: "))
    books = search_book(title, author)
    for book in books:
        print(book)


if __name__ == "__main__":
    main()
