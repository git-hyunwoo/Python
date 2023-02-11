def hello():
    print( 'Hello Python' )

hello()

# Math class , written by Jack Snider
class Math():
    
    def __init__( self ):
        
        pass
    
    # 더하기 함수
    def sum( self , *numbers ):
        
        # parameter is variable factor( 가변인수 )
        
        total = 0  
        for number in numbers:
            total += number

        return total
        
 

    # +,-,*,/ operator
    def optr( self, stnc ):

        lst = []
        tmp = ''
        for i in range( 0, len( stnc ) ):
            if stnc[ i ] != '*' and stnc[ i ] != '/' and stnc[ i ] != '+' and stnc[ i ] != '-':
                
                tmp += stnc[ i ]
                if i == len( stnc ) - 1:
                    lst.append( tmp )
            else:
                lst.append( tmp )
                lst.append( stnc[ i ] )
                tmp = ''

        #-============ 데이터 정제 완료 -============

        order = 0 # 연산 순서

        for x in lst:
            if x == '*' or x == '/':
                if x == '*':
                    order += 1
                    print( f'{ order } : *' )
                    where = lst.index( x )
                    prv = where - 1
                    print( f'prv : {prv}' )
                    nxt = where + 1
                    print( f'nxt : {nxt}' )
                    print( f'{prv}{x}{nxt}' )
                    tmp = int( lst[ prv ] ) * int( lst[ nxt ] )
                    lst[ where ] = tmp
                    lst.pop( prv )
                    lst.pop( nxt - 1 )
                    
                elif x == '/':
                    order += 1
                    print( f'{ order } : /' )
                    where = lst.index( x )
                    prv = where - 1
                    print( f'prv : {prv}' )
                    nxt = where + 1
                    print( f'nxt : {nxt}' )
                    print( f'{prv}{x}{nxt}' )
                    tmp = int( lst[ prv ] ) / int( lst[ nxt ] )
                    lst[ where ] = int( tmp )
                    lst.pop( prv )
                    lst.pop( nxt - 1 )
        
        answer = 0
        for y in lst:
            tmp = 0
            if y == '+' or y == '-':
                if y == '+':
                    order += 1
                    print( f'{ order } : +' )
                elif y == '-':
                    order += 1
                    print( f'{ order } : -' )
                  

        return lst







#==============================================


m = Math()
print( m.optr( '5/5+4*6-2' ) )

#print( '5/5*+4/6*'.index( '*' ) )
