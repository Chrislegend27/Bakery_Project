import tkinter as tk
from PIL import Image, ImageTk
import json, random

#Initializing Variables:
#list of items in your cart as string
cart = []
#Your total order price
total = 0
#List of items in cart as a dictionary which included the image link, price, and name of product.
current_cart = []

#Your final order
order = None
# order_number = 1
root = tk.Tk()


#This function adds i
def addtocart(product):
    global total
    cart.append(product["name"])
    total += product["price"]
    current_cart.append(product)


#This variable is the list of items in stock as a list with a dictionary. Within each dictionary is: "name", "price", "image resource"
current_items = [{
    "name": "Glazed Donuts",
    "price": 10.99,
    "image": "Resources/Donuts.jpg"
}, {
    "name": "Chocolate Donuts",
    "price": 12.99,
    "image": "Resources/my_image.jfif"
}, {
    "name": "Apple Fritter",
    "price": 10.99,
    "image": "Resources/Apple_Fritter.jpg"
}, {
    "name": "Jelly Filled Donuts",
    "price": 12.99,
    "image": "Resources/Jelly_Filled_Donuts.jpg"
}, {
    "name": "Tiramisu ",
    "price": 10.99,
    "image": "Resources/Tiramisu.jpg"
}, {
    "name": "Red Velvet Cupcake ",
    "price": 10.99,
    "image": "Resources/RV_Cupcake.jpg"
}, {
    "name": "Red Velvet Cupcake ",
    "price": 10.99,
    "image": "Resources/RV_Cupcake.jpg"

}, {
    "name": "Red Velvet Cupcake ",
    "price": 10.99,
    "image": "Resources/RV_Cupcake.jpg"
}, {
    "name": "Red Velvet Cupcake ",
    "price": 10.99,
    "image": "Resources/RV_Cupcake.jpg"

}

                 # Add more items as needed
                 ]

MAX_ITEMS_PER_PAGE = 6  # Number of items per page


def create_item_widgets(parent, items):
    row_num = 0
    col_num = 0
    # Iterate through the items and create widgets dynamically
    for item in items:
        # Load and resize the image
        img = Image.open(item["image"])
        img = img.resize((175, 175))
        img = ImageTk.PhotoImage(img)

        # Create and grid the widgets for the current item
        image_label = tk.Label(parent, image=img)
        image_label.grid(row=row_num, column=col_num, pady=30, padx=20)

        price_label = tk.Label(parent,
                               text=f"${item['price']:.2f}",
                               font=("Arial", 20))
        price_label.grid(row=row_num + 1, column=col_num)

        name_label = tk.Label(parent, text=item['name'], font=("Arial", 20))
        name_label.grid(row=row_num + 2, column=col_num)

        cart_button = tk.Button(parent,
                                text="Add to cart",
                                command=lambda tocart=item: addtocart(tocart))
        cart_button.grid(row=row_num + 3, column=col_num)

        # Store the image reference to prevent it from being garbage collected
        image_label.image = img

        # Move to the next row and reset column after every three columns
        col_num += 1
        if col_num >= 3:
            col_num = 0
            row_num += 4


def create_shopping_page(parent, page_number):
    start_index = (page_number - 1) * MAX_ITEMS_PER_PAGE
    end_index = start_index + MAX_ITEMS_PER_PAGE
    items_on_page = current_items[start_index:end_index]

    create_item_widgets(parent, items_on_page)


def navigate_to_next_page(current_page_label, page_number_label, frame,
                          current_page):
    new_page_number = current_page + 1
    current_page_label.config(text=f"Current Page: {new_page_number}")
    page_number_label.config(text=f"Page {new_page_number}")
    for widget in frame.winfo_children():
        widget.destroy()
    create_shopping_page(frame, new_page_number)


def navigate_to_previous_page(current_page_label, page_number_label, frame,
                              current_page):
    new_page_number = max(current_page - 1, 1)
    current_page_label.config(text=f"Current Page: {new_page_number}")
    page_number_label.config(text=f"Page {new_page_number}")
    for widget in frame.winfo_children():
        widget.destroy()
    create_shopping_page(frame, new_page_number)


