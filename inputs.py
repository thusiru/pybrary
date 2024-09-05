from sys import exit


RED = "\033[91m"
RESET = "\033[0m"

first_time = True
if first_time:
    print(
        f"Welcome to Pybrary! For help type {RED}'--help'{RESET} and press enter. For exit type {RED}'--exit'{RESET} and hit enter."
    )
    first_time = False


def parse(text):
    match text.strip().lower():
        case "exit":
            print("Exiting the program...")
            print("Have a nice day! 🙂")
            exit(0)
        case "help":
            print(f"     {RED}exit{RESET} - Exit the Program")
            print(f"     {RED}help{RESET} - Show help")
            print(f"     {RED}search{RESET} - Search for a book title")
            return None
        case _:
            return text
