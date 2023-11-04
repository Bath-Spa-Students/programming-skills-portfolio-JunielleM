toppings = ["Cheesy", "Hawaiian", "Pepperoni", "Double-Cheeseburger", "Mushroom"]

while True:
    pizza = input("Enter a pizza topping (or 'quit' to finish): ")
    
    if pizza.lower() == 'quit':
        break  # When 'quit' is entered, it breaks the loop
    
    toppings.append(pizza)
    print(f"You'll add {pizza} to your pizza.")

print("Your pizza will have the following toppings:")
for topping in toppings:
    print(topping)

text = "\nWould you like toppings on that pizza??"
text += "\nEnter 'quit' when you are done ordering: "

while True:
    topping = input(text)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break
