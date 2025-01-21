#Jheirom Angelion M. Pablo.
# this code is a dummy code and dose not work
#This is an experimantation of how I can tructure the code
#However this code is nit working as it should be 
# A new version 4 will be created
#Vending Machine version 3


#This version I decided to compress the dictionaries in a list with the names and prices.
# I also Made improvements to the menu and prices
Vending_machine_names_and_prices =  {

       # The list is used to store dictionaries of the items along with the price rather then using 2
"CHIPS SECTION": [
        {"Product ID":1, "Product Name": "Chips Scpicy Flavor","AED": 15},
        {"Product ID":2, "Product Name": "Chips Onion Flavor","AED": 15},
        {"Product ID":3, "Product Name": "Chips Tomato Flavor","AED": 15},
        {"Product ID":4, "Product Name": "Chips Brisket Flavor","AED": 15},
],


"SWEETS SECTION": [
        {"Product ID":5, "Product Name": "Galaxy Chocolate Bar","AED": 15},
        {"Product ID":6, "Product Name": "Galaxy Dark Chocolate Bar","AED": 15},
        {"Product ID":7, "Product Name": "Kitkat Chocolate Chip","AED": 15},
        {"Product ID":8, "Product Name": "M&M Candy","AED": 15},
 ],


"HOT DRINKS SECTION": [
        {"Product ID":9, "Product Name": "Coffee Latte","AED": 15},
        {"Product ID":10, "Product Name": "Cappuccino ","AED": 15},
        {"Product ID":11, "Product Name": "Americano","AED": 15},
        {"Product ID":12, "Product Name": "Espresso","AED": 15},
 ],


 "COLD DRINKS SECTION": [
        {"Product ID":13, "Product Name": "Arwa Water","AED": 15},
        {"Product ID":14, "Product Name": "Evian Water","AED": 15},
        {"Product ID":15, "Product Name": "Iced Coffee","AED": 15},
        {"Product ID":16, "Product Name": "Iced Tea","AED": 15},
 ],


 "SOFT DRINKS SECTION": [
        {"Product ID":17, "Product Name": "Cocacola ","AED": 15},
        {"Product ID":18, "Product Name": "Pepsi Flavor","AED": 15},
        {"Product ID":19, "Product Name": "Sprite Tomato Flavor","AED": 15},
        {"Product ID":20, "Product Name": "Seven Up ","AED": 15},
 ],


 "BOBA SECTION": [
        {"Product ID":21, "Product Name": "Boba Cheese Flavor","AED": 15},
        {"Product ID":22, "Product Name": "Boba CHocolate Flavor","AED": 15},
        {"Product ID":23, "Product Name": "Boba Ube Flavor","AED": 15},
        {"Product ID":24, "Product Name": "Boba Strawberry Flavor","AED": 15},
 ],


 "JUICE SECTION": [
        {"Product ID":25, "Product Name": "Grape Juice","AED": 15},
        {"Product ID":26, "Product Name": "Orange Juice Flavor","AED": 15},
        {"Product ID":27, "Product Name": "Apple Juice Flavor","AED": 15},
        {"Product ID":28, "Product Name": "Carrot Jiuce Flavor","AED": 15},
 ],


   
}

def menu_display():
       print("Welcome to the vending Machine!")
       print("We would like you to choose a a section")
       for section in Vending_machine_names_and_prices():
              print(section)

       
       for product in Vending_machine_names_and_prices:
              print(f"ID {product, Vending_machine_names_and_prices["Product ID"]} :{product, Vending_machine_names_and_prices["Product Name"]} AED{product, Vending_machine_names_and_prices["AED"]}")
              print("Type the word 'exit' if you would like to leave the vending machine  ")
 
def process_selection(balance):
    while True:
                                
       try:
            product_id = int(input("Please enter the product that you may want to buy"))
            if product_id == "exit":
             break

            found = False
            for section in Vending_machine_names_and_prices:
             for product in Vending_machine_names_and_prices[section]:
              if product["Product ID"] == product_id:
               found = True
               if balance >= product["AED"]:
                  balance -= product["AED"]
                  print(f"The item is purchased, the product is {product['Product Name']} for AED{balance}. The change is AED {balance}")
                   

              else:
                  print("Your balance is insuficient, please put more money.  ")

              if not found: 
                     print("The input is invalid please tray again")
              
              cont = input("Woud you like to continyou to yse the machine? type yes or no").strip().lower()
              if cont == 'no':
                     break

       except ValueError:
               print("The imput is invalid. Please try again or type 'exit' to stop the machine")


def main_program():
       balance = float(input("Please insert your money"))
       menu_display()
       process_selection(balance)

       print("Thank you so much for using the veding machine. Have a great day!")
       
main_program()
              

     
              


       
              




                
                              
                             

                 







    





