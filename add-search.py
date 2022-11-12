#Write a python program for contact tracing:

import shelve
import dbm 

# Use dictionary to store the info
# Use the full name as key
def save_dict(to_save):  
    with shelve.open("shelve2.db", "c") as s: 
                s["Dict"] = to_save  
def load_dict():  
        with shelve.open("shelve2.db", "r") as s:  
                saved_dict = s["Dict"]  
                return saved_dict   
dict = load_dict() 
data= list(dict.values())


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
        ask = input("add item(y/n): ") 
        if ask == "y":
                keywords = input("Input full name here: ")
                Values = ("Full Name")
                dict[keywords] = Values
                keywords = print("Age: ")
                Values = input("")
                dict[keywords] = Values
                keywords = print("Address: ")
                Values = input("")
                keywords = print("Email: ")
                Values = input("")
                dict[keywords] = Values
                save_dict(dict)
        elif ask == "n":
            print(dict)  
        print("SAVED!")
        break
#Option 2: Ask the user if want to exit or retry.
    if user_input ==2:
        search= input("Search an Keyword: ")
        print(dict.get(search))
        print(dict.get("Age"))
        print(dict.get("Address"))
        print(dict.get("Email"))
        
       
       
     
#- Option 3: Ask the user if want to exit or retry.
    if user_input==3:
        question= input("exit? (y/n)")
        if question == "y":
            print("bye bye ")
        break

