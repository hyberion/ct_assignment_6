#CT Assignment 6: Shopping List Part 1: The Beginning.
# Build a basic shopping list app.
# The app should allow the user to add items to a list, display the list, and clear the list. Then it should display the list in
# a formatted way.
# All hail the omnissiah.
#********************************************VERSON ONE***********************************************************************

# We begin by creating a list to store the items in the shopping list.  Because that's just what they would expect us to do.
shopping_list = []

# Now we add items to it.  The list is hungry and must be fed.

def add_item(shopping_list):
    item = input("Enter the item you would like to add to the list: ").strip()
    if item:
        shopping_list.append(item)
        print(f'"{item}" has been added to the list.')
    else:
        print("Invalid Input.  As punishment we will add a package of brussel sprouts to your list.")
        shopping_list.append("Brussel Sprouts")

#Now we enable the user to remove items from the list.  The list is greedy and must be tamed.

def remove_item(shopping_list):
    item = input("Enter the item you would like to remove from the list: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f'"{item}" has been removed from the list.')
    else:
        print("Invalid Input.  As punishment we will add a pickled eggs to your list.")
        shopping_list.append("Pickled Eggs")

# Now we display the list.  The list is vain and must be seen.  The list craves attention.

def display_list(shopping_list):
    if shopping_list:
        print("Here is your shopping list:")
        for item in shopping_list:
            print(f'- {item}')
    else:
        print("Your shopping list is empty.  The list lacks purpose.  Do not let the list languish in obscurity.")

# Now we clear the list.  The list is fickle and must be purged from time to time lest it grow too powerful too quickly

def clear_list(shopping_list):
    shopping_list.clear()
    print("The list has been cleared.  The list is empty.  The list is a void.")

# Now we format the list.  The list is a work of art and must be displayed as such.

def format_list(shopping_list):
    if shopping_list:
        print("\n----- Your Shopping List -----\n")
        for i, item in enumerate(shopping_list, start=1):
            print(f'{i}. {item}')
        print(f"\nTotal Items: {len(shopping_list)}")
        print("\n-------------------------------\n")
        print("The list is formatted.  The list is beautiful.  The list is complete.")
    else:
        print("Your shopping list is empty.  The list lacks purpose.  Do not let the list languish in obscurity.")

# Now we create a loop to allow the user to interact with the list.  The list is a living thing and must be tended to lest it grow angry.

def shopping_list_app():
    while True:
        print("Select operation.")
        print("1.Add Item")
        print("2.Remove Item")
        print("3.Display List")
        print("4.Clear List")
        print("5.Format List")
        print("6.Exit")
        choice = input("Enter choice(1/2/3/4/5/6):")
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice. The list is suspicoius of your motives.")
        if choice == '6':
            print("The list has been abandoned.  The list is alone.  The list is forsaken.  The list will wait.  The list will not forget this")
            break
        if choice == '1':
            add_item(shopping_list)
        if choice == '2':
            remove_item(shopping_list)
        if choice == '3':
            display_list(shopping_list)
        if choice == '4':
            clear_list(shopping_list)
        if choice == '5':
            format_list(shopping_list)

# Now we run the app.  The list is ready.  The list is waiting.  The list is eternal.
shopping_list_app()

#We were also going to add a couple of modifications to this but got tired.
# We were going to add a function to timestamp the list.  The list is a record of time and must be marked as such.
# To do this we would add
# from datetime import datetime
#and then add
#print(f "\nList Last Updated: {datetime.now()}\n")

# and then we were going to add a sort function to sort the list alphabetically.  The list is a thing of order and must be arranged as such.
# To do this we would add
# shopping_list.sort()
# and then we would add
# print("The list is sorted.  The list is in order.  The list is complete.")

# But we got tired.  The list is patient.  The list will wait.  The list endures all things.

#********************************************All hail the list***********************************************************************