def shopping_gui():
    global shopping_root
    shopping_root = tk.Tk()
    shopping_root.geometry("700x700")
    shopping_root.title("Shopping Page")

    checkout_button = tk.Button(shopping_root,
                                text=f"Checkout",
                                font="Arial",
                                command=Checkout)

    current_page = 1

    page_number_label = tk.Label(shopping_root,
                                 text=f"Page {current_page}",
                                 font=("Arial", 16))
    page_number_label.pack()

    current_page_label = tk.Label(shopping_root,
                                  text=f"Current Page: {current_page}",
                                  font=("Arial", 12))
    current_page_label.pack()

    frame = tk.Frame(shopping_root)
    frame.pack()

    create_shopping_page(frame, current_page)

    next_button = tk.Button(
        shopping_root,
        text="Next Page",
        command=lambda: navigate_to_next_page(
            current_page_label, page_number_label, frame, current_page))
    next_button.pack(side=tk.RIGHT, padx=10)

    prev_button = tk.Button(
        shopping_root,
        text="Previous Page",
        command=lambda: navigate_to_previous_page(
            current_page_label, page_number_label, frame, current_page))
    prev_button.pack(side=tk.LEFT, padx=10)

    checkout_button.pack(pady=10, padx=5)
    # Start the tkinter main loop
    shopping_root.mainloop()


def Ordercomplete():
    checkout_root.destroy()


def Checkout():

    def Removefromkart(e):
        selected_index = listbox.curselection()
        if selected_index:
            sub_from_total = current_cart[selected_index[0]]["price"]
            listbox.delete(selected_index)
            global total
            total = round(total - sub_from_total, 2)
            label3total.config(text="Your total is:"
                               " " + "$" + str(total))
            cart.pop(selected_index[0])
            current_cart.pop(selected_index[0])

    global checkout_root
    shopping_root.destroy()
    donut_emoji = "\U0001F369"
    checkout_root = tk.Tk()
    checkout_root.geometry("700x700")

    label = tk.Label(text=f"{donut_emoji} Your Cart {donut_emoji}", font=30)
    label.pack()

    label2 = tk.Label(text=f"Double click to remove an item from your cart",
                      font=10)
    label2.pack()

    label3total = tk.Label(text="Your total is:"
                           " " + "$" + str(total))
    label3total.pack()

    listbox = tk.Listbox(height=30, width=30)
    for item in cart:
        listbox.insert(tk.END, item)

    listbox.bind("<Double-1>", Removefromkart)
    listbox.pack()

    notext_label = tk.Label(text="")
    notext_label.pack(pady=5)

    address_label = tk.Label(
        text=f"Enter your address [eg. 1234 Main St, Apt 1, DC 12345]",
        font=10)
    address_label.pack(pady=5)
    global address_entry
    address_entry = tk.Entry(checkout_root, width=50)
    address_entry.insert(0, "")
    address_entry.pack(pady=5)

    buy_button = tk.Button(text="Buy", command=Ordercomplete)
    buy_button.pack()
    save_order_to_json()
    checkout_root.mainloop()


orders = {}
try:
    with open("orders.json", "r") as orders_file:
        orders = json.load(orders_file)
except FileNotFoundError:
    orders = {}


# Function to save the order information to a JSON file
def save_order_to_json():

    order_number = None
    setOfOrderNums = set()
    for order in orders:
        setOfOrderNums.add(order)

    while not order_number or order_number in setOfOrderNums:
        order_number = random.randint(1, 1000)
    orders[order_number] = [cart, "not delivered", address_entry.get()]

    with open("orders.json", "w") as orders_file:
        json.dump(orders, orders_file)
        #orders_file.write("\n")  # Add a newline to separate orders


username_entry = None
password_entry = None

# Create a dictionary to store user credentials (can be loaded from a JSON file)
verified_users = {}

# Load existing user data if the JSON file exists
try:
    with open("verified_users.json", "r") as file:
        verified_users = json.load(file)
except FileNotFoundError:
    verified_users = {}


def save_verified_users():
    # Save the user data to the JSON file
    with open("verified_users.json", "w") as file:
        json.dump(verified_users, file)


