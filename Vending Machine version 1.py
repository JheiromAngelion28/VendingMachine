#Jheirom Angelion M. Pablo Vending Machine

#Phase one Dictionary and prices

# Variable for the amount of money 
money = 100.00
# Dictionary for the menu
vending_machine = {
    "Chips Spicy FLavor ":"0A",
    "Chips Onion Flavor":"0B",
    "Chips Tomato Flavor ":"0C",
    "Chips Brisket Flavor":"0D",
    "Instant Noodles Chicken Flavor":"0E",
    "Instant Noodles Beef Flavor":"0F",
    "Instant Noodles Shrimp Flavor":"0G",
    "Cocacola Soda":"1A",
    "Pepsi Soda":"1B",
    "Diet Coke Soda":"1C",
    "Chocolate Milk Shake":"1D",
    "Strawberry Milk Shake":"1E",
    "Iced Tea":"1F",
    "gatorade Energy Drink ":"1G",
    "Evian Water":"2A",
    "Arwa Water":"2B",
    "Masafi ":"2C",
    "Figi Water":"2D",
    "Boba Milk Tea Caramel Flavor ":"2E",
    "Boba Milk Chocolate Milk Flavor":"2F",
    "Boba Milk Cheese Flavor":"2G"
}

# Updated the menu prices by assigning a letter, and a number in each item making it easy for the user to choose
# Dictionary for the Menu Prices
prices = {
    "Chips Spicy FLavor (0A) ":"15AED",
    "Chips Onion Flavor (0B)":"15AED",
    "Chips Tomato Flavor (0C)":"15AED",
    "Chips Brisket Flavor (0D)":"15AED",
    "Instant Noodles Chicken Flavor (0E)":"10AED",
    "Instant Noodles Beef Flavor (0F)":"10AED",
    "Instant Noodles Shrimp Flavor (0G)":"10AED",
    "Cocacola Soda (1A)":"5AED",
    "Pepsi Soda (1B)":"5AED",
    "Diet Coke Soda (1C)":"5AED",
    "Chocolate Milk Shake (1D)":"10AED",
    "Strawberry Milk Shake (1E)":"10AED",
    "Iced Tea (1F)":"10AED",
    "Gatorade Energy Drink (1G)":"10AED",
    "Evian Water (2A)":"10AED",
    "Arwa Water (2B)":"1AED",
    "Masafi (2C)":"1AED",
    "Figi Water (2D)":"10AED",
    "Boba Milk Tea Caramel Flavor (2E)":"22AED",
    "Boba Milk Chocolate Milk Flavor (2F)":"22AED",
    "Boba Milk Cheese Flavor (2G)":"22AED"
}

#Phase 2 Making the seperate fuctions for the vending machine

def money_set (amount): #This is for setting the balance/money

    # We need to use multiple fuctions for an object/Dictionary
    global money
    
    money = amount

def stock(): # Used to track of the stock
    
    stock = vending_machine.values()
    i = 0
    #Using for loop 
    
    for amount in stock:

        i += amount
    
    print(i)

def purchase(reuired_money): #Used to help in traking the balance left to purchase

    global money
    #Using if else fuction to determin if you have enough balance or not
    
    if money >= reuired_money:

       money -= reuired_money
        
       print("Item paid. You may recieve your order")

    else:
        print("Sorry you do not have enough balance")

def exchange_transaction(user_input): # Used to choose for the item and calls the purchase function above
    global money

    #Using the if else and elif fuction to call the purchase fuction for each price
    
    # "Chips Spicy FLavor ": 15 AED 
    if user_input == "0A":
        purchase(15.00)
    
    # "Chips Onion Flavor": 15 AED
    elif user_input == "0B":
        purchase(15.00)
    
    # "Chips Tomato Flavor ": 15 AED
    elif user_input == "0C":
        purchase(15.00)

    # "Chips Brisket Flavor": 15 AED
    elif user_input == "0D":
        purchase(15.00)

    # "Instant Noodles Chicken Flavor": 10 AED
    elif user_input == "0E":
        purchase(10.00)
    
    # "Instant Noodles Beef Flavor": 10 AED
    elif user_input == "0F":
        purchase(10.00)
    
    # "Instant Noodles Shrimp Flavor": 10 AED
    elif user_input == "0G":
        purchase(10.00)
    
    # "Cocacola Soda": 5 AED
    elif user_input == "1A":
        purchase(5.00)

    # "Pepsi Soda": 5 AED
    elif user_input == "1B":
        purchase(5.00)

    # "Diet Coke Soda": 5 AED
    elif user_input == "1C":
        purchase(5.00)
    
    # "Chocolate Milk Shake": 10 AED 
    elif user_input == "1D":
        purchase(10.00)

    # "Strawberry Milk Shake": 10 AED 
    elif user_input == "1E":
        purchase(10.00)
      
    # "Iced Tea": 10 AED
    elif user_input == "1F":
        purchase(10.00)
    
    # "Gatorade Energy Drink ": 10 AED
    elif user_input == "1G":
        purchase (10.00)
    
    # "Evian Water": 10 AED
    elif user_input == "2A":
        purchase(10.00)

    # "Arwa Water": 1 AED
    elif user_input == "2B":
        purchase(1.00)

    # "Masafi": 1 AED
    elif user_input == "2C":
        purchase(1.00)
    
    # "Figi Water": 10 AED 
    elif user_input == "2D":
        purchase(10.00)

    # "Boba Milk Tea Caramel Flavor": 22 AED
    elif user_input == "2E":
        purchase(22.00)

    # "Boba Milk Chocolate Milk Flavor": 22 AED
    elif user_input == "2E":
        purchase(22.00)

    # "Boba Milk Cheese Flavor": 22 AED
    elif user_input == "2G":
        purchase(22.00)
    
    else: 
        print("The selection is invalid")
    


def main(): #This is the main program
        
        item_list = []

        switch = 1 

        while switch == 1: #This is to greet the user using print fuction
            print("Hello! Welcome to the vending machine")

            print("Here is the menu from which you can choose")

            for item, selection in vending_machine.items():

                    item_list.append((item, selection))
            
            print(item_list[::-1]) # It is printed backwards so that it is from top to bottom


            print()

            print("These are the menu prices") 

            for item, price in prices. items(): # This will print all of the menu items along with their prices

                    print(item, price)
            
            print() 

            user_switch = 1 #To prevent the program from looping 

            while user_switch == 1: #As long as the user switch is equall to 1, 

                   print(" Your balance is currently AED" + str(money))

                   user_input = input ("Please type your selection: ").upper()

                   exchange_transaction(user_input)

                   print()

                   choice = 1

                   while choice ==1: 
                       
                        user_input = input("Are you done with using the vending machine? (y/n)").lower()

                        if user_input == "y":
                            
                            user_switch = 0
                            
                            choice = 0
                            
                            switch = 0
                        
                        elif user_input == "n":
                            
                            user_switch = 1
                            
                            choice = 0

                        else:
                            print("That command is invalid please try again")

                            choice = 1

                            
                    

                  
                  
main()

                             
                        


                        

                        
                        





