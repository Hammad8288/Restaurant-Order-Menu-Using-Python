# Restaurant Menu (item: price in Rs)
menu = {
    'Samosa': 20,
    'Burger': 90,
    'Pizza': 100,
    'Pasta': 80,
    'Spring Rolls': 30,
    'Ice Cream': 50,
    'Fruit Salad': 60,
    'Chocolate Cake': 80
}

# Show menu
print ("Welcome to the Restaurant!")
print ("Here is the menu:\n ")

for item , price in menu.items():
    print (f"{item}: Rs {price}")
    
# Initialize order list and total cost
order = {}

while True:
    #take order from the user
    item = input ("Enter item name you want to order (or 'done' to finish): ").title()
    
    if item.lower() == 'done':
        break
    elif item not in menu:
        print("❌ Sorry, item not available. Try again.")
        continue
    
    try:
        quantity = int(input (f"Enter quantity of {item}: "))
    except ValueError:
        print("❌ Invalid quantity. Please enter a valid number.")
        continue
    
    if item in order:
        order[item] += quantity
        print(f"Updated quantity of {item} in your order.")
    else:
        order[item] = quantity
        print(f"{item} Added to your order.")
        
# Calculate total cost of order 
print("\nOrder Summary: ")
total_cost = 0
for item, quantity in order.items():
    cost = menu[item] * quantity
    print(f"{item}: {quantity} x Rs {menu[item]} = Rs {cost}")
    total_cost += cost
    
print(f"\nTotal cost: Rs {total_cost}")
print("Thank you for your order! Enjoy your meal!")
print("If you have any questions, feel free to ask our staff.")