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






#==============================================


m = Math()
print( m.sum( 1,2,3,4,5,6,7,8,9,10 ) )