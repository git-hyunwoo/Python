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

print()

# %s
print('%10s' % ('nice')) # leave 10 spaces from left
print('{:>10}'.format('nice')) # leave 10 spaces from left

print('%-10s' % ('nice')) # leave 10 spaces from right
print('{:10}'.format('nice')) # leave 10 spaces from right

print('{:_>10}'.format('nice')) # leave 10 spaces from left with the charactor '_'
print('{:^10}'.format('nice')) # sort the string in the center between 10 spaces

print( '%.5s' % ( 'nice' ) ) # slice 5 letters from left
print( '%.5s' % ( 'pythonstudy' ) ) 
print( '{:10.5}'.format( 'pythonstudy' ) ) # make 10 spaces but slice only 5 letters


# %d
print( '%d %d' % ( 1,2 ) )
print( '{} {}'.format( 1,2 ) )

print( '%4d' % ( 42 ) )
print( '{:4d}'.format( 42 ) )

print()

# %f
print( '%1.8f' % ( 3.14343434343434 ) ) # 정수는 1자리, 소수는 8자리까지
print( '{:f}'.format( 3.14343434343434 ) )

print( '%06.2f' % ( 3.141592653589793 ) ) # 총 6개 중에서 정수부는 1개, 소수부는 2개
print( '{:06.2f}'.format( 3.141592653589793 ) )
