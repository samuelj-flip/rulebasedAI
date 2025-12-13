# Simple AI Cashier
print("Welcome to FastFood AI! I am your cashier today.")

menu = {
    "burger": 5,
    "fries": 2,
    "cola": 1.5,
    "nuggets": 4
}

order = {}
total = 0

while True:
    print("\nMenu:", menu)
    item = input("What would you like to order? (type 'done' when finished): ").lower()
    
    if item == "done":
        break
    elif item in menu:
        qty = input(f"How many {item}s would you like? ")
        if qty.isdigit():
            qty = int(qty)
            order[item] = order.get(item, 0) + qty
            total += menu[item] * qty
            print(f"Added {qty} {item}(s) to your order.")
        else:
            print("Please enter a valid number.")
    else:
        print("Sorry, we don't have that item.")

print("\nYour order summary:")
for item, qty in order.items():
    print(f"{item.capitalize()}: {qty} x ${menu[item]} = ${qty * menu[item]}")

print(f"Total: ${total}")

while True:
    payment = input("Enter your payment amount: $")
    try:
        payment = float(payment)
        if payment >= total:
            change = payment - total
            print(f"Payment accepted. Your change is ${change:.2f}. Thank you!")
            break
        else:
            print("Insufficient payment. Please pay the full amount.")
    except ValueError:
        print("Please enter a valid amount.")
