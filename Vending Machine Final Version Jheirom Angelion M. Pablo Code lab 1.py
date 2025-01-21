#Vending Machine Final Version jheirom Angelion M. Pablo

#the dictionary has the number, name, and price of each item of the vending machine
#inside them are nested dictionaries to store the item names and prices
vending_machine = {
"1":{"name": "Chips Onion Flavor","Section":"CHIPS","AED":15},
"2":{"name": "Chips Scpicy Flavor","Section":"CHIPS","AED":15},
"3":{"name": "Chips Tomato Flavor","Section":"CHIPS","AED":15},
"4":{"name": "Chips Brisket Flavor","Section":"CHIPS","AED":15},
"5":{"name": "Hot Chocolate Milk","Section":"HOT DRINKS","AED":15},
"6":{"name": "Coffe Latte ","Section":"HOT DRINKS","AED":15},
"7":{"name": "Espresso Coffee","Section":"HOT DRINKS","AED":15},
"8":{"name": "Coffe Americano","Section":"HOT DRINKS","AED":15},
"9":{"name": "Evian Water","Section":"COLD DRINKS","AED":15},
"10":{"name": "Arwa Water","Section":"COLD DRINKS","AED":15},
"11":{"name": "Masafi Water","Section":"COLD DRINKS","AED":15},
"12":{"name": "Iced tea","Section":"COLD DRINKS","AED":15},
"13":{"name": "Chocolate Milkshake","Section":"COLD DRINKS","AED":15},
"14":{"name": "Galaxy Chocolate Bar","Section":"SWEETS","AED":15},
"15":{"name": "Galaxy Dark Chocolate Bar","Section":"SWEETS","AED":15},
"16":{"name": "M%M Cany","Section":"SWEETS","AED":15},
"17":{"name": "KitKat CHocolate Bar","Section":"SWEETS","AED":15},
"18":{"name": "Grape Juice","Section":"JUICE","AED":15,},
"19":{"name": "Apple Juice","Section":"JUICE","AED":15},
"10":{"name": "Strawberry Juice","Section":"JUICE","AED":15},
"21":{"name": "Carrot Juice","Section":"JUICE","AED":15},
"22":{"name": "Boba Cheese Flavor","Section":"BOBA DRINK","AED":15},
"23":{"name": "Boba Chocolate Flavor","Section":"BOBA DRINK","AED":15},
"24":{"name": "Boba Strawbverry Flavor","Section":"BOBA DRINK","AED":15},
"25":{"name": "Boba Ube Flavor","Section":"BOBA DRINK","AED":15},
"26":{"name": "Boba Caramel Flavor","Section":"BOBA DRINK","AED":15}
 
}

#The first fuction is used to print the menu coming from the dictionary.
def print_menu():
    print("Available Products:")
    sections = set([item['Section'] for item in vending_machine.values()])
    for section in sections:
     print(f"\n{section}:")
     for key, item in vending_machine.items():
      if item["Section"] == section:
       print(f"{key}.{item['name']} -AED{item['AED']}")

#the second fuction is used to make the payment and change.
def process_transaction(price):
    print(f"Please insert your money in AED{price}")
    money_inserted = float(input("Please enter the amount of money you want to deposit"))

    if money_inserted < price:
        print("The amount paid is not enough. Please add more money")

    else:
        change = money_inserted - price
        print(f"The Payment is sucsessful! Your change is AED{change:.2f} ")
        return True 

#This is the main program of the machine combining the other 2 fuctions.
def vending_machine_simulation():
    print_menu()
    while True:
        item_number = input("Select the items by entering its number: ")
        if item_number not in vending_machine:
            print("The input is invalid, please try again.")
            continue  # if input is invalid
        item = vending_machine[item_number]
        print(f"You have selected: {item['name']} -- AED{item['AED']}")
        process_transaction(item['AED'])  
        
        print('Thank you for using the vending machine. Would you like to keep using it? (y/n)')
        user_choice = input().strip().lower()  # Normalize input to lowercase
        if user_choice == "y":
            continue  
        elif user_choice == "n":
            print("Thank you for using the vending machine. Goodbye!")
            break  
        else:
            print("Invalid input. Exiting the vending machine. Goodbye!")
            break



vending_machine_simulation()



