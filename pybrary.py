from books import search_books
from inputs import parse


def main():
    while True:
        text = parse(input("Input: "))
        if text is None:
            continue
        match text.strip():
            case "--title":
                query = parse(input("Title: "))
                search_books(query)


if __name__ == "__main__":
    main()
