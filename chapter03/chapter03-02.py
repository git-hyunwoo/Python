# Chapter03-2
# 파이썬 문자형
# 문자형 중요

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print( type( str1 ), type( str2 ), type( str3 ), type( str4 ) )
print( len( str1 ), len( str2 ), len( str3 ), len( str4 ) )

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print( type( str1_t1 ), len( str2_t2 ) )
print( type( str2_t2 ), len( str2_t2 ) )

# 참고 : Escape 코드
# 이스케이프 문자 사용
# \n : 개행
# \t : 탭
# \\ : 문자
# \' : 문자
# \" : 문자
# \000 : 널 문자
# I'm Boy

print( "I'm Boy" )
print( 'I\'am Boy' )
print( 'I\\am Boy' )

print( 'a \t b' ) # tab
print( 'a \"\" b' )

escape_str1 = "Do you have a \"retro games\"?"
print( escape_str1 )
escape_str2 = 'What\'s on TV?'
print( escape_str2 )

# 탭, 줄 바꿈
t_s1 = 'Click \t Start!'
t_s2 = 'New Line \n Check'
print( t_s1 )
print( t_s2 )
print()

# Raw String 
raw_s1 = r'D:\python\test' # r다음에 오는 것은 전부 문자열로 인식한다.

print( raw_s1 )

# 멀티라인 입력
# \를 넣으면 파이썬은 그 다음 라인에 변수를 바인딩 한다고 인식함( 중요!!! )
multi_str = \
'''
String
Multi line
Test
'''
print( multi_str )

# 문자열 연산
str_o1 = 'python'
str_o2 = 'Apple'
str_o3 = 'How are you doing?'
str_04 = 'Seiul Daejeon Busan Jinju'

print( str_o1 * 2 )
print( str_o1 + str_o2 )
print( 'y' in str_o1 )
print( 'z' in str_o1 )
print( 'P' not in str_o2 )

# 문자열 형변환
print( str( 66 ) , type( str( 66 ) ) )
print( str( 10.1 ) )
print( str( True ), type( str( True ) ) )

# 문자열 함수( upper, isalnum, startswith, count, endswith, isalpha... )

print( "Capitalize : ", str_o1.capitalize() )
print("endswith : ", str_o2.endswith('e'))
print('replace : ', str_o1.replace("thon",'Good'))
print('sorted : ', sorted(str_o1)) # return as list type with sorted 
print('split : ', str_04.split(' ')) # return as list type with splited by parameter

# sequence()
im_str = 'Good Boy!'

# dir() returns every attribute of parameter's type
print(dir(im_str)) # __iter__

# print
for i in im_str:
    print(i)

# 슬라이싱
# [ 시작 인덱스 : 끝 인덱스 : step ]
# 음수는 오른쪽 → 왼쪽
# 양수는 왼쪽 → 오른쪽
str_s1 = 'Nice Python'

print( len( str_s1 ) )
# 슬라이싱 연습
print( str_s1[ 0 : 3 ] ) # 마지막은 -1을 하므로 3 - 1까지의 인덱스까지만 나온다.
print( str_s1[ 5 : ] ) # 5번 째 인덱스부터 끝까지
print( str_s1[ : len( str_s1 ) ] ) # 처음부터 배열의 길이만큼의 인덱스 까지
print( str_s1[ 1 : 9 : 2 ] ) # 1번 째 인덱스퉈 9 - 1 인덱스까지 2칸씩 건너뛰어라
print( str_s1[ -5 : ] ) # -가 붙으면 끝에서부터 시작
print( str_s1[ 1 : -2 ] )
print( str_s1[ : : 2 ] )
print( str_s1[ : : -1 ] ) # 처음부터 끝까지 가는데 -1 ( 맨 마지막 )부터 시작해라, 즉 문자열이 뒤집힘

# 아스키 코드
a = 'z'

print( ord( a ) )  # ord : 문자 → 아스키 코드
print( chr( 122 ) ) # chr : 아스키 코드 → 문자
