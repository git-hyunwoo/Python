"""
a원의 x%가 증가했더니 b원이 됬다.

1. a + (a * x) = b
2. a * x = b - a

28680
28577
1000 * x = 1200 - 1000

매수값 * x = 매도값 - 매수값

a = 매도값 - 매수값
x  = a / 매수값
"""
def profit_percent(buy,sell):
    a = sell - buy
    b = a / buy
    return round((b * 100),2)

print(profit_percent(12900,12965))