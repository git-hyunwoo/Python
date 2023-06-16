class Stock():

  def __init__( self, name = 'None', invest_amount = 0, price = 0, percent = 0, term = 0, year = 0 ):

    """
    name : 종목이름
    invest_amount : 투자금
    price : 1주당 가격
    percent : 배당률( 연 )
    term : 배당주기( 1개월, 4개월 ... )
    year : 몇년 동안 투자할 것인지
    """
    
    self.name = name
    self.invest_amount = invest_amount
    self.price = price
    self.percent = percent
    self.term = term
    self.year = year

  def __str__( self ):
    return f'{ self.name }'

  def calculate( self ):

    """
    어떤 종목에 얼마를 몇퍼센트 배당률로 몇년간 투자하해야 얼마의 수익을 얻는가?
    """
    reward = 0
    
    if self.percent >= 1:
      self.percent = self.percent / 100
    
    
    if self.year == 0:
      return '투자기간은 0년이 될 수 없습니다.'

    # 투자금으로 살 수 있는 주식 갯수
    stocks = ( int ) ( self.invest_amount / self.price )

    # 투자할 기간 X 연당 배당 횟수 = 투자기간동안 받을 총 배당 횟수
    round = self.year * self.term

    for _ in range( 1, round + 1 ):

      per_interest = ( self.invest_amount * self.percent ) / self.term # ( 투자금 * 연 배당률 ) / 연당 배당 횟수 = 한 배당 회차당 받는 금액

      # 투자금 + per_interest 

      # stocks = ( int ) ( self.invest_amount / self.price ) → 이자가 쌓여서 주식을 살 수 있으면 계속 산다.

apple = Stock( )

    