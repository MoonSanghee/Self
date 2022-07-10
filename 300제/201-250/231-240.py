# 231-240

# 231
# Q. 아래 코드를 실행한 결과를 예상하라.
# def n_plus_1 (n) :
#     result = n + 1

# n_plus_1(3)
# print (result)

# A.
# 에러가 발생합니다.
# NameError Traceback (most recent call last)
# <ipython-input-2-78e20c8ecef0> in <module>()
# 3 
# 4 n_plus_1(3)
# ----> 5 print (result)
# 6
# NameError: name 'result' is not define
# 함수 내부에서 사용한 변수는 함수 밖에서는 접근이 불가능합니다.
# 함수 내부에서 계산한 값을 전달하기 위해서는 return을 사용해야 합니다.

# 232
# Q. 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
# make_url("naver")
# www.naver.com

# def make_url(a):
#     b = 'www.'+a+'.com'
#     return b

# 233
# Q. 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.
# make_list("abcd")
# ['a', 'b', 'c', 'd']

# A1.
# def make_list(a):
#     b =[]
#     for i in a:
#         b.append(i)
#     return b
# A2.
# def make_list (string) :
#     return list(string)

# 234
# Q. 숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.
# pickup_even([3, 4, 5, 6, 7, 8])
# [4, 6, 8]

# def pickup_even(a):
#     b = []
#     for i in a:
#         if i % 2 == 0:
#             b.append(i)
#     return b

# 235
# Q. 콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하라.
# convert_int("1,234,567")
# 1234567

# def convert_int(a):
#     return int(a.replace(',', ''))

# 236
# Q. 아래 코드의 실행 결과를 예측하라.
# def 함수(num) :
#     return num + 4

# a = 함수(10)
# b = 함수(a)
# c = 함수(b)
# print(c)

# A.
# 22

# 237
# Q. 아래 코드의 실행 결과를 예측하라.
# def 함수(num) :
#     return num + 4

# c = 함수(함수(함수(10)))
# print(c)

# A.
# 22

# 238
# Q. 아래 코드의 실행 결과를 예측하라.
# def 함수1(num) :
#     return num + 4
# def 함수2(num) :
#     return num * 10

# a = 함수1(10)
# c = 함수2(a)
# print(c)

# A.
# a 부터 실행이 되어 함수1의 num 자리에 10이 바인딩되어 14라는 값이 도출되고 
# c의 a 자리에 14라는 값이 들어가 함수 2의 num 자리에 바인딩되어 140이 도출됨.


# 239
# Q. 아래 코드의 실행 결과를 예측하라.
# def 함수1(num) :
#     return num + 4
# def 함수2(num) :
#     num = num + 2
#     return 함수1(num)
# c = 함수2(10)
# print(c)

# A.
# 함수2(num)의 num 자리에 10이 바인딩 되고 12라는 값을 도출 한 후 함수 1의 num 자리에 12가 바인딩되어 16이 최종적으로 도출됨.

# 240
# Q. 아래 코드의 실행 결과를 예측하라.
# def 함수0(num) :
#     return num * 2
# def 함수1(num) :
#     return 함수0(num + 2)
# def 함수2(num) :
#     num = num + 10
#     return 함수1(num)

# c = 함수2(2)
# print(c)

# A.
28