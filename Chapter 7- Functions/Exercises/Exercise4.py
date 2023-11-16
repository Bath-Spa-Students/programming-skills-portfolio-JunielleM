# Defining a variable to make a shirt
def make_shirt(size, message):
    summary = f"You are making a {size}-sized shirt with the message: '{message}'."
    print(summary)

make_shirt("large", "I love Python!")


make_shirt(size="medium", message="No way, you love coding?")
