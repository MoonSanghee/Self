# 211-220

# 211
# Q. 함수의 호출 결과를 예측하라.
# def 함수(문자열) :
#     print(문자열)
# 함수("안녕")
# 함수("Hi")

# A.
# 안녕
# Hi

# 212
# Q. 함수의 호출 결과를 예측하라.
# def 함수(a, b) :
#     print(a + b)
# 함수(3, 4)
# 함수(7, 8)

# A.
# 7
# 15

# 213
# Q.아래와 같은 에러가 발생하는 원인을 설명하라.
# def 함수(문자열) :
#     print(문자열)

# 함수()
# TypeError: 함수() missing 1 required positional argument: '문자열'

# A.
# 함수에 정의와 다르게 함수를 호출하고 있다. 함수를 호출할 때 하나의 파라미터를 입력해야한다.

# 214
# Q.아래와 같은 에러가 발생하는 원인을 설명하라.
# def 함수(a, b) :
#     print(a + b)
# 함수("안녕", 3)
# TypeError: must be str, not int

# A.
# "안녕"이란 문자열은 숫자와 덧셈을 할 수가 없음.

# 215
# Q. 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.
# def print_with_smile(문자열):
#     print(문자열 + ":D" )
 
# 216
# Q. 215에서 정의한 함수를 호출하라. 파라미터는 "안녕하세요"로 입력하라.

# A. print_with_smile("안녕하세요")

# 217
# Q. 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.

# A.
# def print_upper_price(a):
#     print(a*1.3)

# 218
# Q. 두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라.

# A.
# def print_sum(a, b):
#     print(a + b)

# 219
# Q. 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.
# ex)
# print_arithmetic_operation(3, 4)
# 3 + 4 = 7
# 3 - 4 = -1
# 3 * 4 = 12
# 3 / 4 = 0.75
# A1.
# def print_arithmetic_operation(a, b):
#     print(a, '+', b, '=', a + b)
#     print(a, '-', b, '=', a - b)
#     print(a, '*', b, '=', a * b)
#     print(a, '/', b, '=', a / b)
# A2.
# def print_arithmetic_operation(a, b):
#     print('{} + {} = {}'.format(a, b, a + b))
#     print('{} - {} = {}'.format(a, b, a - b))
#     print('{} * {} = {}'.format(a, b, a * b))
#     print('{} / {} = {}'.format(a, b, a / b))

# 220
# 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.

# def print_max(a, b, c):
#     if a > b and a > c:
#         print(a)
#     elif b > a and b > c:
#         print(b)
#     else:
#         print(c)
