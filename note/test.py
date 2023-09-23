# Python3 샘플 코드 #

from urllib.parse import urlencode, quote_plus
import requests

# encoding : KS0VEcGhDJ5DvzTPii8dS7nQx2NnkjXENS%2FTqHorTk8%2F9gSneDrklBugS1%2BjeR8cfCRj%2Bv8QwZV2IrEcPUEJPA%3D%3D
# decoding : KS0VEcGhDJ5DvzTPii8dS7nQx2NnkjXENS/TqHorTk8/9gSneDrklBugS1+jeR8cfCRj+v8QwZV2IrEcPUEJPA==

key = requests.utils.unquote('KS0VEcGhDJ5DvzTPii8dS7nQx2NnkjXENS/TqHorTk8/9gSneDrklBugS1+jeR8cfCRj+v8QwZV2IrEcPUEJPA==')

url = 'http://apis.data.go.kr/1262000/CountryPopulationService2/getCountryPopulationList2'
params ={'serviceKey' : key, 'pageNo' : '1', 'numOfRows' : '10', 'cond[country_nm::EQ]' : '가나', 'cond[country_iso_alp2::EQ]' : 'GH', 'returnType' : 'XML' }

response = requests.get(url, params=params) # 결과값이 bytes로 반환된다?...

print(response.content)


