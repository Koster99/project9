ADDRESSBOOK = {}


def input_error(inner):
    def wrap(*args):
        try:
            return inner(*args)
        except KeyError:
            return "Invalid command. Please enter a valid command."
        except ValueError:
            return "Invalid input. Please enter valid name and phone number."
        except IndexError:
            return "Invalid input. Please enter name and phone number."

    return wrap


@input_error
def add_handler(data):  # Функції обробники команд
    name = data[0].title()
    phone = data[1]
    ADDRESSBOOK[name] = phone
    return f"Contact {name} with phone {phone} was saved"


@input_error
def change_handler(data):
    name = data[0].title()
    phone = data[1]
    if name in ADDRESSBOOK:
        ADDRESSBOOK[name] = phone
        return f'Contact {name} change phone {phone}'
    else:
        return f'Contact "{name}" not found in the list.'


@input_error
def phone_handler(data):
    name = data[0].title()
    if name in ADDRESSBOOK:
        return f'Phone {name} is {ADDRESSBOOK[name]}'
    else:
        return f'Contact "{name}" not found in the list.'


def show_all_handler(*args):
    return str(ADDRESSBOOK)


def exit_handler(*args):
    return "Good bye!"


def hello_handler(*args):
    return "How can I help you"


@input_error
def command_parser(raw_str: str):  # Парсер команд
    elements = raw_str.split()
    for key, value in COMMANDS.items():
        for cmd in value:
            if raw_str.lower().startswith(cmd):
                return key(elements[1:])
    return "Unknown command"


COMMANDS = {
    add_handler: ["add"],
    change_handler: ["change"],
    phone_handler: ["phone"],
    show_all_handler: ["show all"],
    exit_handler: ["good bye", "close", "exit"],
    hello_handler: ["hello"]
}


def main():  # Цикл запит-відповідь.
    while True:
        user_input = input(">>> ")  # add Vlad 0987009090
        result = command_parser(user_input)
        print(result)
        if result == "Good bye!":
            break


if __name__ == "__main__":
    main()
