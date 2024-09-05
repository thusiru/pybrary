from sys import exit


RED = "\033[91m"
RESET = "\033[0m"


def parse(text):
    match text.strip().lower():
        case "--exit":
            print("Exiting the program...")
            print("Have a nice day! 🙂")
            exit
        case "--help":
            print(f"     {RED}--exit{RESET} - Exit the Program")
            print(f"     {RED}--help{RESET} - Show help")
            print(f"     {RED}--title{RESET} - Search for a book title")
            return None
        case _:
            return text
