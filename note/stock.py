from bs4 import BeautifulSoup
import urllib.request as req

# HTML 가져오기
url = "http://finance.naver.com/marketindex/"
res = req.urlopen(url)

# HTML 분석하기
soup = BeautifulSoup(res, "html.parser")

#원하는 데이터 추출하기
price = soup.select_one("div.head_info > span.value").string
price = price.replace( ',','' )
dollar = ''


print("usd/krw = ", price)	


for letter in price:
	if letter == '.':
		break
	dollar += letter

dollar = int( dollar ) 

print( dollar )
 
data = [
 	
 	{
 		'name' : 'Apple',
 		'price' : 152.93,
 		'interest' : 0.006, # 0.6%
 		'period' : 3
 	},
 	
 	{
 		'name' : 'Lockheed Martin',
 		'price' : 480.18,
 		'interest' : 0.0237,
 		'period' : 3
 	},
 	
 	{
 		'name' : 'Raytheon Technologies',
 		'price' : 101.40,
 		'interest' : 0.0213,
 		'period' : 3
 	},
 	
 	{
 		'name' : 'Altria',
 		'price' : 47.33,
 		'interest' : 0.0776,
 		'period' : 3
 	},
 	
 	{
 		'name' : 'OneOk',
 		'price' : 68.76,
 		'interest' : 0.0536,
 		'period' : 3
 	},
 	
 	{
 		'name' : 'Nike',
 		'price' : 125.43,
 		'interest' : 0.0099,
 		'period' : 3
 	},
 	
 	{
 		'name' : 'Realty Income',
 		'price' : 65.75,
 		'interest' : 0.0449,
 		'period' : 1
 	},
 	
 	{
 		'name' : 'Coca Cola',
 		'price' : 59.35,
 		'interest' : 0.0292,
 		'period' : 3
 	},
 	
 	{
 		'name' : 'Chevron',
 		'price' : 168.80,
 		'interest' : 0.033,
 		'period' : 3
 	},
 	
 	{
 		'name' : 'Pfizer',
 		'price' : 43.47,
 		'interest' : 0.0368,
 		'period' : 3
 	},
 		
]
year = 10
daily_invest = 2000
total = 0
origin = 0
# which stock
for stock in data:
	sum = 0
	payed_interest = 0
	print( f'==================== {stock[ "name" ]} =====================' )
	# for how many years ( count with day : 365 )
	for day in range( 1, year * 365 + 1 ):
		
		sum += daily_invest
		origin += daily_invest

		# with how much period
		if day % ( stock[ 'period' ] * 30 ) == 0:
			payed_interest += 1
			sum += ( sum * stock[ 'interest' ]   ) / ( 12 / stock[ 'period'] )
			#print( f'INTEREST : {sum * stock[ "interest" ]}')
		
		if day % 365 == 0:
			print( f'{int(day / 365)} year : {int( sum )}won | ${int( sum / dollar )}' )
			
	total += sum

print( '=========================================' )
print( f'ORIGIN : {int( origin )}won | ${int( origin / dollar )}')
print( f'INVEST : {int( total )}won | ${int( total / dollar )}')
	