def Admin():
    root.destroy()
    print("Welcome back, Admin!")
    while True:
        print("\nAdmin Menu:")
        print("1. View Items in Stock")
        print("2. Remove an Item")
        print("3. Add an Item")
        print("4. View order status")
        print("5. Update order status")
        print("6. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            # Display items in stock
            print("\nItems in Stock:")
            for i, item in enumerate(current_items, 1):
                print(f"{i}. {item['name']} - ${item['price']:.2f}")

        elif choice == "2":
            # Remove an item
            item_name = input("Enter the name of the item to remove: ")
            for item in current_items:
                if item['name'] == item_name:
                    current_items.remove(item)
                    print(f"{item_name} removed from items in stock.")
                    break
            else:
                print(f"{item_name} not found in items in stock.")

        elif choice == "3":
            # Add an item
            item_name = input("Enter the name of the new item: ")
            item_price = float(input("Enter the price of the new item: "))
            item_image = input(
                "Enter image URL for the new item, if not leave it blank: ")
            if not item_image:
                default = "Resources/default_image.jpg"
            new_item = {
                "name": item_name,
                "price": item_price,
                "image": default
                # You can change the default image path
            }
            current_items.append(new_item)
            print(f"{item_name} added to items in stock.")

        elif choice == "4":
            order_number = input("Enter the order number: ")
            if order_number in orders:
                print(f"Items ordered:")
                for item in orders[order_number][0]:
                    print(item)
                print(f"Order status: {orders[order_number][1]}")
            else:
                print(f"Order number {order_number} not found.")

        elif choice == "5":
            order_number = input("Enter the order number: ")
            if order_number in orders:
                order_status = input(
                    "Enter the new order status (delivered/not delivered): ")
                orders[order_number][1] = order_status
                print(f"Order status updated to {order_status}.")
                with open("orders.json", "w") as orders_file:
                    json.dump(orders, orders_file)

            else:
                print(f"Order {order_number} not found.")

        elif choice == "6":
            print("Exiting Admin Menu")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")


def authenticate():
    entered_username = username_entry.get()
    entered_password = password_entry.get()
    message_label.config(text=" \u2716 Login unsuccessful, Please try again.")
    if entered_username == "Admin" and entered_password == "13579":
        Admin()
    elif entered_username in verified_users and verified_users[
            entered_username] == entered_password:
        # Successful login
        #Proceed to the shopping page or any other action you want here
        root.destroy()  # Close the login window
        shopping_gui()  # Open the shopping page


def sign_up():
    # Create a new window for the sign-up page
    sign_up_window = tk.Tk()
    sign_up_window.title("Sign Up")
    sign_up_window.geometry("700x700")

    # Labels and entry widgets for username and password
    username_label = tk.Label(sign_up_window,
                              text="Username",
                              font=("Times New Roman", 15))
    username_label.pack()
    username_entry = tk.Entry(sign_up_window, width=30)
    username_entry.pack()

    password_label = tk.Label(sign_up_window,
                              text="Password",
                              font=("Times New Roman", 15))
    password_label.pack()
    password_entry = tk.Entry(sign_up_window, width=30, show="*")
    password_entry.pack()

    def create_account():
        new_username = username_entry.get()
        new_password = password_entry.get()

        # Add the new user to the dictionary
        verified_users[
            new_username] = new_password  # stores the credentials in the json file
        save_verified_users()

        sign_up_window.destroy()  # Close the sign-up window

    sign_up_button = tk.Button(sign_up_window,
                               text="Sign Up",
                               command=create_account)
    sign_up_button.pack()

    # Start the tkinter main loop for the sign-up page
    sign_up_window.mainloop()


# Login Page
def Login():
    global username_entry, password_entry  # Declare these as global

    root.title("Login page")
    root.geometry("700x700")

    empty_label = tk.Label(root, pady=70)
    empty_label.pack()

    username_label = tk.Label(root,
                              text="Username",
                              font=("Times New Roman", 25))
    username_label.pack()

    username_entry = tk.Entry(root, width=50)
    username_entry.insert(0, "")
    username_entry.pack()

    password_label = tk.Label(root,
                              text="Password",
                              font=("Times New Roman", 25))
    password_label.pack()

    password_entry = tk.Entry(root, width=50, show="*")
    password_entry.insert(0, "")
    password_entry.pack()

    login_button = tk.Button(root,
                             text="Login",
                             command=authenticate,
                             width=10)
    login_button.pack(pady=5)

    global message_label
    message_label = tk.Label(
        root,
        text="",
    )
    message_label.pack()

    new_member_label = tk.Label(root,
                                text="Are you a new member, sign up below:")
    new_member_label.pack(pady=5)

    sign_up_button = tk.Button(root, text="Sign Up", command=sign_up,
                               width=10)  # Adds Sign Up button
    sign_up_button.pack(pady=3)

    empty_label = tk.Label(root, text="")
    empty_label.pack(pady=110)

    # admin_sign_label = tk.Label(root, text="Admins sign in here:")
    # admin_sign_label.pack(pady=5)

    # Start the tkinter main loop for the login page
    root.mainloop()


Login()


#font=("Times New Roman", 15)
