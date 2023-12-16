def start():
    return 'How can I help you?'


def change_contact(args, contacts):
    name, phone = args

    if not contacts.get(name):
        return 'Invalid name'

    contacts[name] = phone
    return "Contact updated."


def show_phone(name, contacts):
    return contacts.get(name[0], 'Invalid name')


def show_all(contacts):
    return '\n'.join([f"{name} - {phone}" for name, phone in contacts.items()])


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def finish():
    return 'Good bye!'


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(finish())
            break
        elif command == "hello":
            print(start())
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
