# combining strings with +
# 'DS830' + "DM857"
print('DS830'+ "DM830")
-> DS830DM857


# The second string starts with ' but ends with ".
print('DS830'+'DM857")
# -> SyntaxError


# Quotes have to match
print('This is the way' the Mandalorian)
# -> yntaxError: invalid syntax. Perhaps you forgot a comma?


print("\ 'the Mandalorian\' is boring!")
# -> \ 'the Mandalorian' is boring!


print("yes\maybe")
# -> yes\maybe


print("yes\no")
# -> yes
# o


print('yes\no")
# -> SyntaxError: unterminated string literal (detected at line 1)


print('yes
no')
# -> SyntaxError: unterminated string literal (detected at line 1)
 

print('''yes
no''')
# ->       
# yes
# no

print(3+'rabbits')
# -> TypeError: unsupported operand type(s) for +: 'int' and 'str'


print(int(3)+'rabbits')
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


print(str(3)+'rabbits')
# 3rabbits


print(3*'rabbits')
# rabbitsrabbitsrabbits

 
print(int(3)*'rabbits')
# rabbitsrabbitsrabbits

      
print(str(3)*'rabbits')
# TypeError: can't multiply sequence by non-int of type 'str'

      
