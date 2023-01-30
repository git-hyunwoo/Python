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

# id( identity ) confirm

m = 800
n = 655

print( id( m ) )
print( id( n ) )
print( id( m ) == id( n ) ) # False
print()

# refer the same object
m = 800
n = 800
z = 800
i = 800
print( id( m ) )
print( id( n ) )
print( id( m ) == id( n ) ) # True
print()

# various definition of variable
# Camel Case : numberOfCollegeGraduates
# Pascal Case : NumberOfCollegeGraduates
# Snake Case : number_of_college_graduates

# allowed way of definite variable
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 7

# reserved words are not allowed to definite as varaibles
# for = 3 -> error
# class = 3 -> error

