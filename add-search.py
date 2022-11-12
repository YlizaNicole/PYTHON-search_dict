#Write a python program for contact tracing:

import shelve
import dbm 

# Use dictionary to store the info
# Use the full name as key
def save_dict(to_save):  
    with shelve.open('shelve2.db', 'c') as s: 
                s['Dict'] = to_save  
def load_dict():  
        with shelve.open('shelve2.db', 'r') as s:  
                saved_dict = s['Dict']  
                return saved_dict   
dict = load_dict() 
# - Display a menu of options
print("MENU")
print ("1 = Add an Item")
print ("2 = Search")
print ("3 = Exit")

# - Allow user to select item in the menu (check if valid)


# - Perform the selected option
# - Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
while True:
    print()
    user_input= int(input("pick a number: "))
    if user_input ==1: 
        ask = input('add item(y/n): ') 
        if ask == 'y':
            keywords = input('keys: ')
            Values = input('values: ')
            dict[keywords] = Values
            save_dict(dict)
        elif ask == 'n':
            print(dict)  
        print("Oh well, nothing else to do here then.")
        break
#Option 3: Ask the user if want to exit or retry.
    if user_input ==2:
        search= input("Search an Keyword: ")
        print(dict.get(search))
        break
#- Option 3: Ask the user if want to exit or retry.
    if user_input==3:
        question= input("exit? (y/n)")
        if question == "y":
            print("bye bye ")
        break

