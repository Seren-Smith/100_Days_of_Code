print("🍕 Welcome to List Manager! 🍕")

# Part 1: Build list
food_list = []

for i in range(5):
    food = input(f"Enter favorite food #{i + 1}: ")
    food_list.append(food)

print("\nHere's your food list:")
for idx, item in enumerate(food_list):
    print(f"{idx}: {item}")

# Part 2: Index viewer
try:
    index = int(input("\nEnter an index to view: "))
    print(f"Item at index {index} is {food_list[index]}")
except IndexError:
    print("That index doesn't exist!")
except ValueError:
    print("Please enter a number.")

# Part 3: Edit Menu
while True:
    print("\n🍽️ Edit Menu:")
    print("1. Add item")
    print("2. Insert item at index")
    print("3. Remove item by name")
    print("4. Remove item by index")
    print("5. Show list")
    print("6. Exit")

    choice = input("Pick an option (1-6): ")

    if choice == '1':
        new_item = input("Add what food? ")
        food_list.append(new_item)
        print(f"'{new_item}' added to the list!")
    elif choice == '2':
        item = input("What to insert? ")
        try:
            index = int(input("At what index? "))
            food_list.insert(index, item)
            print(f"'{item}' inserted at index {index}!")
        except ValueError:
            print("Invalid index.")
    elif choice == '3':
        item = input("What to remove? ")
        if item in food_list:
            food_list.remove(item)
            print(f"'{item}' removed from the list!")
        else:
            print("That item isn't in your list.")
    elif choice == '4':
        try:
            index = int(input("Index to remove? "))
            removed_item = food_list.pop(index)
            print(f"'{removed_item}' removed from index {index}!")
        except (ValueError, IndexError):
            print("Invalid index.")
    elif choice == '5':
        print("\nCurrent list:")
        if not food_list:
            print("(The list is currently empty)")
        else:
            for idx, item in enumerate(food_list):
                print(f"{idx}: {item}")
    elif choice == '6':
        print("\nFinal list:")
        if not food_list:
            print("(The list is empty)")
        else:
            for idx, item in enumerate(food_list):
                print(f"{idx}: {item}")
        print("\nExiting List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
