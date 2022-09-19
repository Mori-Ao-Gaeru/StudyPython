import string

def cipher(a_string, key):
#    uppercase = string.ascii_uppercase
#    lowercase = string.ascii_lowercase
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopwrstuvwxyz'
    encrypt = ''
    for c in a_string:
        if c in uppercase:
            new = (uppercase.index(c) + key) % 26
            encrypt += uppercase[new]
        elif c in lowercase:
            new = (lowercase.index(c) + key) % 26
            encrypt += lowercase[new]
        else:
            encrypt += c
    return encrypt

a = input('Please input a sentense before encrypt:\n')
print('encrypted: ' + cipher(a , 3))
print('original : ' + cipher(cipher(a, 3), 23))
