# Print the glossary with the definition of the topics you learned
glossary = {
    'function': 'A block of code that can work when assigned.',
    'variable': 'A variable is an information that stores codes inside the program.',
    'input': 'Input is a function where it converts it into a string so that it can be interacted while using code',
    'statements': 'Instructions that are waiting to be executed',
    'string': 'A string is one of the foundations of characters'
}

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)
