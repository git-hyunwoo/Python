# Python3 샘플 코드 #


import requests

url = 'http://apis.data.go.kr/1262000/CountryPopulationService2/getCountryPopulationList2'
params ={'serviceKey' : '서비스키', 'pageNo' : '1', 'numOfRows' : '10', 'cond[country_nm::EQ]' : '가나', 'cond[country_iso_alp2::EQ]' : 'GH', 'returnType' : 'JSON' }

response = requests.get(url, params=params)
print(f'a : {response.content}')