#The List of sandwiches
sandwich_orders = ["Zinger", "pastrami", "Extra-cheese", "Egg&Mayo", "Shawarma","Adobo" ]

finished_sandwiches = []

# Check if 'pastrami' is in the list, and if so, remove it
if 'pastrami' in sandwich_orders:
    print("Sorry, we're out of pastrami sandwiches.")
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')

# Ask the user for orders
while True:
    sandwich_order = input("Enter to order your sandwich!(or 'quit' to finish): ")

    if sandwich_order.lower() == 'quit':
        break  # Exit the loop if 'quit'

    if sandwich_order in sandwich_orders:
        finished_sandwiches.append(sandwich_order)
        print(f"{sandwich_order} acquired!")
    else:
        print("Sorry, we don't have that sandwich option.")

# Print the list of finished sandwiches
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
