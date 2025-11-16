import geo.utils as utils

# 직각삼각형 빗변 계산 예제
a, b = 3, 4
c = utils.pythagoras(a, b)
print('c =', c)  # 5.0 나와야 함

# 원의 면적 계산 예제
r = 10
area = utils.circle(r)
print('area =', area)  # 314.159... 나와야 함
