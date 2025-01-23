#Vending Machine Final Version jheirom Angelion M. Pablo

#the dictionary has the number, name, and price of each item of the vending machine
#inside them are nested dictionaries to store the item names and prices
vending_machine = {
"1":{"name": "Chips Onion Flavor","Section":"A: CHIPS","AED":10},
"2":{"name": "Chips Scpicy Flavor","Section":"A: CHIPS","AED":10},
"3":{"name": "Chips Tomato Flavor","Section":"A: CHIPS","AED":10},
"4":{"name": "Chips Brisket Flavor","Section":"A: CHIPS","AED":10},
"5":{"name": "Hot Chocolate Milk","Section":"B: HOT DRINKS","AED":5},
"6":{"name": "Coffe Latte ","Section":"B: HOT DRINKS","AED":6},
"7":{"name": "Espresso Coffee","Section":"B: HOT DRINKS","AED":6},
"8":{"name": "Coffe Americano","Section":"B: HOT DRINKS","AED":6},
"9":{"name": "Evian Water","Section":"C: COLD DRINKS","AED":10},
"10":{"name": "Arwa Water","Section":"C: COLD DRINKS","AED":1},
"11":{"name": "Masafi Water","Section":"C: COLD DRINKS","AED":1},
"12":{"name": "Iced tea","Section":"C: COLD DRINKS","AED":15},
"13":{"name": "Chocolate Milkshake","Section":"C: COLD DRINKS","AED":12},
"14":{"name": "Galaxy Chocolate Bar","Section":"D: SWEETS","AED":2},
"15":{"name": "Galaxy Dark Chocolate Bar","Section":"D: SWEETS","AED":2},
"16":{"name": "M%M Cangy","Section":"D: SWEETS","AED":2},
"17":{"name": "KitKat CHocolate Bar","Section":"D: SWEETS","AED":2},
"18":{"name": "Grape Juice","Section":"E: JUICE","AED":5,},
"19":{"name": "Apple Juice","Section":"E: JUICE","AED":5},
"10":{"name": "Strawberry Juice","Section":"E: JUICE","AED":5},
"21":{"name": "Carrot Juice","Section":"E: JUICE","AED":5},
"22":{"name": "Boba Cheese Flavor","Section":"F: BOBA DRINK","AED":15},
"23":{"name": "Boba Chocolate Flavor","Section":"F: BOBA DRINK","AED":15},
"24":{"name": "Boba Strawbverry Flavor","Section":"F: BOBA DRINK","AED":15},
"25":{"name": "Boba Ube Flavor","Section":"F: BOBA DRINK","AED":15},
"26":{"name": "Boba Caramel Flavor","Section":"F: BOBA DRINK","AED":15}
 
}

#The first fuction is used to print the menu coming from the dictionary.
def print_menu():
    print("Welcome to the vending machine! Here are the available Products:")
    sections = sorted(set(item['Section'] for item in vending_machine.values()))
    for section in sections:
     print(f"\n{section}:")
     for key, item in vending_machine.items():
      if item["Section"] == section:
       print(f"{key}.{item['name']} - AED {item['AED']}")

#the second fuction is used to make the payment and change.
def process_transaction(price):
     print(f"The price is AED{price}")
     while True:
        try:
            money_inserted = float(input("Please enter the amount of money you want to deposit: "))
            if money_inserted < price:
                print("The amount paid is not enough. Please add more money.")
            else:
                change = money_inserted - price
                print(f"The payment is successful! Your change is AED{change:.2f}.")
                return True
        except ValueError:
            print("The input is invalid. Please enter a valid number.")
            return vending_machine_simulation()
            
        

#This is the main program of the machine combining the other 2 fuctions.
def vending_machine_simulation():
    print_menu()
    while True:
        item_number = input("Select the items by entering its number:")
        if item_number not in vending_machine:
            print("The input is invalid, please try again")
            vending_machine_simulation()
        item = vending_machine[item_number]
        print(f"You have selected: {item['name']} -- AED{item['AED']}")
        
        if process_transaction(item['AED']):
            more_items = input("\nDo you want to buy more items? Type 'y' for yes or 'n' for no: ").lower()
            if more_items == "y":
                continue
            elif more_items == "n":
                print("Thank you for using the vending machine!")
                break
            else:
                print("Invalid input. Exiting the vending machine at once.")
                return


vending_machine_simulation()