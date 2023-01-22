# Chapter02-1
# Basic Python
# How to use print()

print('Python Start!') # Recommended
print("Python Start!") # Recommended
print('''Python Start!''')
print("""Python Start!""")

print() 

# seperator option
# sep -> sperator which goes between every charactors
print('P','Y','T','H','O','N', sep='') # expected result : PYTHON
print('010','1234','5678',sep='-') # expected result : 010-1234-5678
print('python','google.com',sep='@') # expected result : python@google.com

print()

# end option
# end -> it set the last letter of String
print('Welcome to',end=' ')
print('IT News',end=' ')
print('Web Site')
# expected result : Welcome to IT News Web Site

# file option
import sys 

# sys.stdout : print in console
print('Learn Python', file=sys.stdout)
print()

# format ( d = 1,2,3..., s = 'Python' , f = 3.14653...)
print('%s %s' % ('one','two'))
print('{} {}'.format('one','two'))

print('{1} {0}'.format('one','two')) # expected result : two one

 


