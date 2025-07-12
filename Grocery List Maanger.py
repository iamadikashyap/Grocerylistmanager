grocery_list =[]
while True:
    print("Welcome to the Grocery List Manager!")
    print("\n Option: add/remove/show/exit")
    action = input("what would you like to do?:")
    if action == "add":
        item= input("Enter the item you want to add:")
        grocery_list.append(item)
        print(f"{item} has been added to your grocery list.")
    elif action == "remove":
        item = input("Enter the item you want to remove:")
        if item in grocery_list:
            grocery_list.remove(item)
            print(f"{item} has been removed from you grocery list.")
        else:
            print(f"{item} is not in your grocery list.")
    elif action == "show":
        print("Your grocery list:")
        for i in grocery_list:
            print(f"-{i}")
    elif action == "exit":
        print("Thanks for using the Grocery List Manager!")
        break
    else:
        print("Invalid option. Please try again.")