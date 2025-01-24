#Vending Machine Final Version Jheirom Angelion M. Pablo
# For the final version, Idecided to try and learn a GUI user interface


import tkinter as tk
from tkinter import messagebox

# Dictionary containing product information with product codes as keys
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

# Create the main window
root = tk.Tk()
root.title("Vending Machine")
root.config(bg="#f0f9ff",)

# Cart dictionary
cart = {}

# Function to add products to the shopping cart
def add_to_cart():
    code = product_code_entry.get().upper()
    try:
        quantity = int(quantity_entry.get())
        if code in products and products[code]['stock'] >= quantity:
            if code in cart:
                cart[code]['quantity'] += quantity
            else:
                cart[code] = {
                    'name': products[code]['name'],
                    'price': products[code]['price'],
                    'quantity': quantity
                }
            products[code]['stock'] -= quantity
            messagebox.showinfo("Success", f"Added {quantity} {products[code]['name']}(s) to your cart.")
            update_product_list()
            show_cart()
        else:
            messagebox.showerror("Error", "Product not available or not enough stock.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid product code and quantity.")

# Function to update product list
def update_product_list():
    product_list.delete(1.0, tk.END)
    product_list.insert(tk.END, "Available Products:\n")
    for code, item in products.items():
        product_list.insert(
            tk.END, f"{code}: {item['name']} - ${item['price']} (Stock: {item['stock']})\n"
        )

# Function to display the contents of the cart
def show_cart():
    cart_contents.delete(1.0, tk.END)
    cart_contents.insert(tk.END, "Your Cart:\n")
    total_cost = 0
    for code, item in cart.items():
        item_total = item['quantity'] * item['price']
        total_cost += item_total
        cart_contents.insert(
            tk.END, f"{item['name']} - Quantity: {item['quantity']} - Each: AED{item['price']}, Total: AED{item_total:.2f}\n"
        )
    total_label.config(text=f"Total: AED{total_cost:.2f}")

# Function to process payment
def process_payment():
    try:
        payment = float(payment_entry.get())
        total_cost = sum(item['quantity'] * item['price'] for item in cart.values())

        if payment >= total_cost:
            change = payment - total_cost
            messagebox.showinfo("Payment Successful", f"Payment accepted!\nChange: AED{change:.2f}")
            reset_cart()
        else:
            messagebox.showerror("Payment Error", "The payment is not enough. Please enter more money.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid payment amount.")

# Function to reset the cart
def reset_cart():
    global cart
    cart = {}
    show_cart()
    total_label.config(text="Total: AED0.00",font=("Times new roman",12,"bold"))
    payment_entry.delete(0, tk.END)
    update_product_list()

# Widgets
product_code_label = tk.Label(root, text="Product Code:", font=("Times new roman", 12, "bold"),bg="#f0f8ff", fg="#000080")
product_code_label.grid(row=0, column=0)
product_code_entry = tk.Entry(root)
product_code_entry.grid(row=0, column=1)

quantity_label = tk.Label(root, text="Quantity:",font=("Times new roman",12,"bold"),bg="#f0f8ff", fg="#000080")
quantity_label.grid(row=1, column=0)
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=1, column=1)

add_button = tk.Button(root, text="Add to Cart",font=("Times new roman",12,"bold"), command=add_to_cart, bg="#f0f8ff", fg="#006400")
add_button.grid(row=2, column=0, columnspan=3)

product_list = tk.Text(root, height=20, width=70)
product_list.grid(row=3, column=0, columnspan=2)
update_product_list()

cart_contents = tk.Text(root, height=20, width=70 )
cart_contents.grid(row=4, column=0, columnspan=2)


total_label = tk.Label(root, text="Total: AED0.00",font=("Times new roman",12,"bold"))
total_label.grid(row=5, column=0, columnspan=2)

payment_label = tk.Label(root, text="Payment Amount AED:",font=("TImes new roman",12,"bold"),bg="#f0f8ff", fg="#006400")
payment_label.grid(row=7, column=0)
payment_entry = tk.Entry(root)
payment_entry.grid(row=7, column=1)

pay_button = tk.Button(root, text="Pay Now",font=("TImes new roman",12,"bold"), command=process_payment, bg="#f0f8ff", fg="red")
pay_button.grid(row=7, column=0, columnspan=90)

# Start the main loop
root.mainloop()

   