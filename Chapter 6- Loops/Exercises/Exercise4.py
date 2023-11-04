#Flavors
sandwiches = ["Zinger", "Extra-cheese", "Egg&Mayo", "Shawarma", "Adobo"]


finished_sandwiches = []

# Ask the user for sandwich orders
while True:
    sandwich_order = input("Enter a sandwich type (or 'quit' to finish): ")

    if sandwich_order.lower() == 'quit':
        break  # Exit the loop if 'quit' is entered

    if sandwich_order in sandwiches:
        finished_sandwiches.append(sandwich_order)
        print(f"{sandwich_order} acquired!")
    else:
        print("Sorry, we don't have that sandwich option.")

# Print the list of finished sandwiches
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
