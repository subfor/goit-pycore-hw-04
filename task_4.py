def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    name = args[0]
    return f"Phone number: {contacts.get(name)}"


def show_all(contacts):
    return contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "all":
                if not contacts:
                    print("Contacts not found.")
                all_contacts = show_all(contacts)
                for name, number in all_contacts.items():
                    print(f"Name: {name}, Phone number: {number}")
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(show_phone(args, contacts))
            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()
