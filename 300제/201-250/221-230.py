# 221-230

# 221
# Q. 입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의하라.
# ex)
# print_reverse("python")
# nohtyp

# def print_reverse(문자열):
#     print(문자열[::-1])

# 222
# Q. 성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 정의하라.
# ex)
# print_score ([1, 2, 3])
# 2.0

# def print_score(a):
#     print(sum(a)/len(a))

# 223
# Q. 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.
# ex)
# print_even ([1, 3, 2, 10, 12, 11, 15])
# 2
# 10
# 12

# def print_even(a):
#     for i in a:
#         if i % 2 == 0:
#             print(i)

# 224
# Q. 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.
# ex)
# print_keys ({"이름":"김말똥", "나이":30, "성별":0})
# 이름
# 나이
# 성별

# def print_keys(a):
#     for b in a.keys():
#         print(b)

# 225
# Q.
# my_dict에는 날짜를 키값으로 OHLC가 리스트로 저장돼 있다.
# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}
# my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의하라.
# print_value_by_key  (my_dict, "10/26")
# [100, 130, 100, 100]

# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}
# def print_value_by_key(a, b):
#     print(a[b])

# 226
# Q. 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.
# print_5xn("아이엠어보이유알어걸")
# 아이엠어보
# 이유알어걸

# def print_5xn(a):
#     b = int(len(a)/5)
#     for c in range(b+1):
#         print(a[c*5: c*5+5])

# 227
# Q. 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.
# printmxn("아이엠어보이유알어걸", 3)
# 아이엠
# 어보이
# 유알어
# 걸

# def printmxn(a, b):
#     a1 = int(len(a)/b)
#     for a2 in range(a1+1):
#         print(a[a2*b: a2*b+b])

# 228
# Q. 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라. 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.
# calc_monthly_salary(12000000)
# 1000000

# def calc_monthly_salary(a):
#     print(int(a/12))

# 229
# Q.아래 코드의 실행 결과를 예측하라.
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)

# my_print(a=100, b=200)

# A.
# 왼쪽: 100
# 오른쪽: 200

# 230
# Q. 아래 코드의 실행 결과를 예측하라.
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)

# my_print(b=100, a=200)

# A.
# 왼쪽: 200
# 오른쪽: 100