from books import search_books


def main():
    query = input("Title: ")
    search_books(query)


if __name__ == "__main__":
    main()