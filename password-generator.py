import random

print('*****Password Generator*****')

# Character source
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*().,?'

# Combined variable
chars = lowercase + uppercase + numbers + symbols

#def is_int(n):
#    if isinstance(n, int):
#        print(True)
#    else:
#        print(False)

# How many passwords should program generate
number = input('Amount of passwords to generate: ')
# Convert string to integer
number = int(number)

# Length of each password
length = input('Password length: ')
# Convert string to integer
length = int(length)

# Print result
print('Here are your passwords: ')

for i in range(number):
    passwords = ''
    for j in range(length):
        passwords += random.choice(chars)
    print(passwords)
