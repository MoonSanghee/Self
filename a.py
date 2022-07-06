#001
#print("hello world")

#002
#print("Mary's cosmetics")

#003
#print('신씨가 소리질렀다. "도둑이야"')

#004
#print("C:\\Windows")

#005
#print("안녕하세요.\n만나서\t\t반갑습니다.")

#006
#print("오늘은","월요일")

#007
#print("naver", "kakao", "sk", "samsung", sep=";")

#008
#print("naver", "kakao", "sk", "samsung", sep="/")

#009
#print("first", end=""); print("second")

#010
#print(5/3)

#011
#삼성전자 = 50000
#총평가금액 = 삼성전자 * 10
#print(총평가금액)

#012
#시가총액 = 29800000000
#현재가 = 50000
#PER = 15.79
#print("시가총액", type(시가총액))
#print("현재가", type(현재가))
#print("PER", type(PER))

#013
#s = "hello"
#t = "python"
#print(s + "!", t)

#014
#print(2+2*3)

#015
#a = "132"
#print(type(a))

#016
# num_str = "720"
# num_int = int(num_str)
# print(num_int+1, type(num_int))

#017
# num = 100
# result = str(num)
# print(result, type(result))

#018
# data = "15.79"
# data = float(data)
# print(data, type(data))

#019
# year = "2020"
# print(int(year)-3)
# print(int(year)-2)
# print(int(year)-1)

#020
# 월 = 48584
# 총금액 = 월 * 36
# print(총금액)

#021
# letter = 'python'
# lang = 'python'
# print(lang[0], lang[2])

#022
# license_plate = "24가 2210"
# print(license_plate[4:8])
# print(license_plate[4:])
# print(license_plate[-4:])
#마지막 자리 생략 가능

#023
# string = "홀짝홀짝홀짝"
# print(string[0:6:2])
# print(string[::2])

#024
# string = "python"
# print(string[::-1])

#025
# phone_number = "010-1111-2222"
# phone_number1 = phone_number.replace("-", " ")
# print(phone_number1)

#026
# phone_number = "010-1111-2222"
# phone_number1 = phone_number.replace("-", "")
# print(phone_number1)

#027
# url = "http://sharebook.kr"
# url_split = url.split('.')
# print(url_split[-1])

#028-결과예측
# lang = 'python'
# lang[0] = 'p'
# print(lang)
#실행 안 됨

#029
# string = 'abcdfe2a354a32a'
# string = string.replace('a', 'A')
# print(string)

#030-결과예측
# string = 'abcd'
# string.replace('b', 'B')
# print(string)
#전환 안 됨

#031
# a = "3"
# b = "4"
# print(a + b)

#032
# print("hi"*3)

#033
# print("-"*80)

#034
# t1 = 'python'
# t2 = 'java'
# t3 = t1 + ' ' + t2 + ' '
# print(t3*4)

#035
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print("이름: %s 나이: %d" % (name1, age1))
# print("이름: %s 나이: %d" % (name2, age2))

#036
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print("이름: {} 나이 {}". format(name1, age1))
# print("이름: {} 나이 {}". format(name2, age2))

#037
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print(f"이름: {name1} 나이: {age1}")
# print(f"이름: {name2} 나이: {age2}")

#038
# 상장주식수 = "5,969,782,550"
# 컴마제거 = 상장주식수.replace(",","")
# 타입변환 = int(컴마제거)
# print(타입변환, type(타입변환))

#039
# 분기 = "2020/03(E) (IFRS연결)"
# print(분기[:7])

#040
# data = "   삼성전자   "
# data1 = data.strip()
# print(data1)

#041
# ticker = "btc_krw"
# a = ticker.upper()
# print(a)

#042
# ticker = "BCT_KRW"
# a = ticker.lower()
# print(a)

#043
# a = "hello"
# a = a.capitalize()
# print(a)

#044
# file_name = "보고서.xlsx"
# print(file_name.endswith("xlsx"))

#045
# file_name = "보고서.xlsx"
# print(file_name.endswith(("xlsx", "xls")))

#046
# file_name = "2020_보고서.xlsx"
# print(file_name.startswith("2020"))

#047
# a = "hello world"
# print(a.split())

# #048
# ticker = "btc_krw"
# print(ticker.split('_'))

#049
# date = "2020-05-01"
# print(date.split('-'))
# split을 이용하여 공백이 아닌 다른 문자를 지울때는 ''나 ""를 사이에 표시할 것

#050
# data = "039490      "
# print(data.rstrip())
# # rstrip 오른쪽 공백 제거
# # strip 양쪽 공백 제거
# # lstrip 왼쪽 공백 제거

#051
# movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]

# #052
# movie_rank.append("배트맨")
# print(movie_rank)