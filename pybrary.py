from books import search_title
from inputs import parse


def main():
    while True:
        text = parse(input("Input: "))
        if text is None:
            continue
        match text.strip():
            case "--title":
                query = parse(input("Title: "))
                search_title(query)
            case "--author":
                query = parse(input("Author: "))
                search_title(query)


if __name__ == "__main__":
    main()
