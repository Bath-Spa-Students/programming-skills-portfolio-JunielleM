message = "And, How old are you?"
message +="\nEnter 'quit' when you are done paying: "
#while loop
while True:
    age = input(message)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("You are free to watch the movie!")
    elif age < 13:
        print("10$ for the movie ticket.")
    else:
        print("The ticket is 15$, sir.")