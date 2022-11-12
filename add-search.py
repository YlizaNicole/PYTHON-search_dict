#Write a python program for contact tracing:
# - Display a menu of options
#Menu:
# 1 -> Add an item
# 2 -> Search
# 3 -> Exit (y/n)
# - Allow user to select item in the menu (check if valid)
# - Perform the selected option
# - Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
# Use dictionary to store the info
# Use the full name as key
# The value is another dictionary of personal information
# - Option 2: Search, ask full name then display the record
# - Option 3: Ask the user if want to exit or retry.

# - Display a menu of options
my_dict = {}
my_dict2= my_dict
my_dict2={}

print("MENU")
print ("1 = Add an Item")
print ("2 = Search")
print ("3 = Exit")

# - Allow user to select item in the menu (check if valid)
print()
user_input= int(input("pick a number: "))

# - Perform the selected option
# - Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
# Use dictionary to store the info
# Use the full name as key
while True:
    if user_input ==1:
       for i in range (4):
            line1 = input("")
            line2 = input("")
            my_dict[line1] = line2
            print ("SAVED!")
    if user_input ==2:
        search= input("keyword")
        print(my_dict2.keys(search))
    if user_input==3:
        question= input("exit? (y/n)")
        if question == "y":
            break

