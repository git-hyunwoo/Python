# Chapter03-01
# Numeric

# int : 정수
# float : 실수
# complex : 복소수
# bool : 불린
# str : 문자열( 시퀸스 )
# list : 리스트( 시퀸스 )
# tuple : 튜플( 시퀸스 )
# set : 집합
# dict : 사전

# data type
str1 = 'Python'
bool = True
str2 = 'Anaconda'
float = 10.0 # 10 == 10.0 False
int = 7
list = [ str1, str2 ] # length can be infinite
dict = {
    "name": "Machine Learning",
    "version": 2.0
}

tuple = ( 7,8,9 ) # 괄호 없이 선언해도 튜플로 인식
set = { 3,5,7 }

# print data type
print( type( str1 ) )
print( type( bool ) )
print( type( str2 ) )
print( type( float ) )
print( type( int ) )
print( type( dict ) )
print( type( tuple ) )
print( type( set ) )


# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
power(x,y) : x의 y제곱 ( x ** y 로 해도 같은 결과 )

"""

# 정수 선언
i = 77
i2 = -14
big_int = 7777777777777999999999999999

# 정수 출력
print( i )
print( i2 )
print( big_int )
print()

# 실수 출력
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

# 실수 출력
print( f )
print( f2 )
print( f3 )
print( f4 )

# 연산 실습
i1 = 39
i2 = 939
big_int1 = 10000000000000000000000
big_int2 = 16546461321684613213854
f1 = 1.234
f2 = 3.939

# +
print( " >>>>> + " )
print( "i1 + i2 : ", i1 + i2 )
print( "f1 + f2 : ", f1 + f2 )
print( "big_int1 + big_int2 : ", big_int1 + big_int2 )

# *
print( " >>>>> * " )
print( "i1 + i2 : ", i1 * i2 )
print( "f1 + f2 : ", f1 * f2 )
print( "big_int1 + big_int2 : ", big_int1 * big_int2 )
