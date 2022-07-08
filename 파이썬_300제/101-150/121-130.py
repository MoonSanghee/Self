121-130

# 121
# user = input("")
# if user.islower():
#     print(user.upper())
# else:
#     print(user.lower())

# 122
# score = input("score: ")
# score = int(score)
# if 81 <= score <= 100:
#     print("grade is A")
# elif 61 <= score <= 80:
#     print("grade is B")
# elif 41 <= score <= 60:
#     print("grade is C")
# elif 21 <= score <= 40:
#     print("grade is D")
# else:
#     print("grade is E")

# # 123
# 환율 = {"달러": 1167, 
#         "엔": 1.096, 
#         "유로": 1268, 
#         "위안": 171}
# user = input("입력: ")
# num, currency = user.split()
# print(float(num) * 환율[currency], "원")
# or
# a = input('입력: ')
# b = a.split()
# x, y = b
# x = float(x)
# if y == '달러':
#     print(x*1167)
# elif y == '엔':
#     print(x*10.96)
# elif y == '유로':
#     print(x*1268)
# else:
#     print(x*171)

# 124
# num1 = input("input number1: ")
# num2 = input("input number2: ")
# num3 = input("input number3: ")
# num1 = int(num1)
# num2 = int(num2)
# num3 = int(num3)

# if num1 >= num2 and num1 >= num3:
#     print(num1)
# elif num2 >= num1 and num2 >= num3:
#     print(num2)
# else:
#     print(num3)

# 125
# number = input("휴대전화 번호 입력: ")
# num = number.split("-")[0]
# if num == "011":
#     com = "SKT"
# elif num == "016":
#     com = "KT"
# elif num == "019":
#     com = "LGU"
# else:
#     com = "알수없음"
# print(f"당신은 {com} 사용자입니다.")

# 126
# a = input('입력: ')
# b = a[2:3:]
# print(b)
# if b in ['0', '1', '2']:
#     print('강북구')
# elif b in ['3', '4', '5']:
#     print('도봉구')
# else:
#     print('노원구')

# 127
# a = input('입력: ')
# b = a[:-6]
# print(b)
# if b in ['1', '3']:
#     print('남자')
# else:
#     print('여자')

# 128
# a = input('입력: ')
# a = a.split('-')[1]
# if 0 <= int(a[1:3]) <= 8:
#     print('서울입니다.')
# else:
#     print('서울이 아닙니다.')

# 129
# data = input('주민등록번호: ')
# data = data.replace('-', '')
# 계산1 = int(data[0]) * 2 + int(data[1]) * 3 + int(data[2]) * 4 + int(data[3]) * 5 + int(data[4]) * 6 + int(data[5]) * 7 + int(data[6]) * 8 + int(data[7]) * 9 + int(data[8]) * 2 + int(data[9]) * 3 + int(data[10]) * 4 + int(data[11]) * 5
# 계산1 = 계산1 % 11
# 계산2 = 11 - 계산1
# 계산2 = str(계산2)

# if data[-1] == 계산2[-1]:
#     print('유효한 주민등록번호입니다.')
# else:
#     print('유효하지 않은 주민등록번호입니다')

# 130
# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

# 변동폭 = float(btc['max_price']) - float(btc['min_price'])
# 시가 = float(btc['opening_price'])
# 최고가 = float(btc['max_price'])

# if (시가+변동폭) > 최고가:
#     print("상승장")
# else:
#     print("하락장")