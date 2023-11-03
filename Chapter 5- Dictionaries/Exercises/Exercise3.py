glossary = {
    'function': 'A block of code that can work when assigned.',
    'variable': 'A variable is an information that stores codes inside the program.',
    'input': 'Input is a function where it converts it into a string so that it can be interacted while using code',
    'statements': 'Instructions that are waiting to be executed',
    'string': 'A string is one of the foundations of characters',
    'comment': 'A note that will guide you but it will not execute since it is not a code',
    'print': 'It is a function that will print the texts',
    'import': 'Import makes a keyword to make the code available in other areas of Python',
    'time': 'returns the time as a floating point number expressed in seconds',
    'float': 'float converts values into floating point numbers such as fractional numbers or integers'
}

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)