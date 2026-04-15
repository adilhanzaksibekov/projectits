def display_menu():
    print("Selection Menu")
    print("1. Add Item")
    print("2. View Items")
    print("3. Edit Item")
    print("4. Delete Item")
    print("5. Exit")

items = []

def add_item():
    item = input("Enter the name of the item to add: ")
    items.append(item)
    print(f'Item "{item}" added.')


def view_items():
    if items:
        print("Items:")
        for index, item in enumerate(items, start=1):
            print(f'{index}. {item}')
    else:
        print("No items to display.")


def edit_item():
    view_items()
    index = int(input("Enter the item number to edit: ")) - 1
    if 0 <= index < len(items):
        new_item = input("Enter the new name for the item: ")
        items[index] = new_item
        print(f'Item updated to "{new_item}".')
    else:
        print("Invalid item number.")


def delete_item():
    view_items()
    index = int(input("Enter the item number to delete: ")) - 1
    if 0 <= index < len(items):
        item = items.pop(index)
        print(f'Item "{item}" deleted.')
    else:
        print("Invalid item number.")


def main_loop():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_item()
        elif choice == '2':
            view_items()
        elif choice == '3':
            edit_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_loop()