from random import choice
# Line hyphen -> \
# Block code
# Quotation (Quotations can be used for code comments)

quotation_1 = 'This is quotation!'
quotation_2 = "This is Ming's quotation!"
quotation_3 = '''We don't
talk
anymore
!!!
'''
print(quotation_1)
print(quotation_2)
print(quotation_3)

# Data type
'''
- Number
- String
- List
- Tuple
- Dictionary
'''

# Access memory address
memory_address = 10 
id(memory_address)

# The difference between del x and x=x+1 in memory

# Operator
'''
1. Arithmetic Operator
2. Assignment Operator
3. Bitwise Operator
4. Comparison Operator
5. Identity Operator
6. Logical Operator
7. Membership Operator
'''

# Operand

# For
x = [1, 2, 3]
xx = ('one', 'two', 'three')
xxx = range(10, 20)
for i in xxx:
    print(i)

# String
s = 'python'
chr(1)
repr(s)
str(s)

# => handle string
choice(s)
c = s.center(20, "-")
l = s.ljust(20, "-")
r = s.rjust(20, "-")
s.count('py')

# operator %
'''
%s => str -> str
%i => int -> int
%d => int -> str
%u => int -> str
%x => hex -> str
%e => exp -> str
%f => float -> str
'''
num = 12.3
print(type(num))
yNum = "%d" %(num)
print(type(yNum))

strName = 'This is text'
Num = 123
xText = 'Test %s %d' %(strName, Num)
print(xText)

# 
str1 = ['a', 'b']
str2 = [1, 2, 3]
str3 = str1 + str2
str4 = str1.extend(str2)
print(str3)
'''
=> The difference between str3 and str4 is that str4 does not generate memory addresses
'''

# Type
a = input('Type a number: ')
print(a)

# Hash
# hashable <=> unhashable(list, set, dict)

# Set type -> like list, tuple, (no duplicate, no order, not include mutable)