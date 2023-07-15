todo_list = []

# add an item
def add_item(item):
    todo_list.append(item)
    print("Item added successfully.")

# remove an item
def remove_item(item):
    if item in todo_list:
        todo_list.remove(item)
        print("Item removed successfully.")
    else:
        print("Item not found in the list.")

#  display the current to-do list
def display_list():
    if len(todo_list) == 0:
        print("No items in the to-do list.")
    else:
        print("To-Do List:")
        for i, item in enumerate(todo_list, 1):
            print(f"{i}. {item}")

# Main program loop
while True:
    print("\n----- TO-DO LIST APP -----")
    print("1. Add item")
    print("2. Remove item")
    print("3. Display list")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item = input("Enter the item to add: ")
        add_item(item)
    elif choice == "2":
        item = input("Enter the item to remove: ")
        remove_item(item)
    elif choice == "3":
        display_list()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
