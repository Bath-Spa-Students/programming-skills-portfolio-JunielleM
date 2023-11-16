# Using def, To define a variable to be used as a new variable
def calculate_usb_sticks_and_change(usb_price, budget):
    usb_sticks = budget // usb_price
    change = budget % usb_price
    return usb_sticks, change

usb_price = 6
budget = 50

usb_sticks, change = calculate_usb_sticks_and_change(usb_price, budget)
# Print the variables with the functions
print("She can buy", usb_sticks, "USB_Sticks")
print("She will get $", change, "left")
