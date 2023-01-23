#chapter 02-02
# Python basic
# Python variable

# basic definition
n = 700

# print
print( n )
print( type( n ) ) # type() shows you the type of data
print()

# multiple definition
x = y = z = 700
print( x,y,z )
print()

# definition
var = 75

# re-definition
var = "Change Value"

# print
print( var )
print( type( var ) )

# Object Reference
# when the variable is assigned

# 1. create object for type
# 2. create value
# 3. print on console

# ex_01)
print( 300 )
print( int( 300 ) )

# ex_02)
# n -> 777
n = 777

print( n, type( n ) )
print()

m = n
# m -> 777 <- n

print( m, n )
print( type( m ), type( n ) )
print()

m = 400

print( m, n )
print( type( m ), type( n ) )
print()