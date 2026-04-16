menu_commands = {
    '1': 'Start Game',
    '2': 'Load Game',
    '3': 'Settings',
    '4': 'Exit'
}


def display_menu():
    print("Menu:")
    for key, value in menu_commands.items():
        print(f"{key}: {value}")


def handle_choice(choice):
    if choice in menu_commands:
        print(f"You selected: {menu_commands[choice]}")
    else:
        print("Invalid choice. Please try again.")


def main():
    while True:
        display_menu()
        user_choice = input("Please enter your choice: ")
        handle_choice(user_choice)
        if user_choice == '4':
            break


if __name__ == '__main__':
    main()
