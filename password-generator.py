# Imports
import random

# Program name
print('*****PASSWORD GENERATOR*****')

# Character source
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*().,?'

# Combined variable
chars = lowercase + uppercase + numbers + symbols

# Reading the number of passwords from the console and handling errors
success1 = False
while not success1:
    try:
        number = input('Enter the number of passwords to generate: ')
        number = int(number)
        success1 = True
    except ValueError:
        number = input('OOPS! YOU SHOULD ENTER ONLY POSITIVE NUMBER. TRY AGAIN...: ')
        number = int(number)
        success1 = True

# Reading the length of each password from the console and handling errors
success2 = False
while not success2:
    try:
        length = input('Password length: ')
        length = int(length)
        success2 = True
    except ValueError:
        length = input('OOPS! YOU SHOULD ENTER ONLY POSITIVE NUMBER. TRY AGAIN...: ')
        length = int(number)
        success2 = True

# Print result
print('Here are your passwords: ')

for i in range(number):
    passwords = ''
    for j in range(length):
        passwords += random.choice(chars)
    print(passwords)
