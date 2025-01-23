# Dictionary containing product information with product codes as keys
products = {
    'A1': {'name': 'Soda', 'price': 16, 'stock': 10},
    'A2': {'name': 'Chips', 'price': 15, 'stock': 5},
    'A3': {'name': 'Candy', 'price': 15, 'stock': 20}
}

#To display the menu, price, and stock
def display_products():
    print("Here are the available products:")
    for code,item in products.items():
     print(f"{code}: {item['name']} - AED{item['price']} (Stock: {item['stock']})")

#Shopping cart
def add_to_cart(cart,code,quantity):
   if code in products and products[code]['stock'] >= quantity:
      if code in cart:
         cart[code][quantity] += quantity
      else:
         cart[code] ={'name':products[code]['name'],'price':products[code]['price'],'quantity':quantity}
         
         products[code]['stock'] += quantity
         print(f"Added{quantity}{products[code]['name']}(s) to your cart")
   else:
       print("The product is not available or out of stock")

#To display the cart
def show_cart(cart):
   if not cart:
      print("Your cart has no items")
   else:
      print("Your cart inventory is:")
      total_cost = 0 
      for code,item in cart.items():
         item_total = item['quantity']* item['price']
         total_cost += item_total
         print(f"{item['name']} - Quantity: {item['quantity']} - Each: AED {item['price']},Total: AED{item_total}")
         print(f"\nTotal Cost: AED {total_cost}")
      return total_cost
   
#Payment processing
def process_payment(total_cost):
   print(F"Total amount of cost: AED {total_cost}")
   while True:
      try:
         payment = float(input("Pease enter your payment:"))
         if payment < total_cost:
            print(f"The amount is insufficient. Please add AED {total_cost} - payment more")
         else:
            change = payment - total_cost
            print(f"Payment is successful! your change is AED {change:.2f}")
            break
      except ValueError:
       print("The input is not valid. Please enter a numeric value")

#The main vending machine fuction
def main():
   cart = {}
   while True:
      display_products()
      user_input= input("Please enter the product ID and quantity of the item you want to buy (e.g.,A2 5) or type 'done' to finish")
      if user_input.lower() == 'done':
         break
      else:
         try:
            code,quantity = user_input.split()
            quantity = int(quantity)
            add_to_cart(cart,code.upper(),quantity)
         except ValueError:
            print("The input is invalid. Please enter a valid item code or quantity")

   total_cost = show_cart(cart)
   if total_cost > 0:
      process_payment(total_cost)

# To start the script
if __name__ == "__main__":
   main()

       

   