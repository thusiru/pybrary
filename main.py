from books import search_books
from inputs import parse


RED = "\033[91m"
RESET = "\033[0m"


def main():
    print(
        f"Welcome to Pybrary! For help type {RED}'--help'{RESET} and press enter. For exit type {RED}'--exit'{RESET} and hit enter."
    )

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
