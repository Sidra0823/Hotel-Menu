# Define the menu of the restaurant
menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80,
    'Pao Bhaji': 120,
    'Dosa': 75,
    'Momo': 120,
    'Sandwich': 50,
}

# Greeting and Menu Display
print("Welcome to Sid Restaurant")
for item, price in menu.items():
    print(f"{item}: Rs{price}")

order_total = 0

while True:
    item = input("Enter the name of the item that you want to order: ")
    
    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added to your order.")
    else:
        print(f"Sorry, {item} is not available.")

    another_order = input("Do you want to add another item? (Yes/No): ").strip().lower()
    if another_order != "yes":
        break  # Exit the loop if the user doesn't want to add more items

print(f"The total amount to pay is Rs{order_total}")
