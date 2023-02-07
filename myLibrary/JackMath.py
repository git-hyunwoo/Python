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
    def optr( self, sentence ):
        
        flag = True
        while flag:
            
            if '*' in sentence or '/' in sentence or '+' in sentence or '-' in sentence:
                pass
            else:
                flag = False

        return sentence  





#==============================================


m = Math()
print( m.optr( '5+1*3/2' ) )


