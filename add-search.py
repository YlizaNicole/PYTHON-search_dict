#Write a python program for contact tracing:
dict={}
# - Display a menu of options
Menu= print("========MENU========")
print ("| [1] = Add an Item |")
print ("| [2] = Search      |")
print ("| [3] = Exit        |")
print("====================")

# - Allow user to select item in the menu (check if valid)


while True:
    print()
    user_input= int(input("pick a number: "))
    # - Perform the selected option
 # - Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
    if user_input ==1:
        print("Type your Details")
        FullName= input( "Full Name: ")
        details={ # Use dictionary to store the info
            FullName:{ # Use the full name as key
                "age": int(input("age: ")),
                "adress": input("adress: "),
                "number": int(input("number: "))
            }
            }
        print("SAVED!")
        dict.update(details)
# - Perform the selected option
#Option 2: Search, ask full name then display the record
    if user_input ==2:
        print("Input the Full Name to search for the details")
        search= input("Full Name:")
        age = (dict[search]["age"])
        print ("age:", age)
        adress= (dict[search]["adress"])
        print ("adress:", adress)
        num = (dict[search]["number"])
        print("number:", num)

# - Perform the selected option
#- Option 3: Ask the user if want to exit or retry.
    if user_input==3:
        question= input("exit? (y/n)")
        if question == "y":
            print("bye bye :>")
        break
