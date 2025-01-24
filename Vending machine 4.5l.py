import tkinter as tk
from tkinter import messagebox


products = {
    'A1': {'name': 'Chips Onion Flavor', 'price': 5, 'stock': 10},
    'A2': {'name': 'Chips Scpicy Flavor', 'price': 5, 'stock': 5},
    'A3': {'name': 'Chips Tomato Flavor', 'price': 5, 'stock': 20},
    'A4': {'name': 'Chips Brisket Flavor', 'price': 5, 'stock': 20},
    'B1': {'name': 'Hot Chocolate Milk', 'price': 6, 'stock': 20},
    'B2': {'name': 'Coffe Latte', 'price': 6, 'stock': 20},
    'B3': {'name': 'Espresso Coffee', 'price': 6, 'stock': 20},
    'B4': {'name': 'Coffe Americano', 'price': 7, 'stock': 20},
    'C1': {'name': 'Evian Water', 'price': 9, 'stock': 20},
    'C2': {'name': 'Arwa Water', 'price': 1, 'stock': 20},
    'C3': {'name': 'Masafi Water', 'price': 1, 'stock': 20},
    'C4': {'name': 'Iced tea', 'price': 9, 'stock': 20},
    'C5': {'name': 'Chocolate Milkshake', 'price': 6, 'stock': 20},
    'D1': {'name': 'Galaxy Chocolate Bar', 'price': 6, 'stock': 20},
    'D2': {'name': 'Galaxy Dark Chocolate Bar', 'price': 2, 'stock': 20},
    'D3': {'name': 'M%M Candy', 'price': 2, 'stock': 20},
    'D4': {'name': 'KitKat Chocolate Bar', 'price': 2, 'stock': 20},
    'E1': {'name': 'Apple Juice', 'price': 12, 'stock': 20},
    'E2': {'name': 'Grape Juice', 'price': 12, 'stock': 20},
    'E3': {'name': 'Strawberry Juice', 'price': 12, 'stock': 20},
    'E4': {'name': 'Carrot Juice', 'price': 12, 'stock': 20},
    'F1': {'name': 'Boba Cheese Flavor', 'price': 15, 'stock': 20},
    'F2': {'name': 'Boba Chocolate Flavor', 'price': 15, 'stock': 20},
    'F3': {'name': 'Boba Strawberry Flavor', 'price': 15, 'stock': 20},
    'F4': {'name': 'Boba Ube Flavor', 'price': 15, 'stock': 20},
    'F5': {'name': 'Boba Caramel Flavor', 'price': 15, 'stock': 20},

}
 
root = tk.Tk()
root.title("Jheirom's Vending machine")
root.config(bg="#f0f9ff",)
root.geometry
shopping_cart = {}

def add_to_cart():
    food = product_code_entry.get().upper()
    try:
        quantity = int(quantity_entry.get())
        if food in products and products[food]['stock'] >= quantity:
            if food in shopping_cart:
                shopping_cart[food]['quantity'] += quantity
            else:
                shopping_cart[food] = {
                    'name': products[food]['name'],
                    'price': products[food]['price'],
                    'quantity': quantity
                }
            products[food]['stock'] -= quantity
            messagebox.showinfo("You have successfully added", f"{quantity} {products[food]['name']}(s) into your shopping cart")
            update_product_list()
            show_cart()
        else:
            messagebox.showerror("Sorry, the product is out of stock")
    except ValueError:
        messagebox.showerror("The input is invalid. Please try again")

def update_product_list():
    product_list.delete(1.0, tk.END)
    product_list.insert(tk.END, "Welcome to the vending machine! Here are the available products\n" )
    for food, item in products.items():
        product_list.insert(
            tk.END,f"{food} {item['name']} - AED{item['price']} (Stock: {item['stock']} \n",
        ),

def show_cart():
    cart_contents.delete(1.0, tk.END)
    cart_contents.insert(tk.END, "Your shopping cart inventory:\n")
    total_cost = 0
    for food,item in shopping_cart.items():
        item_total = item ['quantity'] * item['price']
        
        total_cost += item_total
        cart_contents.insert(
          tk.END, f"{item['name']} - Quantity: {item['quantity']} - Each: AED{item['price']}, Total: AED{item_total:.2f}\n"
        )
    total_label.config(text=f"Total: AED{total_cost:.2f}") 

def process_payment():
    try:
        payment = float(payment_entry.get())
        total_cost = sum(item['quantity'] * item['price'] for item in shopping_cart.values())
        if payment >= total_cost:
           change = payment - total_cost
           messagebox.showinfo("The Payment is successful!", f"The payment is accepted with a change of \n AED:{change:.2f}")
           reset_cart() 
        else:
            messagebox.showerror("Error. The amout given isnot enough. Please add more money")
    except ValueError:
        messagebox.showerror("The input is invalid. Please try again")

def reset_cart():
    global shopping_cart
    shopping_cart = {}
    show_cart()
    total_label.config(text="Total: AED0.00",font=("Times new roman",12,"bold"))
    payment_entry.delete(0, tk.END)
    update_product_list()


product_code_label = tk.Label(root, text="Product Code:", font=("Times new roman", 12, "bold"),bg="#f0f8ff", fg="#000080")
product_code_label.grid(row=1, column=0) 
product_code_entry = tk.Entry(root)
product_code_entry.grid(row=0, column=1)

quantity_label = tk.Label(root, text="Quantity:",font=("Times new roman",12,"bold"),bg="#f0f8ff", fg="#000080")
quantity_label.grid(row=1, column=0)
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=1, column=1)

add_button = tk.Button(root, text="Add to Cart",font=("Times new roman",12,"bold"), command=add_to_cart, bg="#f0f8ff", fg="#006400")
add_button.grid(row=2, column=0, columnspan=3)

product_list = tk.Text(root, height=25, width=100)
product_list.grid(row=3, column=0, columnspan=2,) 
update_product_list()

cart_contents = tk.Text(root, height=25, width=100)
cart_contents.grid(row=4, column=0, columnspan=2), 


total_label = tk.Label(root, text="Total: AED0.00",font=("Times new roman",12,"bold"))
total_label.grid(row=5, column=0, columnspan=2)

payment_label = tk.Label(root, text="Payment Amount AED:",font=("TImes new roman",12,"bold"),bg="#f0f8ff", fg="#006400")
payment_label.grid(row=7, column=0)
payment_entry = tk.Entry(root)
payment_entry.grid(row=7, column=1)

pay_button = tk.Button(root, text="Pay Now",font=("TImes new roman",12,"bold"), command=process_payment, bg="#f0f8ff", fg="red")
pay_button.grid(row=7, column=0, columnspan=90)


root.mainloop()

   

     






