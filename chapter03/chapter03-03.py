# Chapter03-3
# 파이썬 리스트
# 자료구조에서 중요ㅕ
# 리스트 자료형( 순서 o, 순서 o, 수정 o, 삭제 o )

# 선언
a = []
b = list()
c = [ 70,75,80,85 ] # Len
print( len( c ) )
d = [ 1000,10000,'Ace','Base','Captain' ]
e = [ 100,1000, [ 'Ace','Base','Captain' ] ]
f = [ 21.42, 'foobar', 3, 4, False, 3.14159 ]


# 인덱싱
print( '>>>>>' )
print( f'd - {type( d )} : {d}' )
print( f'd - {d[ 1 ]}' )
print( f'd - {d[ 0 ] + d[ 1 ] + d[ 1 ]}' )
print( f'd - {d[ -1 ]}' )
print( f'e - {list( e[ -1 ][ 1 ] )}' )


# 슬라이싱
print( '>>>>>' )
print( f'd - {d[ 0 : 3 ]}' )
print( f'd - {d[ 2 : ]}' )
print( f'e - {e[ -1 ][ 1 : 3 ]}' )


# 리스트 연산
print( '>>>>>' )
print( f'c + d = { c + d }' )
print( f'c * 3 : { c * 3 }' )
print( f"'Test' + c[ 0 ] : {'Test' + str( c[ 0 ] )}" )

# 값 비교