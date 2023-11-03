housepets = [
    {'animal': 'Dog: Maltese', 'owner': 'Jenny'},
    {'animal': 'Parrot: Budgerigar', 'owner': 'Mackenzel'},
    {'animal': 'Cat: Persian', 'owner': 'Avdol'},
    {'animal': 'Dog: Teacup', 'owner': 'Nathan'}
]

for housepet in housepets:
    animal, breed = housepet['animal'].split(': ')
    owner = housepet['owner']
    print(f"This housepet is a {animal} ({breed}).")
    print(f"Owner's name: {owner}\n")
