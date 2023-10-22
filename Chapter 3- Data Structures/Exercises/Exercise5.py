import random
# Our list of celebrities
visitors = ["Paul Walker", "Kobe Bryant", "Stephen Hawking"]

# The main while loop continues until only two guests are left
while len(visitors) > 2:
    # Randomly select a guest to invite
    guest_to_invite = random.choice(visitors)

    # Remove the selected guest from the list
    visitors.remove(guest_to_invite)

    # Print a message to the selected guest
    print(f"Our guest of honor, {guest_to_invite}, I'd like to publicly ask you to dinner so that we may discuss your thoughts on the current political and economic situation in the world.")

# The loop now iterates through the remaining two guests and sends them a dinner invitation
for visitor in visitors:
    print(f"Dear {visitor}, I would like to invite you to dinner to discuss about your professional experiences and the economical and political state of the world.")