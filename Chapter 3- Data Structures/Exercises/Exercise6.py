# A list of celebrities, while for loop
visita = ["Paul Walker", "Kobe Bryant","Stephen Hawking"]
for visitors in visita:
    print(f"Our guest of honor, {visitors},I'd like to publicly ask you to dinner so that we may discuss your thoughts on the current political and economic situation in the world.")
# Replace one of the celebrities with a new "variable"
excused_visitor = "Kobe Bryant"
print(f"My fellow guests,{excused_visitor} will be cancelling dinner due to circumstances going here and have been in an accident.")
# Replace the current visitor "Kobe Bryant" with a new variable "new_visitor"
new_visitor = "Mohammed Ali"
remove_guest = (excused_visitor)
add_guest = (new_visitor)
print(f"Dear {new_visitor}, I would like to invite you to dinner to discuss about boxing and the economical and political state of the world.")
print(new_visitor + ", I apologize for the inconvenience but you are not invited to the party.")
visitors = visita.pop(2)
print (visita)
for visitors in visita:
    print ("Honored guest, "+ visitors + " you are invited to dinner" )
del visita[1]
del visita[0]
print(visita, "Empty List")

