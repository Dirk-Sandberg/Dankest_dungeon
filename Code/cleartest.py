import os
def clear():
    name = os.name
    if name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

clear()
